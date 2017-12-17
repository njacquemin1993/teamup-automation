from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

import main.views

urlpatterns = [
    url(r'^$', main.views.WodListView.as_view(), name='wod-list-view'),
    url(r'^create/$', main.views.WodCreateView.as_view(), name='wod-create-view'),
    url(r'^update/(?P<pk>\d+)/$', main.views.WodUpdateView.as_view(), name='wod-update-view'),
    url(r'^delete/(?P<pk>\d+)/$', main.views.WodDeleteView.as_view(), name='wod-delete-view'),
]
