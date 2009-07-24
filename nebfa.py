# Copyright 2009 New England Biolabs <davisp@neb.com>
#
# This file is part of the nebfa package released under the MIT license.
#

import hashlib
import itertools
import os
import re
import types

IDTYPES = set("dbj emb gb gi ref pir prf sp pdb pat bbs lcl gnl sha1".split())

def parse(data, stream=False):
    if isinstance(data, types.StringTypes):
        reader = Reader.fromstring(data)
    else:
        reader = Reader(iter(data))
    while True:
        yield Record(reader, stream=stream)        

def parse_file(path):
    with open(path) as handle:
        for rec in parse(handle):
            yield rec

class Record(object):
    def __init__(self, handle, stream=False):
        hdr = handle.nextheader()
        self.meta = Record.parse_defline(hdr)
        if not stream:
            hstr = HashStream(handle)
            self.sequence = ''.join(hstr)
            self.hash = hstr.hash()
        else:
            self.seqiter = HashStream(handle)
            self.hash = property(lambda self: self.seq.hash())

    @property
    def id(self):
        "Primary identifier for this record."
        return self.meta["ids"][0]
    
    @property
    def desc(self):
        "Primery description of this record."
        return self.meta["desc"][0]

    @staticmethod
    def parse_defline(data):
        if data[:1] != ">":
            raise ValueError("Invalid header has no '>': %s" % header)
        headers = data[1:].split('\x01')
        ret = {"ids": [], "desc": []}
        for h in headers:
            bits = h.split(None, 1)
            ident, desc = bits[0], bits[1].strip() or None
            for sid in Record.parse_id(ident):
                if sid not in ret["ids"]:
                    ret["ids"].append(sid)
            if desc not in ret["desc"]:
                ret["desc"].append(desc)
        return ret
    
    @staticmethod
    def parse_id(data):
        if data.find("|") < 0: return data
        bits = data.split("|")
        ret = []
        while len(bits):
            idtype = bits.pop(0)
            curr = []
            while len(bits) and bits[0] not in IDTYPES:
                curr.append(bits.pop(0))
            ret.append((idtype, '|'.join(filter(None, curr))))
        return ret

class Reader(object):
    def __init__(self, stream):
        self.stream = itertools.ifilter(Reader.skipblank, stream)
        self.header = None

    def __iter__(self):
        return self

    @staticmethod
    def skipblank(line):
        return bool(line.strip())
    
    @staticmethod
    def from_string(strdata):
        def _ter(data):
            prev = 0
            next = data.find("\n")
            while next >= 0:
                yield data[prev:next]
                prev, next = next, data.find("\n", next+1)
            yield data[prev:]
        return Reader(_iter(strdata))

    def nextheader(self):
        if self.header is not None:
            ret, self.header = self.header, None
            return ret
        line = self.stream.next().lstrip()
        if not line[:1] == ">":
            raise ValueError("Invalid definition line: %s" % line)
        return line

    def next(self):
        if self.header:
            raise StopIteration
        line = self.stream.next().lstrip()
        if line[:1] == ">":
            self.header = line
            raise StopIteration
        return line

class HashStream(object):
    def __init__(self, stream):
        self.stream = stream
        self.sha = hashlib.sha1()
        self.exhausted = False
    
    def __iter__(self):
        return self
    
    def next(self):
        if self.exhausted:
            raise StopIteration
        try:
            data = self.stream.next().strip()
        except StopIteration:
            self.exhausted = True
            raise
        self.sha.update(data)
        return data
    
    def hash(self):
        return self.sha.hexdigest().upper()


