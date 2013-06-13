# Copyright 2010-2012 Canonical Ltd.  This software is licensed under
# the GNU Lesser General Public License version 3 (see the file LICENSE).

from django.contrib import admin
from example_app.models import Post


class PostAdmin(admin.ModelAdmin):

    list_display = ('author', 'title', 'created_at')


admin.site.register(Post, PostAdmin)
