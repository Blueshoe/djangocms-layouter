import os
from setuptools import setup
from layouter import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


CLASSIFIERS = [
    'Framework :: Django',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.7',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

REQUIREMENTS = [
    'django>=2,<3',
    'django-cms>=3.5.0',
    'easy-thumbnails>=2.1 ',
]

setup(
    name='djangocms-layouter',
    packages=['layouter'],
    version=__version__,
    description='Grid system for Django-CMS users which aims for ease of use.',
    long_description=read('README.rst'),
    license='MIT',
    author='Robert Stein',
    author_email='robert@blueshoe.de',
    url='https://github.com/Blueshoe/djangocms-layouter',
    download_url='https://github.com/Blueshoe/djangocms-layouter/archive/1.0.0.zip',
    install_requires=REQUIREMENTS,
    keywords=['django', 'Django CMS', 'grid', 'bootstrap', 'website', 'CMS', 'Blueshoe'],
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,
    test_suite='tests.settings.run',
)
