# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on July 2016.
"""

from django.conf.urls import url

from .views import TasksHomeFormView


urlpatterns = [
    url(r'^$', TasksHomeFormView.as_view(), name='home'),
]
