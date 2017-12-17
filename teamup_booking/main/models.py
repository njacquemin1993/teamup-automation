# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.db import models
from django_extensions.db.models import TimeStampedModel
from django.contrib.auth.models import User

import uuid
from jsonfield import JSONField

class Wod(TimeStampedModel):
    uuid = models.UUIDField(default=uuid.uuid4, editable=False)
    user = models.ForeignKey(User)
    wod_url = models.CharField(max_length=100)
    launch_time = models.DateTimeField(default=None, null=True, blank=True)
    launched = models.BooleanField(default=False)

    def __unicode__(self):
        return u"{}: {} - {}".format(self.user.username, self.wod_url, self.launch_time)
