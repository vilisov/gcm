#!/usr/bin/env python
from distutils.core import setup

CLASSIFIERS = [
    "Development Status :: 5 - Production/Stable",
    "Intended Audience :: Developers",
    "License :: OSI Approved :: MIT License",
    "Programming Language :: Python",
    "Programming Language :: Python :: 2.7",
    "Programming Language :: Python :: 3",
    "Programming Language :: Python :: 3.3",
    "Programming Language :: Python :: 3.4",
    "Topic :: Software Development :: Libraries :: Python Modules",
    "Topic :: System :: Networking",
]

setup(
    name='gcm',
    version='0.3',
    packages=['gcm'],
    description='Python client for Google Cloud Messaging (Android GCM)',
    author='Stas Vilisov',
    author_email='st@pirsipy.com',
    url='https://github.com/vilisov/gcm',
    keywords=['android', 'gcm', 'push', 'notification', 'google', 'cloud', 'messaging'],
    requires=['requests'],
    classifiers=CLASSIFIERS,
)
