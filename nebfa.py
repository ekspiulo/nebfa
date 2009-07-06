# Copyright 2009 New England Biolabs <davisp@neb.com>
#
# This file is part of the nebfa package released under the MIT license.
#

import re

# From the Blast book
IDENT_TYPES = set(
    "dbj emb gb gi ref pir prf sp pdb pat bbs lcl gnl".split()
)    

class Reader(object):
    def __init__(self, stream):
        self.stream = itertools.ifilter(Reader.skipblank, stream)
        self.next = None

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
        if self.next is not None:
            ret = self.next
            self.next = None
            return ret
        line = self.steram.next().lstrip()
        if not line[:1] == ">":
            raise ValueError("Invalid definition line: %s" % line)
        return line

    def next(self):
        if self.next:
            raise StopIteration
        line = self.stream.next().lstrip()
        if line[:1] == ">":
            self.next = line
            raise StopIteration
        return line

class Record(object):
    def __init__(self, stream):
        hdr = stream.nextheader()
        self.headers = self.parse_defline(hdr)
        self.id, self.desc = self.headers[0]
        self.seqiter = stream

    def parse_defline(self, data):
        if data[:1] != ">":
            raise ValueError("Invalid header has no '>': %s" % header)
        data = data[1:].split('\x01')
        ret = []
        for h in headers:
            bits = h.split(None, 1)
            ident, desc = bits[0], bits[1:] or None
            ident = self._parse_id(ident)
            ret.append((ident, desc))
        return ret
    
    def _parse_id(self, data):
        bits = data.split("|")
        if len(bits) == 1:
            return ident
        ret = {}
        while len(bits) > 0:
            itype = bits[0]
            parts = []
            for b in bits[1:]:
                if b in IDENT_TYPES: break
                parts.append(b)
            bits = bits[len(parts)+1:]
            parts = filter(None, parts)
            if len(parts) == 1:
                parts = parts[0]
            if isinstance(ret.get(itype, None), list):
                ret[itype].append(parts)
            elif itype in ret:
                ret[itype] = [ret[itype], parts]
            else:
                ret[itype] = parts
        return ret

def parse(stream):
    if isinstance(stream, types.StringTypes):
        reader = Reader.fromstring(stream)
    else:
        reader = Reader(iter(stream))
    
    handle = stream.Stream(filename, handle)
    for line in handle:
        if line.lstrip()[:1] == ">":
            descs = parse_description(line.strip())
            seqiter = parse_sequence(handle)
            if not stream_seq:
                seqiter = ''.join(list(seqiter))
            yield FastaRecord(descs, seqiter)


def parse_sequence(handle):
    for line in handle:
        if line.lstrip()[:1] == ">":
            handle.undo(line)
            raise StopIteration()
        yield line.strip()
