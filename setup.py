# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


try:
    import pypandoc
    description = pypandoc.convert('README.md', 'rst')
except (IOError, ImportError):
    with open('README.md', 'rb') as f:
        description = f.read()


setup(
    name='djangocms-css-background',
    version='1.0.1b',
    license='MIT',
    description='A django-cms plugin which allow you to edit css background image or color from the edit mode',
    long_description=description,
    author='Steeve',
    author_email='mo0ofier@gmail.com',
    include_package_data=True,
    url='https://github.com/WnP/djangocms-css-background',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: MIT License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
        'Programming Language :: Python :: 2.7',
    ],
    zip_safe=False,
)

## Installation by Mauricio Aizga - @MaoAiz
