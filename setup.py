""" Module setup for umtool project """

from setuptools import setup, find_packages

with open('README') as f:
    long_description = ''.join(f.readlines())

setup(
    name='umtool',
    version='0.1',
    description='Terminal tool for UNIX user management',
    long_description=long_description,
    author='Martin Tomes',
    author_email='jsem@martintomes.net',
    license='Public Domain',
    url='https://github.com/tomesm/umtool',
    packages=find_packages(),
    zip_safe=False,
)
