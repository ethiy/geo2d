#! /usr/bin/env python3
# -*- coding: <utf-8> -*-

from setuptools import setup, find_packages
from requirements import parse

from geo2d import config


def readme():
    """
    Longer description from readme.
    """
    with open('ReadMe.md', 'r') as readmefile:
        return readmefile.read()


def requirements():
    """
    Get requirements to install.
    """
    with open('requirements.txt', 'r') as req:
        return [dep.name for dep in parse(req)]


setup(
    name='geo2d',
    version=config.__version__,
    description='python package for 2d geo information: raster and vector. ',
    long_description=readme(),
    classifiers=[
        'License :: MIT License',
        'Intended Audience :: Developers',
        'Intended Audience :: Research',
        'Topic :: Scientific/Engineering',
        'Programming Language :: Python :: 3.5',
        'Programming Language :: Python :: 3.6'
    ],
    platforms=[
        'Environment :: Console',
        'Operating System :: POSIX',
        'Operating System :: MacOS',
        'Operating System :: Unix',
        'Operating System :: Windows'
    ],
    keywords='gis processing',
    url='https://github.com/ethiy/geo2d',
    author='Oussama Ennafii [IGN :: LaSTIG]',
    author_email='oussama.ennafii@ign.fr',
    license='License :: OSI Approved :: GNU General Public License v3 or later (GPLv3+)',
    packages=find_packages(exclude=['tests']),
    install_requires=requirements(),
    include_package_data=True,
    zip_safe=False
)
