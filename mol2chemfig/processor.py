import urllib

import mol2chemfig.common
import mol2chemfig.options
import mol2chemfig.molecule

from mol2chemfig.indigo import Indigo, IndigoException


class Processor:
    '''
    parses input and invokes backend, returns result
    '''
    def __init__(self):
        parser = mol2chemfig.options.getParser()

        # data obtained from the proper source go here
        self.data_string = None

        # parse options and arguments
        self.args = parser.parse_args()

        if self.args.input == 'file':
            with open(self.args.target) as f:
                self.data = f.read()
        else:
            self.data = self.args.target

        # Check to see if the input is pubchemId
        try:
            pubchem_id = int(self.data)
            self.data = mol2chemfig.common.get_pubchem_sdf(pubchem_id)
        except ValueError:
            pubchem_id = None

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

        mol = mol2chemfig.molecule.Molecule(self.args, tkmol)

        return mol
