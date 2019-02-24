"""
Mock of annoying to compile library from here:
https://github.com/epam/Indigo/blob/master/api/python/indigo.py
"""


class Indigo:
    ABS = 1
    OR = 2
    AND = 3
    EITHER = 4
    UP = 5
    DOWN = 6
    CIS = 7
    TRANS = 8
    CHAIN = 9
    RING = 10
    ALLENE = 11

    SINGLET = 101
    DOUBLET = 102
    TRIPLET = 103
    RC_NOT_CENTER = -1
    RC_UNMARKED = 0
    RC_CENTER = 1
    RC_UNCHANGED = 2
    RC_MADE_OR_BROKEN = 4
    RC_ORDER_CHANGED = 8


class IndigoException(Exception):
    pass
