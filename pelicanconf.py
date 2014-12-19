#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Charles Butler'
SITENAME = u'Chuck@Home'
SITEURL = 'http://blog.dasroot.net'

PATH = 'content'
PLUGIN_PATH = 'pelican-plugins'
PLUGINS = ['googleplus_comments']
STATIC_PATHS = ['images']
TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

THEME = u'svbremix'
GOOGLE_ANALYTICS = u'UA-29116636-1'
TAGLINE = 'juju deploy happiness'
INTERNET_DEFENSE_LEAGUE = True
# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('About Chuck', 'http://charlesbutler.me/'),
         ('My GPG Key', 'http://blog.juju.solutions/'),
         ('Archives', 'http://blog.dasroot.net/archives'))

# Social widget
SOCIAL = (('Github', 'http://github.com/chuckbutler'),
         ('Twitter', 'http://twitter.com/lazypower'),
         ('Google+', 'https://plus.google.com/+CharlesButlertheNinja'))

DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True
