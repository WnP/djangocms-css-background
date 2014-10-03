# -*- coding: utf-8 -*-
from setuptools import setup, find_packages


setup(
    name='djangocms-css-background',
    version='0.0.1',
    description='A django-cms plugin which allow you to edit css background image or color from the edit mode',
    author='Steeve',
    author_email='mo0ofier@gmail.com',
    include_package_data=True,
    url='https://github.com/WnP/djangocms-css-background',
    packages=find_packages(),
    classifiers=[
        'Development Status :: 4 - Beta',
        'Environment :: Web Environment',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    zip_safe=False,
)

## Installation by Mauricio Aizga - @MaoAiz