# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on July 2016.
"""

from django.contrib import admin

from models import SourceURL


@admin.register(SourceURL)
class SourceURLModelAdmin(admin.ModelAdmin):
    list_display = ('url', 'title', 'created_on', 'updated_on', 'heading',
                    'encoding', 'job_id')