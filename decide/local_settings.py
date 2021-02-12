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

BASEURL = 'https://examenegcalberto.herokuapp.com'

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
        'NAME': 'dba4ap4pjfndpo',
        'USER': 'evqpltgwaztjnp',
        'PASSWORD':
        'a0c933118151df7774176803effe0ebe1fb2c1bcf5601514b6ed5210e9c97f8b',
        'HOST': 'ec2-100-24-139-146.compute-1.amazonaws.com',
        'PORT': '5432',
    }
}
# number of bits for the key, all auths should use the same number of bits
KEYBITS = 256
