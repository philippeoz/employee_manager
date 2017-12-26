from decouple import config

from .base import BASE_DIR, DEBUG


# URLs to serve media and static files
# STATIC_URL = '/static/'
# MEDIA_URL = '/media/'
MEDIA_URL = config('MEDIA_URL', default='/media/')
STATIC_URL = config('STATIC_URL', default='/static/')


# Directories to save media and compiled static files
# STATIC_ROOT = 'staticfiles'
# MEDIA_ROOT = os.path.join(BASE_DIR, 'media')
STATIC_ROOT = BASE_DIR.child('frontend', 'staticfiles')
MEDIA_ROOT = BASE_DIR.child('media')


# Directories to find static files
# STATICFILES_DIRS = (
#     os.path.join(BASE_DIR, 'static'),
# )
STATICFILES_DIRS = [
    BASE_DIR.child('frontend', 'static'),
    # BASE_DIR.child('frontend', 'bower_components'),
]

# Static files finding engines
STATICFILES_FINDERS = [
    'django.contrib.staticfiles.finders.FileSystemFinder',
    'django.contrib.staticfiles.finders.AppDirectoriesFinder',
    # 'compressor.finders.CompressorFinder',
]

# Pre-processing and compression
# _bower = BASE_DIR.child('frontend', 'bower_components')

# _sass_includes = ' '.join(
#     ['--include-path={}'.format(_bower.child('susy', 'sass')), ]
# )

# COMPRESS_PRECOMPILERS = [
#     ('text/x-scss', 'sassc {infile} {outfile} ' + _sass_includes),
# ]

# COMPRESS_PRECOMPILERS = [
#    ('text/x-scss', 'sassc {infile} {outfile}'),
# ]

# COMPRESS_CSS_FILTERS = [
#     'compressor.filters.cssmin.rCSSMinFilter',
# ]

# COMPRESS_JS_FILTERS = [
#     'compressor.filters.jsmin.JSMinFilter',
# ]

# Template finders and processors
TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [
            BASE_DIR.child('frontend', 'templates'),
        ],
        'OPTIONS': {
            'debug': DEBUG,
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
                'django.template.context_processors.media',
            ],
            'loaders': [
                'django.template.loaders.filesystem.Loader',
                'django.template.loaders.app_directories.Loader',
            ],
        },
    },
]
