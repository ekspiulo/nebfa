
import t

@t.parse("basic.fa")
def test_basic(handle):
    recs = list(t.nebfa.parse(handle))
    t.eq(len(recs), 1)
    rec = recs[0]
    t.eq(rec.meta, {
        "ids": [("gi", "0120123123")],
        "desc": ["Some stuff"]
    })
    t.eq(rec.id, rec.meta["ids"][0])
    t.eq(rec.desc, rec.meta["desc"][0])
    t.eq(rec.sequence, "ACGT")
    t.eq(rec.hash, "2108994E17F6CCA9FF2352ADA92B6511DB076034")
