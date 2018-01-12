import django
from django.conf import settings
import django_heroku

settings.configure(default_settings=django_heroku.settings, DEBUG=True)
django.setup()