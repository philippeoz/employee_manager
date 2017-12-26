from decouple import Csv
from decouple import config


# Key for salting hashes and such
SECRET_KEY = config('SECRET_KEY', default='changeme')

# Host names allowed when DEBUG=False
ALLOWED_HOSTS = config('ALLOWED_HOSTS', default='*', cast=Csv())

# Password validation
# https://docs.djangoproject.com/en/1.11/ref/settings/#auth-password-validators

AUTH_PASSWORD_VALIDATORS = [
    {
        'NAME': 'django.contrib.auth.password_validation.UserAttributeSimilarityValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.MinimumLengthValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.CommonPasswordValidator',
    },
    {
        'NAME': 'django.contrib.auth.password_validation.NumericPasswordValidator',
    },
]
