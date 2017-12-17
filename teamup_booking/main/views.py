# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.shortcuts import render
from django.views.generic.list import ListView
from django.views.generic.edit import UpdateView, DeleteView, FormView, CreateView
from django.contrib.auth.decorators import login_required
from django.utils.decorators import method_decorator
from django.urls import reverse_lazy
from django.contrib import messages
from django.utils.translation import ugettext as _

from main.models import Wod
from main.forms import WodUpdateForm

@method_decorator(login_required, name='dispatch')
class WodListView(ListView):
    model = Wod
    template_name = "wod_list.html"

    def get_queryset(self):
        return Wod.objects.filter(user=self.request.user)

@method_decorator(login_required, name='dispatch')
class WodCreateView(CreateView):
    model = Wod
    form_class = WodUpdateForm
    template_name = "wod_update.html"

    def get_form_kwargs(self):
        kwargs = super(WodCreateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        messages.success(self.request, _("Successfully saved."))
        return reverse_lazy('wod-list-view')

@method_decorator(login_required, name='dispatch')
class WodUpdateView(UpdateView):
    model = Wod
    template_name = "wod_update.html"
    form_class = WodUpdateForm

    def get_form_kwargs(self):
        kwargs = super(WodUpdateView, self).get_form_kwargs()
        kwargs['user'] = self.request.user
        return kwargs

    def get_success_url(self):
        messages.success(self.request, _("Successfully saved."))
        return reverse_lazy('wod-list-view')

@method_decorator(login_required, name='dispatch')
class WodDeleteView(DeleteView):
    model = Wod
    template_name = "wod_delete.html"
    success_url = reverse_lazy("wod-list-view")

    def delete(self, request, *args, **kwargs):
        messages.success(self.request, _("Successfully deleted."))
        return super(WodDeleteView, self).delete(request, *args, **kwargs)
