What is it?
===========

This is the development buildout script for LFS. 

It will create a complete developement evironment for LFS. 

LFS is an online shop based on Python, Django and jQuery.

How to use it?
==============

1. Check it out from bitbucket
    
    $ hg clone https://bitbucket.org/diefenbach/lfs-buildout-development

2. Change to the directory

    $ cd lfs-buildout-development
    
3. Bootstrap buildout

    $ python bootstrap.py
    
4. Run buildout

    $ bin/buildout -v
    
5. Enter your database settings into lfs_project/settings.py

6. Sync your database

    $ bin/django syncdb
    
7. Initialize LFS

    $ bin/django lfs_init

8. Start server

    $ bin/django runserver
    
9. Browse to LFS

    http://localhost:8000
    
More Information
================

* `Official page <http://www.getlfs.com/>`_
* `Documentation on PyPI <http://packages.python.org/django-lfs/index.html>`_
* `Releases on PyPI <http://pypi.python.org/pypi/django-lfs>`_
* `Source code on bitbucket.org <http://bitbucket.org/diefenbach/django-lfs>`_
* `Google Group <http://groups.google.com/group/django-lfs>`_
* `lfsproject on Twitter <http://twitter.com/lfsproject>`_
* `IRC <irc://irc.freenode.net/django-lfs>`_