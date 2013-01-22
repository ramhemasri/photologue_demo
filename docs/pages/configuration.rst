#################
Project structure
#################

Requirements files
==================
This project uses several requirements files:

- ``requirements/dev.txt`` contains what you need for a development environment.
- ``requirements/prod.txt`` is for production.

Installing either of the above files will auto-install ``requirements/common.txt``,
which as the name implies contains common requirements.

Settings files
==============
Django's settings are contained in several files in folder ``/photologue_demo/settings/``, laid out as follows:

- ``common.py`` contains all the basic settings. All the other settings files
  inherit from this one.
- ``prod.py`` contains production settings.
- ``dev.py`` contains settings suitable for a development environment.

By default, ``manage.py`` uses the ``dev.py`` file, so that the project can run with 
'zero-config' for a new developer who has just installed it.

Personal files
^^^^^^^^^^^^^^
Individual developers can write their own custom settings file
that extends ``dev.py``. To get the project to use these custom settings:: 

  export DJANGO_SETTINGS_MODULE="settings.<your custom settings filename>"

If you're using virtualenvwrapper, just add the above line to the ``bin/postactivate``
file.

These custom files should be version-controlled, for 2 reasons::

1. Because the file is version-controlled, diffs are easy to spot.
2. Tricks used by one dev are always worth sharing with all.

Production environment
^^^^^^^^^^^^^^^^^^^^^^
See the :ref:`deployment-instructions-label` page for what happens in prod. 




