"""
Django settings for geodjango project.

Generated by 'django-admin startproject' using Django 3.2.13.

For more information on this file, see
https://docs.djangoproject.com/en/3.2/topics/settings/

For the full list of settings and their values, see
https://docs.djangoproject.com/en/3.2/ref/settings/
"""

from pathlib import Path
import os

# - - - - - - - - - - - - - - - - - - - - 
# environment на Mac:
# conda activate //anaconda3/envs/condageoenv
# - - - - - - - - - - - - - - - - - - - - 

# Build paths inside the project like this: BASE_DIR / 'subdir'.
BASE_DIR = Path(__file__).resolve().parent.parent

# BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))


# use this if setting up on Windows 10 with GDAL installed from OSGeo4W using defaults
# !!!ВКЛЮЧИ НА WINDOWS10!!! - - - - - - - 
if os.name == 'nt':
    VIRTUAL_ENV_BASE = os.environ['VIRTUAL_ENV']
    os.environ['PATH'] = os.path.join(VIRTUAL_ENV_BASE, r'.\Lib\site-packages\osgeo') + ';' + os.environ['PATH']
    os.environ['PROJ_LIB'] = os.path.join(VIRTUAL_ENV_BASE, r'.\Lib\site-packages\osgeo\data\proj') + ';' + os.environ['PATH']
# - - - - - - - - - - - - - - - - - - - - 

# [...] settings.py code continues


# Quick-start development settings - unsuitable for production
# See https://docs.djangoproject.com/en/3.2/howto/deployment/checklist/

# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = '2hqtBmzFZYyakoinY6JV25qd39e_88fHog1hJYMjhykADSwsm'

# SECURITY WARNING: don't run with debug turned on in production!
DEBUG = True

ALLOWED_HOSTS = ['*'] # Разрешаем доступ с любого хоста

# Application definition
INSTALLED_APPS = [
    'django.contrib.admin',
    'django.contrib.auth',
    'django.contrib.contenttypes',
    'django.contrib.sessions',
    'django.contrib.messages',
    'django.contrib.staticfiles',
    'django.contrib.gis', # Настраеваем geodjango
    'rest_framework', # REST API
    'geoapp', # My App
    'corsheaders', # CORS
]

# Для установки режима запроса "no-cors" в Django, 
# следует настроить middleware для обработки CORS (Cross-Origin Resource Sharing). 
# CORS – это механизм веб-безопасности, позволяющий серверам указывать, 
# какие ресурсы могут быть запрашиваемы скриптами веб-страниц из другого домена.
# В Django вы можете использовать пакет django-cors-headers для управления настройками CORS. 

MIDDLEWARE = [
    'corsheaders.middleware.CorsMiddleware', # CORS (Должно быть одним из первых, чтобы быть применимым к остальным запросам)
    
    'django.middleware.csrf.CsrfViewMiddleware', # csrf (токены)

    'django.middleware.security.SecurityMiddleware',
    'django.contrib.sessions.middleware.SessionMiddleware',
    'django.middleware.common.CommonMiddleware',
    'django.contrib.auth.middleware.AuthenticationMiddleware',
    'django.contrib.messages.middleware.MessageMiddleware',
    'django.middleware.clickjacking.XFrameOptionsMiddleware',
    
]

ROOT_URLCONF = 'geodjango.urls'

TEMPLATES = [
    {
        'BACKEND': 'django.template.backends.django.DjangoTemplates',
        'DIRS': [],
        'APP_DIRS': True,
        'OPTIONS': {
            'context_processors': [
                'django.template.context_processors.debug',
                'django.template.context_processors.request',
                'django.contrib.auth.context_processors.auth',
                'django.contrib.messages.context_processors.messages',
            ],
        },
    },
]

WSGI_APPLICATION = 'geodjango.wsgi.application'


# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.contrib.gis.db.backends.postgis',
        'NAME': 'test',
        'USER': 'postgres',
        'PASSWORD': 'admin',
        # 'PASSWORD': ':)',
        'HOST': 'localhost',
        'PORT': '5432',
    }
}


# Password validation
# https://docs.djangoproject.com/en/3.2/ref/settings/#auth-password-validators

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


# Internationalization
# https://docs.djangoproject.com/en/3.2/topics/i18n/

LANGUAGE_CODE = 'en-us'

TIME_ZONE = 'UTC'

USE_I18N = True

USE_L10N = True

USE_TZ = True


