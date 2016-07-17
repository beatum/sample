# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on July 2016.
"""

from django.db import models


class SourceURL(models.Model):
    """
    Базовая модель для хранения данных полученных в результате
    асинхронного парсинга ссылок
    """
    url = models.URLField()
    title = models.CharField(blank=True, max_length=256)
    heading = models.CharField(blank=True, max_length=256)
    encoding = models.CharField(blank=True, max_length=256)
    created_on = models.DateTimeField(auto_now_add=True)
    # устанавливаем дату и время при создании
    updated_on = models.DateTimeField(auto_now=True)
    # устанавливаем дату и время при сохранении
    results = models.CharField(blank=True, max_length=128)
    job_id = models.CharField(max_length=128)

    class Meta:
        ordering = ['-created_on',]