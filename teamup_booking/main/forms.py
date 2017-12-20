# -*- coding: utf-8 -*-

from django import forms
from django.utils.translation import ugettext as _
from pygments import highlight
from pygments.formatters import HtmlFormatter
from django.utils.safestring import mark_safe

from django.forms.formsets import BaseFormSet

from django.conf import settings

from main.models import Wod

class WodUpdateForm(forms.ModelForm):
    launch_time = forms.DateTimeField(required=False, input_formats=["%d-%m-%Y %H:%M"])

    class Meta:
        model = Wod
        fields = ["wod_url", "launch_time"]

    def __init__(self, *args, **kwargs):
        self.user = kwargs.pop('user', None)
        try:
            self.fields["launch_time"].initial = self.instance.launch_time.strftime("%d-%m-%Y %H:%M")
        except:
            pass
        super(WodUpdateForm, self).__init__(*args, **kwargs)

    def save(self):
	self.instance.user = self.user
        return super(WodUpdateForm, self).save()
