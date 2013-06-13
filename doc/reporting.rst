===============
Getting Summary
===============

You have two ways of getting a report of the latest changes. One is to
get them printed to the console, other to get them sent to the list of
recipients configured in the ``settings.py`` file.


Sending The Summary Email
=========================
To send an email, run following command::

    $ python manage.py adminaudit_email_report

This will generate an email message and send it to all recipients
configured in the settings file. The report will have changes that
happened the previous day (based on the server date).


Printing Summary to the Console
===============================
Use following::

    $ python manage.py adminaudit_report

It will print exactly the same information as it's sent via email,
just to the console.


Example Message
===============

Following is an example message sent by ``adminaudit_email_report`` or
printed by ``adminaudit_report``::

    Following is the summary of all changes made to the database via admin interface.
    
    admin's changes
    ===============
    2011-03-28 14:36:30.352990: create example_app.post (Post object)
    
    
    new's changes
    =============
    2011-03-28 14:35:51.001892: update auth.user (admin)
    
    
    This report was generated for 2011-03-28.
