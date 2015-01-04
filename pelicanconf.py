#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = 'Charles Butler'
AUTHORBIO = 'Is a seasoned devops veteran. Currently employed by Canonical. Charles works on the Juju data center orchestration platform as a charmer. His prior work includes building the #4 Pittsburgh PA Digital Marketing Agency: Level Interactive, and performing community Q/A with many Open Source projects.'
SITENAME = 'Chuck@Home'
TAGLINE = 'Juju deploy happiness'
SITEURL = 'http://blog.dasroot.net'
TIMEZONE = 'America/New_York'

PATH = 'content'
PLUGIN_PATHS = ['pelican-plugins']
PLUGINS = ['googleplus_comments', 'sitemap', 'pelican_gist', 'better_figures_and_images', 'related_posts']
STATIC_PATHS = ['images', 'pages', 'extra/robots.txt', 'extra/favicon.ico']
EXTRA_PATH_METADATA = {
    'extra/robots.txt': {'path': 'robots.txt'},
    'extra/favicon.ico': {'path': 'favicon.ico'}
}

DEFAULT_LANG = 'en'
DEFAULT_PAGINATION = 8

# Uncomment following line if you want document-relative URLs when developing
RELATIVE_URLS = True


# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None
MD_EXTENSIONS = ['extra']

# Theme Options / Settings
THEME = 'porto'
GOOGLE_ANALYTICS = 'UA-29116636-1'
SOCIAL = (('googleplus', 'https://plus.google.com/+CharlesButlertheNinja/'),
          ('twitter', 'https://twitter.com/lazypower'),
          ('linkedin', 'www.linkedin.com/pub/charles-butler/28/748/74/'),
          ('reddit', 'http://www.reddit.com/user/lazypower/'),
          ('github', 'http://www.github.com/chuckbutler'))
CALLOUT_NAV = (('In Depth with Chuck', 'http://charlesbutler.me'),
               ('My GPG Key', 'https://keybase.io/lazypower'))
NAV = (('Home', '/'), ('Videos', '/tag/video.html'))

TWITTER_WIDGET_ID = 551646827624554496


# Plugin Options
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

# Setting for the better_figures_and_images plugin
RESPONSIVE_IMAGES = True

RELATED_POSTS_MAX = 3
