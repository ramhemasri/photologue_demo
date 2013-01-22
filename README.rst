Personal framework for creating Django projects. Largely inspired by
`Django Best Practices <http://lincolnloop.com/django-best-practices/>`_, and
also by my many years of making mistakes :-)

Checklist for creating a project using this skeleton

- Create a virtualenv.
- Create the skeleton (django-admin.py startproject --template <PATH TO>/django-project-skel --extension py,rst,gitignore,html <PROJECT NAME>

Install requirements::

	cd photologue_demo
	pip install -r requirements/dev.txt

Documentation
=============

Set up Sphinx::

	cd docs
	sphinx-quickstart

Remember to answer 'yes' to 'autodoc'.

There are a couple of pre-prepared pages - link them into the documentation
index::

	.. toctree::
	   :maxdepth: 2
	
	   pages/configuration.rst
	   pages/deployment.rst


Requirements
============
Some requirements such as South are auto-installed, but you'll want to revisit
the requirements file and specify the exact revisions that have been installed
for this project.


Now delete anything up to this line, you don't need it anymore :-)
===============================================================================

#######################################
Photologue_Demo Django Project
#######################################

About
=====
This project serves 2 purposes:
- It's a quick demo of django-photologue for people who wish to try it out.
- It's also the basis of the django-photologue demo site (coming soon!).

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

The project is set up to run SQLite in dev, so no database configuration is
required. To setup the database::

	python manage.py syncdb
	python manage.py migrate

Note: You may want to get a copy of the production database instead of creating
a blank local copy. YMMV.

And finally run the project::

	python manage.py runserver

Open browser to http://127.0.0.1:8000

Configuration
=============
Head over to the Sphinx docs for this project::

	cd docs
	make html

And then open the docs under photologue_demo/docs/_build/html/index.html for
more information on configuring and using this project.
	
.. 
	Note: this README is formatted as reStructuredText so that it's in the same
	format as the Sphinx docs. 