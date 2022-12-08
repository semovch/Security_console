import os

from dotenv import load_dotenv
load_dotenv('.env')

DATABASES = {
    'default': {
        'ENGINE': os.getenv('ENGINE'),
        'HOST': os.getenv('HOST'),
        'PORT': os.getenv('PORT'),
        'NAME': os.getenv('NAME'),
        'USER': os.getenv('SERVER_USER'),
        'PASSWORD': os.getenv('PASSWORD'),
    }
}

INSTALLED_APPS = [os.getenv('INSTALLED_APPS')]

SECRET_KEY = os.getenv('SECRET_KEY')

DEBUG = os.getenv('DEBUG')

ROOT_URLCONF = os.getenv('ROOT_URLCONF')

ALLOWED_HOSTS = [os.getenv('ALLOWED_HOSTS')]


BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
TEMPLATES = [
    {
        'BACKEND': os.getenv('BACKEND'),
        'DIRS': [os.path.join(BASE_DIR, os.getenv('DIRS'))],
        'APP_DIRS': os.getenv('APP_DIRS'),
    },
]


USE_L10N = os.getenv('USE_L10N')

LANGUAGE_CODE = os.getenv('LANGUAGE_CODE')

TIME_ZONE = os.getenv('TIME_ZONE')

USE_TZ = os.getenv('USE_TZ')

DEFAULT_AUTO_FIELD = os.getenv('DEFAULT_AUTO_FIELD')
