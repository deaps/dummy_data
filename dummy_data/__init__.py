# -*- coding: utf-8 -*-
# The MIT License (MIT)
#
# Copyright (c) <year> <copyright holders>
#
# Permission is hereby granted, free of charge, to any person obtaining a copy
# of this software and associated documentation files (the "Software"), to deal
# in the Software without restriction, including without limitation the rights
# to use, copy, modify, merge, publish, distribute, sublicense, and/or sell
# copies of the Software, and to permit persons to whom the Software is
# furnished to do so, subject to the following conditions:
#
# The above copyright notice and this permission notice shall be included in all
# copies or substantial portions of the Software.
#
# THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND, EXPRESS OR
# IMPLIED, INCLUDING BUT NOT LIMITED TO THE WARRANTIES OF MERCHANTABILITY,
# FITNESS FOR A PARTICULAR PURPOSE AND NONINFRINGEMENT. IN NO EVENT SHALL THE
# AUTHORS OR COPYRIGHT HOLDERS BE LIABLE FOR ANY CLAIM, DAMAGES OR OTHER
# LIABILITY, WHETHER IN AN ACTION OF CONTRACT, TORT OR OTHERWISE, ARISING FROM,
# OUT OF OR IN CONNECTION WITH THE SOFTWARE OR THE USE OR OTHER DEALINGS IN THE
# SOFTWARE.

"""

"""

__author__ = 'João Andrade'
__email__ = 'joaoandrade2@protonmail.com'
__version__ = '0.1'

from Models import Folder, File

def build(tree):
    try:
        print_data(tree)
    except Exception as e:
        print(e)
        raise

def print_data(top, prefix = 0):
    if type(top) is Folder:
        print("-" * prefix + "-> Folder name: " + top.path)

        for item in top.content:
            if type(item) is Folder:
                print_data(item, 4 + prefix)
            else:
                print("-" * prefix + "-> File name: " +
                    item.path + " Content: " + item.content
                )
    else:
        print("-" * prefix + "-> File name: " + top.path +
            "Content: " + top.content
        )
