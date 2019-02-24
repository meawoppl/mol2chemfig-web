'''
accept input from command line or through the web and
return the result.
'''

import urllib

# TODO(meawoppl) - Sweep import rename
import mol2chemfig.common as common
from mol2chemfig.indigo import Indigo, IndigoException
import mol2chemfig.options as options
import mol2chemfig.molecule as molecule


class HelpError(common.MCFError):
    pass


class Processor:
    '''
    parses input and invokes backend, returns result
    '''
    def __init__(self):
        self.optionparser = options.getParser()

        # data obtained from the proper source go here
        self.data_string = None

        # parse options and arguments
        self.args = self.optionparser.parse_args()

        if self.args.input == 'file':
            with open(self.args.target) as f:
                self.data = f.read()
        else:
            self.data = self.args.target

        # Check to see if the input is pubchemId
        try:
            pubchem_id = int(self.data)
        except ValueError:
            pubchem_id = None

        if pubchem_id is not None:
            url = common.pubchem_url % pubchem_id
            self.data = urllib.urlopen(url).read()

    def get_mol(self):
        '''
        turn the input into a toolkit molecule according to user settings

        indigo is supposed to read transparently, so we can do away with
        the format setting, basically. If it's numeric, we ask pubchem,
        if it isn't, we consider it a molecule.
        '''
        tkmol = Indigo().loadMolecule(self.data)

        if self.args.hydrogens == 'add':
            tkmol.unfoldHydrogens()
            tkmol.layout()  # needed to give coordinates to added Hs

        elif self.args.hydrogens == 'delete':
            tkmol.foldHydrogens()

        if not tkmol.hasCoord() or self.args.recalculate_coordinates:
            tkmol.layout()

        mol = molecule.Molecule(self.args, tkmol)

        return mol
