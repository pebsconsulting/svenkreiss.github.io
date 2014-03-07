#!/usr/bin/env python
# -*- coding: utf-8 -*- #
from __future__ import unicode_literals

AUTHOR = u'Sven Kreiss'
SITENAME = u'Sven Kreiss'
SITEURL = 'http://localhost:8000'

TIMEZONE = 'America/New_York'

DEFAULT_LANG = u'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None

# Make about page the front page
INDEX_SAVE_AS = 'blog.html'

# Blogroll
LINKS = (
	('unicodeit.net', 'http://www.unicodeit.net'),
)

# Social widget
SOCIAL = (
    ('twitter-square', 'https://twitter.com/svenkreiss'),
    ('linkedin-square', 'http://www.linkedin.com/in/svenkreiss'),
    ('github', 'https://github.com/svenkreiss/'),
)
TWITTER_USERNAME = 'svenkreiss'

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = True

STATIC_PATHS = (['images', 'files', 'extras'])

EXTRA_PATH_METADATA = {
    'extras/robots.txt': {'path': 'robots.txt'},
    'extras/favicon.ico': {'path': 'favicon.ico'},
}

THEME = "../pelican-theme-pure"

# plugins
PLUGIN_PATH = '../pelican-plugins'
PLUGINS = [
	'sitemap', 'gravatar', 'render_math',
	'liquid_tags.img', 'liquid_tags.video',
	'liquid_tags.youtube', 'liquid_tags.include_code',
	'liquid_tags.notebook',
]

# pure theme specific
COVER_IMG_URL = '/images/winter_mountains.jpg'
AUTHOR_EMAIL = 'sk@svenkreiss.com'
TAGLINE = ''
DISQUS_SITENAME = 'svenkreisscom'

ARTICLE_URL = 'blog/{slug}/'
ARTICLE_SAVE_AS = 'blog/{slug}/index.html'

PAGE_URL = PAGE_SAVE_AS = '{slug}.html'

MENUITEMS = [
	('Projects', 'projects.html'),
	('Blog', 'blog.html'),
]
DISPLAY_PAGES_ON_MENU = True


# plugin render_math
MATH = {'color':'blue', 'align':'left'}

TYPOGRIFY = True

