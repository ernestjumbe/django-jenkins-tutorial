from jenkinstutorial.settings.base import *

DEBUG = True
TEMPLATE_DEBUG = DEBUG

import os
import sys
import jenkinstutorial as project_module

PROJECT_DIR = os.path.dirname(os.path.realpath(project_module.__file__))
BASE_PATH     = os.path.dirname(PROJECT_DIR)

database_dir = os.path.join(BASE_PATH, 'databases')

if not os.path.exists(database_dir):
	os.mkdir(database_dir)

ADMINS = (
    ('You', 'your@email'),
)

MANAGERS = ADMINS

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(database_dir, 'dev.db'),
    }
}

INSTALLED_APPS += (
    'debug_toolbar',
    'django_jenkins',
  
)

#==============================================================================
# Miscellaneous local settings
#==============================================================================

#TEST_RUNNER = 'discover_runner.DiscoverRunner'

#Debug toolbar settings
#----------------------

INTERNAL_IPS = ('127.0.0.1',)


DEBUG_TOOLBAR_PANELS = (
    'debug_toolbar.panels.version.VersionDebugPanel',
    'debug_toolbar.panels.timer.TimerDebugPanel',
    'debug_toolbar.panels.settings_vars.SettingsVarsDebugPanel',
    'debug_toolbar.panels.headers.HeaderDebugPanel',
    'debug_toolbar.panels.request_vars.RequestVarsDebugPanel',
    'debug_toolbar.panels.template.TemplateDebugPanel',
    'debug_toolbar.panels.sql.SQLDebugPanel',
    'debug_toolbar.panels.signals.SignalDebugPanel',
    'debug_toolbar.panels.logger.LoggingPanel',
)

DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}

def show_toolbar(request):
    return True
SHOW_TOOLBAR_CALLBACK = show_toolbar

JENKINS_TASKS = (
    'django_jenkins.tasks.with_coverage',
    'django_jenkins.tasks.django_tests',   # select one django or
    #'django_jenkins.tasks.dir_tests'      # directory tests discovery
    'django_jenkins.tasks.run_pep8',
    'django_jenkins.tasks.run_pyflakes',
    'django_jenkins.tasks.run_jslint',
    'django_jenkins.tasks.run_csslint',    
    'django_jenkins.tasks.run_sloccount',    
    'django_jenkins.tasks.lettuce_tests',
)