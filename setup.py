#!/usr/bin/env python

"""The setup script."""
from requirements import *
from setuptools import setup, find_packages

with open('README.rst') as readme_file:
    readme = readme_file.read()

with open('HISTORY.rst') as history_file:
    history = history_file.read()

setup(
    author="Anselmo Lira (https://github.com/aberriel)",
    python_requires='>=3.7',
    classifiers=[
        'Development Status :: 2 - Pre-Alpha',
        'Intended Audience :: Developers',
        'Natural Language :: English',
        'Programming Language :: Python :: 3.7',
        'Programming Language :: Python :: 3.8',
    ],
    description="Classes to implement a Clean Architecure Python Framework",
    entry_points={
        'console_scripts': [
            'clean_architecture_basic_classes=clean_architecture_basic_classes.cli:main',
        ],
    },
    install_requires=requirements,
    long_description=readme + '\n\n' + history,
    include_package_data=True,
    keywords='clean_architecture_basic_classes',
    name='clean_architecture_basic_classes',
    packages=find_packages(include=['clean_architecture_basic_classes', 'clean_architecture_basic_classes.*']),
    test_suite='tests',
    url='https://github.com/aberriel/clean_architecture_basic_classes',
    version='0.1.0',
    zip_safe=False,
)
