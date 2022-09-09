To generate translation strings, you'll want to set the appropriate flavor in a `.env` file and run something like the following:

```bash
pip install python-dotenv[cli]

dotenv -f .env-stage run src/manage.py makemessages \
  --locale en \
  --locale es \
  --locale zh_Hans \
  --ignore 'env/*' \
  --ignore 'defaultflavor/*' \
  --ignore '2014/*' \
  --ignore '2015/*' \
  --ignore '2016/*' \
  --ignore '2017/*' \
  --ignore '2018/*' \
  --ignore '2019/*' \
  --ignore 'src/sa_web/jstemplates/place-detail-survey.html' \
  --ignore 'src/sa_web/jstemplates/activity-list-item.html' \
  --ignore 'src/sa_web/jstemplates/location-string.html'

dotenv -f .env-stage run src/manage.py flavormessages \
  --locale en \
  --locale es \
  --locale zh_Hans \
  --ignore 'env/*' \
  --ignore 'defaultflavor/*' \
  --ignore '2014/*' \
  --ignore '2015/*' \
  --ignore '2016/*' \
  --ignore '2017/*' \
  --ignore '2018/*' \
  --ignore '2019/*' \
  --ignore 'src/sa_web/jstemplates/place-detail-survey.html' \
  --ignore 'src/sa_web/jstemplates/activity-list-item.html' \
  --ignore 'src/sa_web/jstemplates/location-string.html'
```

Note that in the above, the year ignores are for past PB cycles that we want to ignore, and the _jstemplates_ ignores are for templates in the base project that we have overridden in _pbnyc_.
