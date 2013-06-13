.. Django Admin Audit documentation master file, created by
   sphinx-quickstart on Thu Mar 24 11:17:26 2011.
   You can adapt this file completely to your liking, but it should at least
   contain the root `toctree` directive.

Welcome to Django Admin Audit's documentation!
==============================================

This project provides a mean to audit all changes to the models made
via the Django admin interface. It does that by saving all changes in
a separate database table with enough information so that those changes
can be potentially reverted.

Contents:

.. toctree::
   :maxdepth: 2

   installation
   configuration
   reporting
   access-preventions
