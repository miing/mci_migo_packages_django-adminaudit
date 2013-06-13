====================
 Access Preventions
====================

This document describes various ways in which the modification of
``AuditLog`` objects is accomplished. Because it's the trail which
enables reverting system to its previous state no modification to it
should be possible.

The Simplest Solution
=====================
The simplest solution would be to not show it via web admin
interface. Unfortunately will cause a lose of the ability for anybody
to easily see the changes which were made to the data. Because of that
other means are implemented which enables everybody to see the
``AuditLog`` objects but not to modify them in any way.

Change Template Override
========================
The default template for ``AuditLog``
(``adminaduit/admin/adminaudit/auditlog/change_form.html``) does not
contain any forms or any other means of modification of the data. Link
to deletion of it is also removed. 

The Last and Most Important Bit
===============================
The last and the most important part of making sure that the security
is taken care of is overriding change and delete views for
``AuditLog`` models. In both cases, if the modification is attempted
the server returns 404 Not Found HTTP status code and nothing is modified.
