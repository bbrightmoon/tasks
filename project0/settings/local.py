import os
from pathlib import Path

from .env_reader import env

BASE_DIR = Path(__file__).resolve().parent.parent.parent

# SECRET_KEY
SECRET_KEY = env('SECRET_KEY')

# ALLOWED_HOSTS
ALLOWED_HOSTS = ['*']

# DEBUG
DEBUG = os.getenv('DEBUG', 'true') == 'true'

# Database
DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.sqlite3',
        'NAME': BASE_DIR / 'db.sqlite3',
    }
}