# Конфигурация статических файлов в Django используется для работы со всеми немодифицируемыми файлами, 
# которые ваш веб-сайт использует, такими как CSS, JavaScript, изображения и другие подобные ресурсы. 
# Ниже описано назначение каждой из секций, связанных с статическими файлами:

# 1. **STATIC_URL**: 
#    - `STATIC_URL = '/static/'` определяет базовый URL, по которому будут доступны статические файлы. 
# Он используется в шаблонах для генерации ссылок на статические файлы. Например, если у вас есть статический файл `style.css`, он будет доступен по адресу `http://<ваш_домен>/static/style.css`.

# 2. **STATICFILES_DIRS**:
#    - `STATICFILES_DIRS` — это список дополнительных директорий, 
# в которых Django будет искать статические файлы помимо стандартных путей 
# (например, `static/` в каждом приложении). В данном случае указана директория 
# `os.path.join(BASE_DIR, 'geoapp', 'static')`. 
# Это может быть полезно, если вы организовали ваши статические файлы в отдельных директориях 
# или они расположены вне приложений.

# 3. **STATIC_ROOT**:
#   - `STATIC_ROOT = BASE_DIR / 'static'` — это путь к директории на сервере, 
# в которую команда `collectstatic` будет собирать все статические файлы проекта. 
# На этапе развёртывания в production Django собирает статические файлы из всех приложений 
# и указанных дополнительных директорий в одну эту директорию, чтобы веб-сервер мог обслуживать их из одного места.

# 4. **STATICFILES_FINDERS**:
#  - `STATICFILES_FINDERS` — это список поисковых механизмов (finders), которые Django использует для нахождения статических файлов. 
#  - `"django.contrib.staticfiles.finders.FileSystemFinder"` ищет файлы в директориях, указанных в `STATICFILES_DIRS`.
#  - `"django.contrib.staticfiles.finders.AppDirectoriesFinder"` ищет файлы в директориях `static/` каждого приложения.

# Эти настройки позволяют эффективно управлять статическими ресурсами приложения Django, 
# делая их легко доступными и управляемыми как в среде разработки, так и в production.  


# Static files (CSS, JavaScript, Images)
# https://docs.djangoproject.com/en/3.2/howto/static-files/


STATIC_URL = '/static/'
STATICFILES_DIRS = [
    os.path.join(BASE_DIR, 'geoapp', 'static'), 
    ]
STATIC_ROOT = BASE_DIR / 'static' 
STATICFILES_FINDERS = [
 "django.contrib.staticfiles.finders.FileSystemFinder",
 "django.contrib.staticfiles.finders.AppDirectoriesFinder",
   ]

# Пути к медиаресурсам при организации доступа к ним посредствам БД
# Также создай папку медиа в корне сайта(проекта)
MEDIA_URL = '/media/'
MEDIA_ROOT = BASE_DIR / 'media'

# Default primary key field type
# https://docs.djangoproject.com/en/3.2/ref/settings/#default-auto-field

DEFAULT_AUTO_FIELD = 'django.db.models.BigAutoField'

# CORS_ALLOW_CREDENTIALS = True # This allows CORS requests to go in and out

# CORS_ALLOW_HEADERS = (
#     'accept',
#     'accept-encoding',
#     'authorization',
#     'content-type',
#     'dnt',
#     'origin',
#     'user-agent',
#     'x-csrftoken',
#     'x-requested-with',
# )

# CORS_ALLOWED_ORIGINS = [
#     "http://127.0.0.1:8000",
# ]

CORS_ORIGIN_ALLOW_ALL = True

# SHA256:D3LFYmfoQHBJl6M2BEuZyzIy/gggHTb9jKslWjBqJjc


# https://ru.stackoverflow.com/questions/1412894/%d0%9a%d0%b0%d0%ba-%d0%bf%d0%be%d1%81%d0%bb%d0%b0%d1%82%d1%8c-post-%d0%b7%d0%b0%d0%bf%d1%80%d0%be%d1%81-%d1%81-csrf-%d1%82%d0%be%d0%ba%d0%b5%d0%bd%d0%be%d0%bc
# Если вы используете Django ≥ 4, то теперь необходимо указывать CSRF_TRUSTED_ORIGINS в settings.py:
# CSRF_TRUSTED_ORIGINS = ['https://your-domain.com', 'https://www.your-domain.com']

CSRF_TRUSTED_ORIGINS = ['http://127.0.0.1:8000', 'https://swan-decent-shrew.ngrok-free.app']