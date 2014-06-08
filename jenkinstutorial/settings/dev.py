"""Settings for Development Server"""
from jenkinstutorial.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

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