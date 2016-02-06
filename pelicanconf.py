#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Angel Garcia R.'
SITENAME = u'/angel-garcia:'
SITEURL = u'http://localhost:8000'
SITETITLE = AUTHOR
SITESUBTITLE = u'Dev/Human'
FAVICON = SITEURL + '/img/favicon.ico'
THEME = 'pelican-elegant'

# Regional Settings
TIMEZONE = 'America/Chihuahua'
DEFAULT_LANG = u'en'

# Plugins and extensions

# Appearance
DEFAULT_PAGINATION = False

# Defaults
DEFAULT_CATEGORY = 'Miscellaneous'
USE_FOLDER_AS_CATEGORY = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Social
SOCIAL = (
        ('Twitter', 'http://twitter.com/ang3lga'),
        ('Github', 'http://github.com/angelga'),
        ('Email', 'mailto:me@agarcia.pw'),
          )

# Elegante theme
STATIC_PATHS = ['img',]

LANDING_PAGE_ABOUT = {'title': 'developer',
		'details': """<p>Hello, my name is <a href="https://www.linkedin.com/in/angelga">Angel Garcia Reyes</a>. I'm a former Microsoft developer with experience in the Windows and Office ecosystem and cloud services.</p>
		<p>I'm currently interested in Python, bash, web technologies, and *nix.</p>
		<p>I also love traveling and recently took a sabbatical and visited South America and Mexico.</p>
        <p>Before college, I volunteered for two years at the Mexican Red Cross where I was an Emergency Medical Technician.</p>
		<p>Follow me on <a href="https://twitter.com/ang3lga">twitter</a> or <a href="mailto:me@agarcia.pw">email me</a> to keep in touch.</p>"""}

# Other
GOOGLE_ANALYTICS = u'UA-73091315-1'
DISQUS_SITENAME = u'ang3lxyz'
