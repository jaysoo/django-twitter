__author__ = 'jack.hsu@gmail.com'
__version__ = '0.2-devel'

METADATA = dict(
    name = 'django-tweet',
    version = __version__,
    url = 'http://github.com/jaysoo/django-tweet',
    description ='Manages twitter accounts a for Django project',
    author = 'Jack Hsu',
    author_email = 'jack.hsu@gmail.com',
    packages = ['django_tweet'],
    package_data = {'': ['templates/django_tweet/*.html','templates/admin/django_tweet/twitteraccount/*.html']},
    license = 'The MIT License',
    keywords = 'twitter django oauth api',
)

SETUPTOOLS_METADATA = dict(
    install_requires = ['setuptools', 'twitter'],
    include_package_data = True,
)

def Read(file):
    return open(file).read()

def BuildLongDescription():
    return '\n'.join([Read('LICENSE'), Read('README.md')])

def Main():
    # Build the long_description from the README and CHANGES
    METADATA['long_description'] = BuildLongDescription()

    # Use setuptools if available, otherwise fallback and use distutils
    try:
        import setuptools
        METADATA.update(SETUPTOOLS_METADATA)
        setuptools.setup(**METADATA)
    except ImportError:
        import distutils.core
        distutils.core.setup(**METADATA)

if __name__ == '__main__':
    Main()
