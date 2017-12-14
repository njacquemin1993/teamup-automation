# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator

from main.models import Wod

@method_decorator(login_required, name='dispatch')
class WodListView(ListView):
    model = Wod
    template_name = "wod_list.html"
