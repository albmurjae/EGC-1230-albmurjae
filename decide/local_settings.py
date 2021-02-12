ALLOWED_HOSTS = ["*"]

# Modules in use, commented modules that you won't use
MODULES = [
    'authentication',
    'base',
    'booth',
    'census',
    'mixnet',
    'postproc',
    'store',
    'visualizer',
    'voting',
]

BASEURL = 'https://pruebaegcalberto.herokuapp.com'

APIS = {
    'authentication': BASEURL,
    'base': BASEURL,
    'booth': BASEURL,
    'census': BASEURL,
    'mixnet': BASEURL,
    'postproc': BASEURL,
    'store': BASEURL,
    'visualizer': BASEURL,
    'voting': BASEURL,
}


DATABASES = {
    'default': {
        'ENGINE': 'django.db.backends.postgresql',
        'NAME': 'dee895if7dcqtj',
        'USER': 'uqgnhnylevyoyz',
        'PASSWORD':
        'c5671fcf406df953b82c838e805c7904a6636869c7675f7cba98001fd8f99192',
        'HOST': 'ec2-54-145-249-177.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
