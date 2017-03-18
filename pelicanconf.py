#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals


AUTHOR = 'Nathanael Cunningham'
SITENAME = 'Community Hospital Of Bremen'
SITEURL = ''

# MD_EXTENSIONS = ['mdx_sections']

MARKDOWN = {
    'extension_configs': {
        'markdown.extensions.codehilite': {'css_class': 'highlight'},
        'markdown.extensions.extra': {},
        'markdown.extensions.meta': {},
        'mdx_sections': {},
    },
    'output_format': 'html5',
}

#Dont auto-generate these files
ARCHIVES_SAVE_AS = ''
AUTHORS_SAVE_AS = ''
TAGS_SAVE_AS = ''
CATEGORIES_SAVE_AS = ''

PATH = 'content'

TIMEZONE = 'EST'
LOAD_CONTENT_CACHE = False
DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None


DEFAULT_PAGINATION = False

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True
USE_FOLDER_AS_CATEGORY = False

DISPLAY_CATEGORIES_ON_MENU = False

INDEX_SAVE_AS = 'list_index.html'
THEME_STATIC_DIR = 'themes/hospital-theme/static'
THEME= 'themes/hospital-theme'
FAVICON = "favicon.ico"

STATIC_PATHS = ['images']

MENUITEMS = [
    ('Home', '/'),
    ('Page1', '/pages/page1.html'),
    ('BillPay', 'http://bremenhospital.com/online-pay.php'),
    ('Laboratory', '/pages/laboratory.html'),
]

CAROUSEL = [
    ('/images/carousel/sample.png', 'test 1'),
    ('/images/carousel/sample.png', 'test 2'),
    ('/images/carousel/sample.png', 'test 3'),
]
