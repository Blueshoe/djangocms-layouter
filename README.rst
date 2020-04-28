===================
Django-CMS Layouter
===================

.. image:: https://travis-ci.org/Blueshoe/djangocms-layouter.svg?branch=master
    :target: https://travis-ci.org/Blueshoe/djangocms-layouter
    :alt: Code analysis status

**Django-CMS Layouter** is a plugin for **Django CMS** which aims to provide a grid system for authors and editors
with a high ease of use and comprehensibility. It is leveraging `Bootstrap <http://getbootstrap.com/>`_ (version 3 and 4 supported) as it
is a very popular framework to create responsive websites.

.. image:: https://raw.githubusercontent.com/Blueshoe/djangocms-layouter/master/layouter.gif

Documentation
=============

Please feel free to contribute and help us to improve **Django-CMS Layouter**.

Installation and Configuration
------------------------------

**Django-CMS Layouter** supports Django-CMS>=3.4. It may work with any older version.

* Install via pip: ``pip install djangocms-layouter``.
* Add ``layouter`` to ``INSTALLED_APPS``.
* Add ``url(r'^layouter/', include('layouter.urls', namespace='layouter'), )`` to your url config
* Run migrations: ``python manage.py migrate layouter``.
* Set the setting ``LAYOUTER_BOOTSTRAP_VERSION`` to 3 or 4.
* Done.

Please note: Migrations are generated each release. If you checkout the current state of development
migrations might be missing.

**Static files**

The required CSS and JavaScript files are added to the sekizai blocks ``css`` and ``js``. If you don't use these blocks, you need to manually add the static files:

- ``layouter/css/layouter.css``
- ``layouter/js/layouter.js``

Both are only required when the toolbar is in ``edit_mode``.

Features
--------

These are the core features of **Django-CMS Layouter**:

* Flat tree in structure mode
* Automatic arrangement of columns, for different screen sizes
* Warning, due to too many plugins, in structure mode
* Optional equal height for columns (uses CSS3 flexbox)
* Toggle grid - show and hide grid in content mode

Migrating to Django>=2
----------------------

Make sure to update the layouter the version ``0.3.3``. Run ``python manage.py migrate``. That release contains
the old and the squashed migrations. After that update to ``>=1.0.0``.


ToDo's
------

No software is perfect, everyone's code sucks. Feel free to suggest, criticize and/or contribute.

**Dynamic Warning Updates** - Dragging and Dropping in the structure view does not update the warnings within the
plugin.

**Add support for Divio Cloud** - Adding support for the Divio Cloud, so that the Layouter is installable via
Divio Cloud control panel.

**Author / Editor Documentation** - IMHO this is one of the things Django-CMS lacks. We need more and better resources
for authors and editors. Not only for Django-CMS, this plugin needs it to, for sure.

**Advanced Mode** - Not completely sure what it should look like. The current implementation is very limited
when it comes to adapting columns for different screen sizes or using more than 4 columns. It currently is completely
defined by this plugin, which can be good, but does not have to be. Some users want the plugin to take care, others want
to control the behaviour themselves.

**Tests** - There should be something like casper.js tests, maybe there is something better.
