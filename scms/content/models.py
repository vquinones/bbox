# -*- coding: utf-8 -*-
from __future__ import unicode_literals

import uuid
from django.db import models
from django.contrib.auth.models import User
from django.utils.translation import ugettext_lazy as _
from model_utils.models import TimeStampedModel


class Content(TimeStampedModel):
    cid = models.UUIDField(primary_key=True, default=uuid.uuid4, editable=False)
    version = models.CharField(_('Version'), max_length=10)
    created_by = models.ForeignKey(User, related_name='created_by')
    updated_by = models.ForeignKey(User, related_name='updated_by')
    name = models.CharField(_('Content Type'), max_length=300, null=False, blank=False)

    def __unicode__(self):
        return self.name

    class Meta:
        ordering = ('cid', 'name')
        db_table = "content"
