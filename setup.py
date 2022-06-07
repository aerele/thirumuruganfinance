# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

# get version from __version__ variable in thirumuruganfinance/__init__.py
from thirumuruganfinance import __version__ as version

setup(
	name='thirumuruganfinance',
	version=version,
	description='Thirumurugan Finance',
	author='Aerele Technologies Private Limited',
	author_email='vignesh@aerele.in',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
