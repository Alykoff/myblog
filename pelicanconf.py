#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Alykoff Gali'
SITENAME = u'blog.alykoff.com'
SITEURL = ''

PATH = 'content'

TIMEZONE = 'Europe/Paris'

DEFAULT_LANG = u'ru'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Blogroll
LINKS = (('Pelican', 'http://getpelican.com/'),
         ('Python.org', 'http://python.org/'),
         ('Jinja2', 'http://jinja.pocoo.org/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 20

DATE_FORMATS = {
    'en': '%a, %d %b %Y',
    'ru': '%d.%m.%Y',
}

THEME = "c:/work/lern/themes/pelican-octopress-theme/"
SITESUBTITLE = "влияние предмета наблюдения на наблюдателя посредством наблюдения"

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
