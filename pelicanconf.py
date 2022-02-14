AUTHOR = 'Carlos Peralta'
SITENAME = 'mypelicanwebsite'
SITEURL = 'https://carlos9917.github.io/mypelicanwebsite/'

PATH = 'content'

TIMEZONE = 'Europe/Rome'

DEFAULT_LANG = 'en'

# Feed generation is usually not desired when developing
FEED_ALL_ATOM = None
CATEGORY_FEED_ATOM = None
TRANSLATION_FEED_ATOM = None
AUTHOR_FEED_ATOM = None
AUTHOR_FEED_RSS = None

# Blogroll
LINKS = (('Pelican', 'https://getpelican.com/'),
         ('Python.org', 'https://www.python.org/'),
         ('Jinja2', 'https://palletsprojects.com/p/jinja/'),
         ('You can modify those links in your config file', '#'),)

# Social widget
SOCIAL = (('You can add links in your config file', '#'),
          ('Another social link', '#'),)

DEFAULT_PAGINATION = 10

# Uncomment following line if you want document-relative URLs when developing
#RELATIVE_URLS = False

from markdown.extensions.tables import TableExtension
MARKDOWN = {
    "extensions": [TableExtension()]    
}


PLUGIN_PATHS = ['pelican-plugins',"pelican-plugins/pelican-encrypt-content/pelican/plugins"]
PLUGINS = ['encrypt_content']

#THEME = './themes/Flex'


ENCRYPT_CONTENT = {
    'title_prefix': '[Encrypted]',
    'summary': 'This content is encrypted.'
}

FAVICON = 'content/images/favicon.ico'
