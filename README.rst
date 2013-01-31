#######################################
Photologue_Demo Django Project
#######################################

About
=====
This project serves 2 purposes:

- It's a quick demo of django-photologue for people who wish to try it out.
- The 'website' branch is used for the django-photologue demo site (coming soon!).

Prerequisites
=============

- python 2.7
- virtualenvwrapper

Installation
============
**Note**: the project is configured so that it can run immediately in dev with zero configuration (especially
of settings files).

Create a virtual python environment for the project. The use of virtualenvwrapper
is strongly recommended::

	mkproject --no-site-packages photologue_demo
	or for more sophisticated setups:
	mkvirtualenv --no-site-packages photologue_demo


Obtain the url to your git repository::

	git clone <URL_TO_GIT_REPOSITORY> photologue_demo

Install requirements::

	cd photologue_demo
	pip install -r requirements/dev.txt

The project is set up to run SQLite in dev so that it can be quickly started
with no configuration required (you can of course specify another database in
the settings file). To setup the database::

	./manage.py syncdb
	./manage.py migrate

Note: You may want to get a copy of the production database instead of creating
a blank local copy. YMMV.

And finally run the project (it defaults to a safe set of settings for a dev
environment)::

	./manage.py runserver

Open browser to http://127.0.0.1:8000

Configuration
=============
Head over to the Sphinx docs for this project::

	cd docs
	make html

And then use your browser to open the docs under photologue_demo/docs/_build/html/index.html for
more information on configuring and using this project.
	
.. 
	Note: this README is formatted as reStructuredText so that it's in the same
	format as the Sphinx docs. 
