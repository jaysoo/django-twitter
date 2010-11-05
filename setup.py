from setuptools import setup, find_packages

setup(
    name = "django-tweet",
    version = "0.1",
    url = 'http://github.com/jaysoo/django-tweet',
    license = 'MIT',
    description ='Manages twitter accounts a for Django project',
    author = 'Jack Hsu',
    packages = find_packages('django_tweet'),
    package_dir = {'': 'django_tweet'},
    install_requires = ['setuptools'],
)
