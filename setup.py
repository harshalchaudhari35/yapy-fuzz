#!/usr/bin/env python
# coding: utf-8
# Copyright (c) 2023 Harshal Chaudhari
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in
# all copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN
# THE SOFTWARE.
#
# Author: Harshal Chaudhari <harshal.chaudhary@gmail.com>

import os
from setuptools import setup
from distutils.command.install import INSTALL_SCHEMES

for scheme in INSTALL_SCHEMES.values():
    scheme["data"] = scheme["purelib"]

prjdir = os.path.dirname(__file__)


def read(filename):
    return open(os.path.join(prjdir, filename)).read()


LONG_DESC = read("README.md") + "\nCHANGES\n=======\n\n" + read("CHANGES")

setup(
    name="yapy-fuzz",
    include_package_data=True,
    version=read("VERSION").strip("\n"),
    description="Python wrapper for junegunn's fuzzyfinder (fzf)",
    long_description=LONG_DESC,
    author="Harshal Chaudhari",
    license="MIT",
    author_email="harshal.chaudhary@gmail.com",
    url="https://github.com/harshalchaudhari35/yapy-fuzz",
    install_requires=["pandas"],
    # py_modules=[],
    packages=["yapyfuzz"],
    classifiers=[
        "Development Status :: 4 - Beta",
        "Environment :: Console",
        "Intended Audience :: Developers",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python",
        "Topic :: Terminals",
    ],
)
