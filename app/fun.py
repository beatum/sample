# -*- coding: utf-8 -*-
from __future__ import unicode_literals
"""
Created by Ivan Semernyakov <direct@beatum-group.ru> on July 2016.
"""

import string
import urllib2

import BeautifulSoup as bs

from .models import SourceURL

MAX_FOR_DOWNLOAD = 300 * 1024  # 300Kb


def parse_link(url, job_id):

    task, created = SourceURL.objects.get_or_create(
        job_id=job_id,
        url=url,
        results='Упс!'
    )

    opener = urllib2.build_opener()
    opener.addheaders = [('User-agent', 'Mozilla/5.0')]

    try:
        res = opener.open(url)
        encoding = None

        content_type = res.headers.get('Content-type', None)
        # определяем Content-type с целью извлечения кодировки страницы
        # return: text/html; charset=UTF-8

        if content_type:
            charset_ind = content_type.find('charset=')
            # возвращает индекс первого вхождения искомой подстроки

            if charset_ind:
                charset = string.strip(content_type)
                # удаляем пробельные символы в начале и в конце строки

                encoding = charset[charset_ind + len('charset='):]
                # делаем срез и возвращаем нужное значение

                task.encoding = encoding

        html = res.read(MAX_FOR_DOWNLOAD)
        res.close()

        try:

            soup = bs.BeautifulSoup(
                    html,
                    fromEncoding=encoding,
                    convertEntities=bs.BeautifulStoneSoup.HTML_ENTITIES
            )

            title = soup.find('title')
            # ищем title

            if title:
                task.title = title.contents[0][:150]
            else:
                task.title = 'Не удалось определить title'

            h1 = soup.find('h1')
            # ищем h1

            if h1:
                task.heading = h1.contents[0][:150]
            else:
                task.heading = 'Не удалось найти заголовок h1'

            task.results = 'Ням!'

            task.save()

        except Exception as e:
            print e

    except urllib2.URLError as e:
        print e

    return task
