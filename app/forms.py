# -*- coding: utf-8 -*-
from __future__ import unicode_literals

"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on July 2016.
"""

from django import forms


class SourceURLForm(forms.Form):
    """
    Простая форма для добавления ссылки, которая будет поставлена
    в качестве новой задачи для последующего парсинга страница.
    Предусмотрена возможность указать время, через которое будет
    выполнен парсинг и кол-во повторений для данной задачи.
    """
    url = forms.URLField(label='URL парсируемой страницы', max_length=256,
                         help_text='URL должен начинаться с http/https, '
                                   'и не должен превышать '
                                   '256 символов')
    schedule_times = forms.IntegerField(label='Количество повторений',
                                        required=False,
                                        initial=1,
                                        help_text='Сколько раз выполнять эту '
                                                  'задачу, для однократного '
                                                  'выполнения задачи укажите 1')
    schedule_interval = forms.IntegerField(label='Интервал в секундах',
                                           required=False,
                                           initial=1,
                                           help_text='Через какое количество '
                                                     'времени выполнять эту '
                                                     'задачу, '
                                                     'указывается в секундах')

    def clean(self):
        data = super(SourceURLForm, self).clean()
        schedule_times = data.get('schedule_times')
        schedule_interval = data.get('schedule_interval')
        print data

        if schedule_times and not schedule_interval or not schedule_times and\
                schedule_interval:
            msg = 'Пожалуйста заполните два поля интервал в секундах и ' \
                  'количество повторений, либо оба поля оставьте пустыми'
            self.add_error('schedule_times', msg)
            self.add_error('schedule_interval', msg)
