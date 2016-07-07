# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

setup(
    name='dummy_data',
    version='0.0.1',
    description='Create dummy data dynamically.',
    url='http://github.com/deaps/dummy_data',
    author='João Andrade',
    author_email='joaoandrade2@protonmail.com',
    license='MIT',
    packages=['dummy_data'],
    keywords=['dummy files', 'dummy folders', 'filesystem'],
    install_requires=[
        "lorem"
    ],
    zip_safe=False
)
