import t

@t.parse("multi.fa")
def test_multi(handle):
    recs = list(t.nebfa.parse(handle))
    t.eq(len(recs), 2)
    first(recs[0])
    second(recs[1])

def first(rec):
    t.eq(rec.meta, {
        "ids": [("gi", "0120123123")],
        "desc": ["Some stuff"]
    })
    t.eq(rec.id, rec.meta["ids"][0])
    t.eq(rec.desc, rec.meta["desc"][0])
    t.eq(rec.sequence, "ACGT")
    t.eq(rec.hash, "2108994E17F6CCA9FF2352ADA92B6511DB076034")

def second(rec):
    t.eq(rec.meta, {
        "ids": [("ref", "YP_234234.2")],
        "desc": ["Another sequence"]
    })
    t.eq(rec.id, rec.meta["ids"][0])
    t.eq(rec.desc, rec.meta["desc"][0])
    t.eq(rec.sequence, "TCGCGACTAGCATACGTACACAGCTA")
    t.eq(rec.hash, "8250AA0B3D91A87AC2F5F1499A9EE615D520606D")
    