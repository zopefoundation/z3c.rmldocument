##############################################################################
#
# Copyright (c) 2008 Zope Foundation and Contributors.
# All Rights Reserved.
#
# This software is subject to the provisions of the Zope Public License,
# Version 2.1 (ZPL).  A copy of the ZPL should accompany this distribution.
# THIS SOFTWARE IS PROVIDED "AS IS" AND ANY AND ALL EXPRESS OR IMPLIED
# WARRANTIES ARE DISCLAIMED, INCLUDING, BUT NOT LIMITED TO, THE IMPLIED
# WARRANTIES OF TITLE, MERCHANTABILITY, AGAINST INFRINGEMENT, AND FITNESS
# FOR A PARTICULAR PURPOSE.
#
##############################################################################
"""Test harness for z3c.rmldocument."""

import doctest
import os.path
import unittest


def test_suite():
    return doctest.DocFileSuite(
        'README.txt',
        optionflags=(doctest.ELLIPSIS|
                     doctest.REPORT_NDIFF|
                     doctest.NORMALIZE_WHITESPACE),
        globs={'EXAMPLE':
               os.path.join(os.path.dirname(__file__), 'examples',
                            'example%s.rml')})
