from __future__ import unicode_literals

import base64
import os

import logging
log = logging.getLogger(__name__)

def basic_auth_protected(application):
    username = os.environ.get('BASIC_AUTH_USERNAME')
    password = os.environ.get('BASIC_AUTH_PASSWORD')
    is_protected = (username and password)

    def not_authorized(environ, start_response, msg=None):
        start_response('401 NOT AUTHORIZED', [('WWW-Authenticate', 'Basic')])
        if msg:
            log.warn('Not authorized: ' + msg)
        yield (msg or 'Not Authorized')

    def protected_application(environ, start_response):
        auth = environ.get('HTTP_AUTHORIZATION', b'').split()
        
        if not auth or auth[0].lower() != b'basic':
            return not_authorized(environ, start_response)

        if len(auth) == 1:
            return not_authorized(environ, start_response, 'Invalid basic header. No credentials provided.')

        if len(auth) > 2:
            return not_authorized(environ, start_response, 'Invalid basic header. Credentials string should not contain spaces.')

        try:
            auth_parts = base64.b64decode(auth[1]).decode('iso-8859-1').partition(':')
        except (TypeError, UnicodeDecodeError):
            return not_authorized(environ, start_response, 'Invalid basic header. Credentials not correctly base64 encoded.')

        if (username, password) != (auth_parts[0], auth_parts[2]):
            return not_authorized(environ, start_response, 'Invalid username/password.')

        return application(environ, start_response)
    
    return protected_application if is_protected else application


def securely_connected(application):
    is_secured = (os.environ.get('HTTPS', '').lower() in ('true', 'on', 'yes'))

    def construct_url(environ):
        from urllib import quote
        url = 'https://'

        if environ.get('HTTP_HOST'):
            url += environ['HTTP_HOST']
        else:
            url += environ['SERVER_NAME']

        url += quote(environ.get('SCRIPT_NAME', ''))
        url += quote(environ.get('PATH_INFO', ''))
        if environ.get('QUERY_STRING'):
            url += '?' + environ['QUERY_STRING']
            
        return url

    def redirect_to_secure(environ, start_response):
        secure_url = construct_url(environ)
        start_response('301 PERMANENT REDIRECT', [('Location', secure_url)])
        yield 'This resource requires a secure connection. Use SSL to access %s instead.' % (secure_url,)

    def secured_application(environ, start_response):
        if environ.get('wsgi.url_scheme', '').lower() != 'https':
            return redirect_to_secure(environ, start_response)
        return application(environ, start_response)

    return secured_application if is_secured else application