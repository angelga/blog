#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Angel Garcia R.'
SITENAME = u'/angel-garcia:'
SITEURL = u'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = u'Dev/Human'
FAVICON = SITEURL + '/img/favicon.ico'
THEME = 'elegant'
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

LANDING_PAGE_ABOUT = {'title': 'developer',
		'details': """<p>Hello, my name is <a href="https://www.linkedin.com/in/angelga">Angel Garcia Reyes</a>. I'm a former Microsoft developer with experience in the Windows and Office ecosystem and cloud services.</p>
		<p>I'm currently interested in Python, bash, web technologies, and *nix.</p>
		<p>I also love traveling and recently took a sabbatical and visited South America and Mexico.</p>"""}

#TODO
#Customize theme to:
#- Also show last blog post
