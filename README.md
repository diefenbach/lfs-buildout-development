What is it?
===========

This is the development buildout script for LFS. 

It will create a complete developement evironment for [LFS](https://github.com/diefenbach/django-lfs).

LFS is an online shop based on Python, Django and jQuery.

How to use it?
==============

1. Check it out from GitHub
    
    $ git clone git@github.com:diefenbach/lfs-buildout-development.git

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

* Official page http://www.getlfs.com/
* Documentation on PyPI http://packages.python.org/django-lfs/index.html
* Releases on PyPI http://pypi.python.org/pypi/django-lfs
* Source code on GitHub https://github.com/diefenbach/django-lfs
* Google Group http://groups.google.com/group/django-lfs
* lfsproject on Twitter http://twitter.com/lfsproject
* IRC irc://irc.freenode.net/django-lfs