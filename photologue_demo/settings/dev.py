"""
A set of Django settings suitable for a development environment.
"""
from common import *

TEMPLATE_DEBUG = DEBUG = True

# Default dev database is Sqlite. In production we use postgres.
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': os.path.join(PROJECT_DIR, 'database.sql3')
    }
}

INSTALLED_APPS.append('django.contrib.admindocs')

# Send emails to stdout - avoids accidentally mailing everyone in the database!
EMAIL_BACKEND = 'django.core.mail.backends.console.EmailBackend'
EMAIL_SUBJECT_PREFIX = '[photologue_demo (dev)] '

# Need to set here the IP of the host (gurgeh) for use by debug toolbar.
INTERNAL_IPS = ('10.0.2.2',)

# Django debug toolbar.
MIDDLEWARE_CLASSES.insert(0, 'debug_toolbar.middleware.DebugToolbarMiddleware')
INSTALLED_APPS.append('debug_toolbar')
DEBUG_TOOLBAR_CONFIG = {
    'INTERCEPT_REDIRECTS': False,
}
