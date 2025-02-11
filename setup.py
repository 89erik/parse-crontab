#!/usr/bin/env python

from distutils.core import setup

try:
    with open('README.rst') as f:
        long_description = f.read()
except:
    long_description = ''

setup(
    name='parse_crontab',
    version='0.22.9',
    description='Parse and use crontab schedules in Python',
    author='Josiah Carlson',
    author_email='josiah.carlson@gmail.com',
    url='https://github.com/josiahcarlson/parse-crontab',
    packages=['parse_crontab'],
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'License :: OSI Approved :: GNU Library or Lesser General Public License (LGPL)',
        'License :: OSI Approved :: GNU Lesser General Public License v2 (LGPLv2)',
        'License :: OSI Approved :: GNU Lesser General Public License v3 (LGPLv3)',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.6',
        'Programming Language :: Python :: 2.7',
        'Programming Language :: Python :: 3.2',
        'Programming Language :: Python :: 3.3',
        'Programming Language :: Python :: 3.4',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6',
    ],
    license='GNU LGPL v2.1',
    long_description=long_description,
    #install_requires=["pytz"],
)
