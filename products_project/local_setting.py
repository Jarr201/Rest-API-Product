# SECURITY WARNING: keep the secret key used in production secret!
SECRET_KEY = 'django-insecure-%*(i1o(*k%t%f^v1f!#2n-f_jy(*56l^1r!kvfhbfa!nl$5)t$'

# Database
# https://docs.djangoproject.com/en/4.1/ref/settings/#databases

DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.mysql',
        'NAME': 'products_database',
        'HOST': 'localhost',
        'USER': 'root',
        'PASSWORD': 'password'
    }
}