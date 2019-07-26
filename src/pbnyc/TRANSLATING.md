To generate translation strings, you'll want to set the appropriate flavor in a `.env` file and run something like the following:

```bash
foreman run -e .env src/manage.py makemessages --locale en --locale es \
  --ignore 'env/*' \
  --ignore '2016/*' \
  --ignore '2017/*' \
  --ignore '2018/*' \
  --ignore 'src/sa_web/jstemplates/place-detail-survey.html' \
  --ignore 'src/sa_web/jstemplates/activity-list-item.html' \
  --ignore 'src/sa_web/jstemplates/location-string.html'

foreman run -e .env src/manage.py flavormessages --locale en --locale es \
  --ignore 'env/*' \
  --ignore '2016/*' \
  --ignore '2017/*' \
  --ignore '2018/*' \
  --ignore 'src/sa_web/jstemplates/place-detail-survey.html' \
  --ignore 'src/sa_web/jstemplates/activity-list-item.html' \
  --ignore 'src/sa_web/jstemplates/location-string.html'
```

Note that in the above, the year ignores are for past PB cycles that we want to ignore, and the _jstemplates_ ignores are for templates in the base project that we have overridden in _pbnyc_.
