"""Settings for Production Server"""
from jenkinstutorial.settings.base import *

DEBUG = False

ADMINS = (
    #('You', 'your@email'),
)

MANAGERS = ADMINS

# Hosts/domain names that are valid for this site; required if DEBUG is False
# See https://docs.djangoproject.com/en/1.5/ref/settings/#allowed-hosts
ALOOWED_HOSTS = [
#    'example.com',
]

VAR_ROOT = '/var/www/jenkinstutorial'
MEDIA_ROOT = os.path.join(VAR_ROOT, 'uploads')
STATIC_ROOT = os.path.join(VAR_ROOT, 'static')

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': 'jenkinstutorial',
#        'USER': 'dbuser',
#        'PASSWORD': 'dbpassword',
    }
}

# WSGI_APPLICATION = 'jenkinstutorial.wsgi.dev.application'