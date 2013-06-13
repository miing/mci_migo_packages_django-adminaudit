# Copyright 2010-2012 Canonical Ltd.  This software is licensed under
# the GNU Lesser General Public License version 3 (see the file LICENSE).

from django.db import models
from django.contrib.auth.models import User


class Post(models.Model):
    author = models.ForeignKey(User)
    title = models.CharField(max_length=128)
    body = models.TextField()
    attachement = models.FileField(upload_to='attachements')
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)
    related = models.ForeignKey('self', blank=True, null=True)
