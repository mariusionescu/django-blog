#!/usr/bin/env python
import os
from setuptools import setup, find_packages

f = open(os.path.join(os.path.dirname(__file__), 'README.md'))
readme = f.read()
f.close()

setup(
    name='django-blog',
    version='0.1',
    package_dir={'django-blog': 'blog'},
    description='A very simple django blog application.',
    author='Marius Ionescu',
    author_email='marius@appix.io',
    url='https://github.com/mariusionescu/django-blog.git',
    license='BSD',
    packages=find_packages(),
    include_package_data=True,
    zip_safe=False,
    classifiers=[
        'Development Status :: 5 - Production/Stable',
        'Environment :: Web Environment',
        'Framework :: Django',
        'Intended Audience :: Developers',
        'License :: OSI Approved :: BSD License',
        'Operating System :: OS Independent',
        'Programming Language :: Python',
    ],
    keywords='django,cms',
)
