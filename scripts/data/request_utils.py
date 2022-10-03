import requests
from sys import stderr


def request_with_retries(method, url, retries=5, session=None, **kwargs):
    session = session or requests
    responses = []
    for _ in range(retries):
        print(f'Trying to send {method} request to {url}', file=stderr)
        response = getattr(session, method)(url, **kwargs)
        if response.status_code in (200, 201, 204):
            return response
        responses.append(response)
    status_codes = [r.status_code for r in responses]
    raise Exception(f'Failed to send {method} request to {url}. Response codes: {status_codes}. Additional info: {response.text} {kwargs}')


def download_with_retries(url, retries=5, session=None):
    return request_with_retries('get', url, retries=retries, session=session)


def download_all_pages(url, session=None):
    pages = []
    while url:
        response = download_with_retries(url, session=session)
        page = response.json()
        pages.append(page)
        url = page['metadata']['next']
    return pages
