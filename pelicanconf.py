#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Charles Butler'
AUTHORBIO = 'Works for canonical as a Juju charmer'
SITENAME = 'Chuck@Home'
TAGLINE = 'juju deploy happiness'
SITEURL = 'http://blog.dasroot.net'
TIMEZONE = 'America/New_York'

PATH = 'content'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['googleplus_comments', 'sitemap', 'pelican_gist']
STATIC_PATHS = ['images', 'pages', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_LANG = 'en'

THEME = 'masonary-redux'
GOOGLE_ANALYTICS = 'UA-29116636-1'
INTERNET_DEFENSE_LEAGUE = True

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
MD_EXTENSIONS = ['extra']

# Blogroll
LINKS = (('About Chuck', 'http://charlesbutler.me/'),
         ('My GPG Key', 'http://blog.juju.solutions/'),
         ('Archives', 'http://blog.dasroot.net/archives'))

DEFAULT_PAGINATION = 9

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True

SITEMAP = {
    'format': 'xml',
    'priorities': {
        'articles': 0.5,
        'indexes': 0.5,
        'pages': 0.5
    },
    'changefreqs': {
        'articles': 'weekly',
        'indexes': 'daily',
        'pages': 'monthly'
    }
}
