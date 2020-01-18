# Setup file for Python DI
#
# Copyright (C) 2012  Red Hat, Inc.
#
# This program is free software: you can redistribute it and/or modify
# it under the terms of the GNU General Public License as published by
# the Free Software Foundation, either version 2 of the License, or
# (at your option) any later version.
#
# This program is distributed in the hope that it will be useful, but
# WITHOUT ANY WARRANTY; without even the implied warranty of
# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the GNU
# General Public License for more details.
#
# You should have received a copy of the GNU General Public License
# along with this program.  If not, see
# <http://www.gnu.org/licenses/>.
#
# Red Hat Author(s): Martin Sivak <msivak@redhat.com>
#

import os
from setuptools import setup

# Utility function to read the README file.
# Used for the long_description.  It's nice, because now 1) we have a top level
# README file and 2) it's easier to type in the README file than to put a raw
# string in below ...
def read(fname):
    return open(os.path.join(os.path.dirname(__file__), fname)).read()

setup(
    name = "di",
    version = "0.3",
    author = "Martin Sivak",
    author_email = "msivak@redhat.com",
    description = ("Python module which provides decorators to make "
                   "dependency injection easy to use."),
    license = "GPLv2+",
    keywords = "testing dependency injection IoC",
    url = "http://fedorapeople.org/cgit/msivak/public_git/python-di.git/",
    packages = ['di'],
    setup_requires= ['nose>=1.0'],
    test_suite = "di",
    long_description=read('README'),
    classifiers=[
        "Development Status :: 3 - Alpha",
        "Intended Audience :: Developers",
        "Topic :: Software Development :: Testing",
        "License :: OSI Approved :: GNU General Public License v2 or later (GPLv2+)",
    ],
)
