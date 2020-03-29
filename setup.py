import os
try:
    from setuptools import setup
except ImportError:
    from distutils.core import setup

with open('requirements.txt') as f:
    required = f.read().splitlines()

setup(
    name='pydkan',
    version='0.2',
    author='CivicActions',
    author_email='devops@nucivic.com',
    license='BSD licence, see LICENCE.txt',
    description='Python Client for DKAN Dataset API',
    packages=['dkan'],
    include_package_data=True,
    zip_safe=False,
    entry_points = {},
    install_requires=required,
)
