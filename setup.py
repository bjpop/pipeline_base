#!/usr/bin/env python

from setuptools import setup

setup(
    name='pipeline_base',
    version='1.0.0',
    author='Bernie Pope',
    author_email='bjpope@unimelb.edu.au',
    packages=['pipeline_base'],
    #entry_points={
    #    'console_scripts': ['fampipeline = src.main:main']
    #},
    url='https://github.com/bjpop/pipeline_base',
    license='LICENSE',
    description='support infrastructure for writing Bioinformatics pipelines using Ruffus',
    long_description=open('README.md').read(),
    install_requires=[
        "ruffus == 2.6.3",
        "drmaa == 0.7.6",
        "PyYAML == 3.11"
    ],
)
