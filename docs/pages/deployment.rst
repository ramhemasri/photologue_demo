.. _deployment-instructions-label:

##########
Deployment
##########

Settings files
==============
``settings/prod.py`` contains the production settings. The ``wsgi.py`` file is
configured to pick up this settings file. When you use ``manage.py``, you need to 
tell it to use the correct settings file:: 

	export DJANGO_SETTINGS_MODULE="settings.prod"

If you're using virtualenvwrapper, just add the above line to the ``bin/postactivate``
file.