#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Copyright 2010-2012 Canonical Ltd.  This software is licensed under the
# GNU Library General Public License version 3 (see the file LICENSE).
import os

from distutils.core import setup, Command


class TestCommand(Command):
    user_options = []

    def initialize_options(self):
        pass

    def finalize_options(self):
        pass

    def run(self):
        """Run the project tests."""
        os.environ['DJANGO_SETTINGS_MODULE'] = 'django_project.settings'

        from django.core.management import call_command
        call_command('test', 'adminaudit')


setup(
    # metadata
    name='django-adminaudit',
    version='0.4.0',
    description="Extends Django's admin logging capabilities",
    url='https://launchpad.net/django-adminaudit',
    author='Łukasz Czyżykowski',
    author_email='lukasz.czyzykowski@canonical.com',
    license='LGPLv3',
    classifiers=[
        'Framework :: Django',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Topic :: Software Development :: Libraries',
        'Topic :: Software Development :: Libraries :: Python Modules',
    ],

    # content
    packages=[
        'adminaudit',
        'adminaudit.management',
        'adminaudit.management.commands',
    ],
    package_data={
        'adminaudit': [
            'templates/admin/adminaudit/auditlog/*.html',
            'templates/admin/*.html',
            'templates/adminaudit/*.txt',
        ],
    },

    # tests
    cmdclass={'test': TestCommand},
)
