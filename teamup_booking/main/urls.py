from django.conf.urls import include, url
from django.contrib.auth.decorators import login_required

import main.views

urlpatterns = [
    url(r'^$', main.views.WodListView.as_view(), name='wod-list-view'),
]
