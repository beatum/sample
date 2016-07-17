# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on July 2016.
"""

from django_rq import job
from rq import get_current_job

from .fun import parse_link


@job
def get_link(url):

    job = get_current_job()
    # создаём инстанс задачи для последующей обработки

    job_id = job.get_id()
    # вытягиваем id задачи

    task = parse_link(url, job_id)
    # передаём url и id задачи в функцию парсинга

    return task
