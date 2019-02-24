import sys

from mol2chemfig.options import getParser

program = "mol2chemfig"
version = "2.0.0"


class MCFError(Exception):
    '''
    this flags an anticipated error due to faulty user input.
    '''
    pass

# pubchem url for retrieving sdf for numerical IDs
pubchem_url = r"http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid=%s&disopt=DisplaySDF"

HEADER = """
{program} version {version}

mol2chemfig generates chemfig code from molfiles.
For more information, type '{program} --help'.
""".format(program=program, version=version)

FOOTER = '''
{program} v. {version}, by:
- Eric Brefo-Mensah
- Michael Palmer
- Matthew Goodman

{program} generates chemfig code from molfiles. Usage example:

{program} --angle=45 --aromatic-circles somefile.mol
'''.format(program=program, version=version)


# the settings dict contains a number of fixed settings that can not
# be overridden from the command line. A copy of this dict will
# augmented with command line options and passed around during processing.
settings = dict(
    # input mode: auto, molfile, molblock, smilesfile, smiles
    input_mode='auto',

    # use relative angles
    relative_angles=False,

    # round bond lengths to this many decimal digits
    bond_round=3,

    # round angles to this many digits
    angle_round=1,

    # tolerance for angle impingement on atom quadrants, range 0 to 1
    quadrant_tolerance=0.1,
)


class Counter:
    '''
    a simple Counter class, just to remove the dependency on version 2.7
    (which provides one in module collections)
    '''
    def __init__(self, lst):
        self._d = {}
        assert len(lst) != 0, "Can not count empty..."

        for val in lst:
            if val not in self._d:
                self._d[val] = 0

            self._d[val] += 1

    def most_common(self):
        lst = self._d.items()
        lst.sort(key=lambda pair: pair[1])

        return lst[-1][0]
