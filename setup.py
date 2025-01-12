# -*- coding: utf-8 -*-
from setuptools import setup, find_packages

with open('requirements.txt') as f:
	install_requires = f.read().strip().split('\n')

from barista import __version__ as version

setup(
	name='barista',
	version=version,
	description='Frappe App Test Framework',
	author='ElasticRun',
	author_email='shreem.bansal@elastic.run',
	packages=find_packages(),
	zip_safe=False,
	include_package_data=True,
	install_requires=install_requires
)
