# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _
from pygments import highlight
from pygments.formatters import HtmlFormatter
from django.utils.safestring import mark_safe

from django.forms.formsets import BaseFormSet

from django.conf import settings

from main.models import Wod

from datetime import datetime

class WodUpdateForm(forms.ModelForm):
    launch_time = forms.DateTimeField(required=False, input_formats=["%d-%m-%Y %H:%M"])

    class Meta:
        model = Wod
        fields = ["wod_url", "launch_time"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        super(WodUpdateForm, self).__init__(*args, **kwargs)
        instance = kwargs.get("instance", None)
        if instance:
            self.initial["launch_time"] = instance.launch_time.strftime("%d-%m-%Y %H:%M")

    def save(self):
	self.instance.user = self.user
        return super(WodUpdateForm, self).save()
