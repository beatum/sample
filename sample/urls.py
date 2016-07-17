# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.conf.urls import url, include
from django.contrib import admin


urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^admin/rq/', include('django_rq.urls')),
    url(r'^admin/dashboard/', include('django_rq_dashboard.urls')),
    url(r'', include('app.urls')),
]