# Copyright 2010-2012 Canonical Ltd.  This software is licensed under
# the GNU Lesser General Public License version 3 (see the file LICENSE).

from django.conf.urls.defaults import patterns, include, handler404, handler500
from django.contrib import admin

from adminaudit import audit_install

admin.autodiscover()
audit_install()

urlpatterns = patterns('',
    (r'^admin/', include(admin.site.urls)),
)
