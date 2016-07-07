# -*- coding: utf-8 -*-

try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('README.rst') as readme_file:
    readme = readme_file.read()

setup(
    name='dummy_data',
    version='0.0.2',
    description='Create dummy data dynamically.',
    long_description=readme,
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
