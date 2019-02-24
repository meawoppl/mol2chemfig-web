import urllib

from mol2chemfig.options import getParser

program = "mol2chemfig"
version = "2.0.0"


class MCFError(Exception):
    '''
    this flags an anticipated error due to faulty user input.
    '''
    pass


# pubchem url for retrieving sdf for numerical IDs
PUBCHEM_URL_TEMPLATE = r"http://pubchem.ncbi.nlm.nih.gov/summary/summary.cgi?cid=%s&disopt=DisplaySDF"


def get_pubchem_sdf(pubchem_id: int):
    return urllib.urlopen(PUBCHEM_URL_TEMPLATE % pubchem_id).read()


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
