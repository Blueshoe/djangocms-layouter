import os
from distutils.core import setup
from layouter import __version__


def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()


CLASSIFIERS = [
    'Development Status :: 4 - Beta',
    'Framework :: Django',
    'Environment :: Web Environment',
    'Intended Audience :: Developers',
    'Operating System :: OS Independent',
    'Programming Language :: Python',
    'Programming Language :: Python :: 2',
    'Programming Language :: Python :: 2.7',
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.4',
    'Programming Language :: Python :: 3.5',
    'Topic :: Internet :: WWW/HTTP',
    'Topic :: Internet :: WWW/HTTP :: Dynamic Content',
    'Topic :: Software Development :: Libraries :: Python Modules',
    'Topic :: Software Development :: Libraries :: Application Frameworks',
]

REQUIREMENTS = [
    'django>=1.8.14',
    'django-cms>=3.4.0',
]

setup(
    name='djangocms-layouter',
    packages=['layouter'],
    version=__version__,
    description='Grid system for Django-CMS users which aims for ease of use.',
    long_description=read('README.rst'),
    license=read('LICENSE.txt'),
    author='Robert Stein',
    author_email='robert@blueshoe.de',
    url='https://github.com/Blueshoe/djangocms-layouter',
    download_url='https://github.com/Blueshoe/djangocms-layouter/archive/0.1.5.zip',
    install_requires=REQUIREMENTS,
    keywords=['django', 'Django CMS', 'grid', 'bootstrap', 'website', 'CMS', 'Blueshoe'],
    classifiers=CLASSIFIERS,
    include_package_data=True,
    zip_safe=False,
)
