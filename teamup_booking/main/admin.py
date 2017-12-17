# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin

from main.models import Wod

@admin.register(Wod)
class WodAdmin(admin.ModelAdmin):
    list_display = ("uuid", "user", "wod_url", "launch_time", "launched")
