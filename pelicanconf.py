#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Angel Garcia R.'
COPYRIGHT_YEAR = u'2015-2016'
SITENAME = u'/dev/angel/garcia'
SITEURL = u'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = u'Dev/Human'
SITEDESCRIPTION = u'%s\'s thoughts and projects' % AUTHOR
SITELOGO = SITEURL + '/img/profile.png'
FAVICON = SITEURL + '/img/favicon.ico'
THEME = 'Flex'
TIMEZONE = 'America/Chihuahua'

USE_FOLDER_AS_CATEGORY = True
MAIN_MENU = True

SOCIAL = (('linkedin', 'https://www.linkedin.com/in/angelga'),
          ('github', 'https://github.com/angelga'),
          ('rss', '//agarcia.pw/feeds/all.atom.xml'))

MENUITEMS = (('Archives', '/archives.html'),
             ('Categories', '/categories.html'),
             ('Tags', '/tags.html'),)

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

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
