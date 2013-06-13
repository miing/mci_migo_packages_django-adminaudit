=============
Configuration
=============

``settings``
============

These settings affect the behaviour of ``django-adminaudit``

``ADMINAUDIT_EMAILS_RECIPIENTS``
--------------------------------
List of email addresses of users which will receive a summary
report. By default it's the same as ``ADMIN`` list of Django. The
format is simpler than that list, just an iterable with email
addresses.

``ADMINAUDIT_SUMMARY_SUBJECT``
------------------------------
A subject of the summary emails which will be send out. By default
it's set to *"Admin Audit Summary"*.

``ADMINAUDIT_EMAIL_FROM``
-------------------------
An e-mail address from which report emails are being sent. It's mostly
a requirement of Django's ``send_mail`` function. By default this code
uses ``DEFAULT_FROM_EMAIL`` setting, which is set by Django.


Email report template
=====================

This code uses only one template, located in
``adminaudit/email_report.txt`` file. To override it just create a file with
the same name somewhere in one of the paths listed in the ``TEMPLATE_DIRS``
setting.

The template gets passed in the following variables:

``recipient``
  E-mail address of the person which will be getting this particular
  email.

``report_for_date``
  A ``date`` object indicating the date the report is for.

``users``
  A list of dictionaries, one for each user for which there is at least one
  ``AuditLog`` object for the reported period.  Each dictionary will have the
  following keys:

  ``caption``
    An appropriate email header
  ``underline``
    A string of equal signs, just long enough to match ``caption``.
  ``auditlogs``
    A list of AuditLogs created by this user for the reported period.


``configglue``
==============

``django-adminaudit`` doesn't directly depend on ``configglue``, but for
those projects that use it a schema is included (``adminaudit.schema``)
representing all available configuration settings.
