============
Installation
============

This project aims to be as much of an automatic solution as is
possible. Unfortunately not everything can be made fully automatic
and some manual steps are necessary.

1. First task is to install the code in such a place that the Django
   project can find it. Usually that means putting the code on the
   system path or if using virtualenv_ just ``easy_install``-ing it to
   the environment.

2. Making sure that the code is accessible from python, next step
   is to add ``adminaudit`` application to the list of installed apps
   in ``settings.py`` (or it's equivalent).  Add it to the existing
   list. Preferably it should be after ``django.contrib.admin``
   application, so that it can have access to it.

3. In the project's ``urls.py`` add following import statement::

      from adminaudit import audit_install

4. Next, add a call to the imported function. It's important that it's
   called after ``admin.autodiscover()``, because it relies on the
   structures set by that. In the end it should look like this::

       admin.autodiscover()
       audit_install()

At that point the application itself should be properly installed and
working. You can check that by logging to the Django admin interface
and check that ``Adminaudit`` application is visible on the list. Also
the ``Audit logs`` model should be visible there.

.. _virtualenv: http://pypi.python.org/pypi/virtualenv
    
