import os

# Database
# https://docs.djangoproject.com/en/3.2/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': os.environ.get("DB_ENGINE", "django.db.backends.sqlite3"),
        'NAME': os.environ.get("DB_NAME", "db.sqlite3"),
        'USER': os.environ.get('DB_USER', 'user'),
        'PASSWORD': os.environ.get('DB_PASSWORD', 'password'),
        'HOST': os.environ.get('DB_HOST', 'localhost'),
        'PORT': os.environ.get('DB_PORT', 5432),
        'OPTIONS': {
            # Нужно явно указать схемы, с которыми будет работать приложение.
            'options': '-c search_path=public,content'
        }
    }
}
