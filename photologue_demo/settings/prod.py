"""
Settings for production environment.
"""
from common import *

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql_psycopg2',
        'NAME': '',
        'USER': '',
        'PASSWORD': '',
    }
}

SEND_BROKEN_LINK_EMAILS = True

TEMPLATE_DEBUG = DEBUG = False

EMAIL_SUBJECT_PREFIX = '[photologue_demo] '

# In production we log to file rather than to console.
LOGGING['loggers']['']['handlers'] = ['file']
