#
# Copyright 2009 New England Biolabs <davisp@neb.com>
#
# This file is part of the nebfa package released under the MIT license.
#

import os

import nebfa

def datapath(fname):
    return os.path.join(os.path.dirname(__file__), "data", fname)

class parse(object):
    def __init__(self, fname):
        self.fname = datapath(fname)
    def __call__(self, func):
        def wrap():
            with open(self.fname, "r") as handle:
                func(handle)
        wrap.func_name = func.func_name
        return wrap

def eq(a, b):
    assert a == b, "%r != %r" % (a, b)
