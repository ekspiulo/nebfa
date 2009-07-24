import t

@t.parse("multidef.fa")
def test_multi(handle):
    recs = list(t.nebfa.parse(handle))
    t.eq(len(recs), 2)
    first(recs[0])
    second(recs[1])

def first(rec):
    t.eq(rec.meta, {
        'ids': [
            ('gi', '15674171'),
            ('ref', 'NP_268346.1'),
            ('gi', '116513137'),
            ('ref', 'YP_812044.1'),
            ('gi', '125625229'),
            ('ref', 'YP_001033712.1'),
            ('gi', '13878750'),
            ('sp', 'Q9CDN0.1|RS18_LACLA'),
            ('gi', '122939895'),
            ('sp', 'Q02VU1.1|RS18_LACLS'),
            ('gi', '166220956'),
            ('sp', 'A2RNZ2.1|RS18_LACLM'),
            ('gi', '12725253'),
            ('gb', 'AAK06287.1|AE006448_5'),
            ('gi', '116108791'),
            ('gb', 'ABJ73931.1'),
            ('gi', '124494037'),
            ('emb', 'CAL99037.1')
        ],
        'desc': [
            '30S ribosomal protein S18 [Lactococcus lactis subsp. lactis Il1403]',
            '30S ribosomal protein S18 [Lactococcus lactis subsp. cremoris SK11]',
            '30S ribosomal protein S18 [Lactococcus lactis subsp. cremoris MG1363]',
            'RecName: Full=30S ribosomal protein S18',
            'SSU ribosomal protein S18P [Lactococcus lactis subsp. cremoris SK11]'
        ]
    })
    t.eq(rec.id, ('gi', '15674171'))
    t.eq(rec.desc, "30S ribosomal protein S18 [Lactococcus lactis subsp. lactis Il1403]")
    t.eq(rec.sequence, ''.join("""
        MAQQRRGGFKRRKKVDFIAANKIEVVDYKDTELLKRFISERGKILPRRVTGTSAKNQ
        RKVVNAIKRARVMALLPFVAEDQN
    """.split()))
    t.eq(rec.hash, "C53CFB6A15CBD598154C31B396F57B917222EA2D")

def second(rec):
    t.eq(rec.meta, {
        'ids': [
            ('gi', '66816243'),
            ('ref', 'XP_642131.1'),
            ('gi', '1705556'),
            ('sp', 'P54670.1|CAF1_DICDI'),
            ('gi', '793761'),
            ('dbj', 'BAA06266.1'),
            ('gi', '60470106'),
            ('gb', 'EAL68086.1')
        ],
        'desc': [
            'calfumirin-1 [Dictyostelium discoideum AX4]',
            'RecName: Full=Calfumirin-1; Short=CAF-1',
            'calfumirin-1 [Dictyostelium discoideum]'
        ]
    })
    t.eq(rec.id, ('gi', '66816243'))
    t.eq(rec.desc, 'calfumirin-1 [Dictyostelium discoideum AX4]')
    t.eq(rec.sequence, ''.join("""
        MASTQNIVEEVQKMLDTYDTNKDGEITKAEAVEYFKGKKAFNPERSAIYLFQVYDKDNDGKITIKELA
        GDIDFDKALKEYKEKQAKSKQQEAEVEEDIEAFILRHNKDDNTDITKDELIQGFKETGAKDPEKSANF
        ILTEMDTNKDGTITVKELRVYYQKVQKLLNPDQ
    """.split()))
    t.eq(rec.hash, "7D6B32F721E2E8BF34A37015C11E3FBAA0C791B8")
