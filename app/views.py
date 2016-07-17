# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on July 2016.
"""

import datetime

import django_rq
from django.views.generic.edit import FormView

from forms import SourceURLForm
from models import SourceURL
from task import get_link


class TasksHomeFormView(FormView):
    """
    Класс выводит форму добавления ссылки, с возможностью указать
    параметры сдвига во времени и кол-во повторений, а также полученные
    результаты парсинга.
    """
    form_class = SourceURLForm
    template_name = 'index.html'
    success_url = '/'

    def form_valid(self, form):

        url = form.cleaned_data['url']

        schedule_times = form.cleaned_data.get('schedule_times')
        # смещение во времени

        schedule_interval = form.cleaned_data.get('schedule_interval')
        # кол-во повторение

        if schedule_times and schedule_interval:
            # при наличии указанных параметров инициализируем планировщик задач
            scheduler = django_rq.get_scheduler('default')
            job = scheduler.schedule(
                scheduled_time=datetime.datetime.utcnow(),
                func=get_link,
                args=[url],
                interval=schedule_interval,
                repeat=schedule_times,
            )
        else:
            get_link.delay(url)  # однократный парсинг

        return super(TasksHomeFormView, self).form_valid(form)

    def get_context_data(self, **kwargs):
        context = super(TasksHomeFormView, self).get_context_data(**kwargs)
        context['tasks'] = SourceURL.objects.all().order_by('-created_on')
        return context
