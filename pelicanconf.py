#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Angel Garcia R.'
SITENAME = u'/angel-garcia:'
SITEURL = u'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = u'Dev/Human'
FAVICON = SITEURL + '/img/favicon.ico'
THEME = 'myidea'
TIMEZONE = 'America/Chihuahua'

USE_FOLDER_AS_CATEGORY = True

MENUITEMS = (('All posts', '/archives.html'),)

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

STATIC_PATHS = [
    'img',
    ]

DEFAULT_PAGINATION = 5