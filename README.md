nebfa - Fasta File Parser
=========================

Usage:

    >>> import nebfa
    >>> rec = nebfa.parse(open("./test/data/basic.fa")).next()
    >>> rec.id
    ('gi', '0120123123')
    >>> rec.desc
    'Some stuff'
    >>> rec.sequence
    'ACGT'
    >>> rec.hash
    '2108994E17F6CCA9FF2352ADA92B6511DB076034'
    
    # Alternatively, parse_file avoids the need for a call to open.
    >>> for rec in nebfa.parse_file("./test/data/multi.fa"):
    ...     print rec.id
    ('gi', '0120123123')
    ('ref', 'YP_234234.2')

Records also have a meta attribute that has two keys for identifiers and
descriptions. You will need to consult that member when you have Ctl-A separated
deflines. If you have a better syntax suggestion please send a note along.
