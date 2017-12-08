#!/usr/bin/env python
from setuptools import setup, find_packages

__version__ = "0.0.1"

setup(
    name='Some Algorithms',
    version=__version__,
    description='',
    keywords='',
    url='git@github.com:rsk-mind/rsk-mind-framework.git',
    author='George Theofilis',
    author_email='theofilis.g@gmail.com',
    license='MIT',
    include_package_data=True,
    packages=find_packages(exclude=('tests', 'tests.*', 'doc', 'tests.*')),
    install_requires=[
            'pygraphviz'
    ],
    extras_require={
            'tests': ['nose']
    },
    zip_safe=False
)
