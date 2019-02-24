'''
option declarations. The options will be used to update the
settings dict in module common.
'''
import argparse
import mol2chemfig.common


def getParser():
    '''
    make sure the parser is created anew on each request
    '''
    parser = argparse.ArgumentParser(
        description=mol2chemfig.common.HEADER,
        epilog=mol2chemfig.common.FOOTER)

    parser.add_argument(
        "--i", "--input",
        default="file",
        type=str,
        choices="direct file pubchem".split(),
        help="""How to interpret the argument. With 'file', mol2chemfig
                expects a filename. With 'direct', the argument is
                intrepreted directly; don't forget to put quotes around
                it. With 'pubchem', the argument is treated as an
                identifier for the PubChem database.""")

    parser.add_argument(
        "--z", "--terse",
        type=bool,
        default=False,
        help="Remove all whitespace and comments from the output.")

    parser.add_argument(
        "--r", "--strict",
        default=True,
        type=bool,
        help="""Abide by Indigo's chemical structure validation.
                If true, mol2chemfig will fail if Indigo reports
                that something is wrong with the molecule, like
                a carbon with five bonds. If false, mol2chemfig
                will ignore such errors""")

    parser.add_argument(
        "--d", "--indent",
        default=4,
        type=int,
        help="""Number of spaces to use for indenting molecule
                branches in generated code. Without effect when
                'terse' option is passed. Affects only the generated
                tex code, not the rendered molecule""")

    parser.add_argument(
        "--u", "--recalculate-coordinates",
        default=True,
        type=bool,
        help="""Discard existing coordinate and calculate new
                ones from covalent structure. For smiles input,
                this is performed implicitly""")

    # rotate?!!
    parser.add_argument(
        "--a", "--angle",
        type=float,
        default=0.0,
        help="Rotate molecule counterclockwise by this angle")

    parser.add_argument(
        "--v", "--relative-angles",
        type=bool,
        default=False,
        help="Use relative bond angles")

    # key="flip_horizontal"  
    parser.add_argument(
        "--p", "--flip",
        type=bool,
        default=False,
        help="Flip the structure horizontally")

    # key="flip_vertical"
    parser.add_argument(
        "--q", "--flop",
        type=bool,
        default=False,
        help="Flip the structure vertically")

    parser.add_argument(
        "--c", "--show-carbons",
        type=bool,
        default=False,
        help="Show element symbol for carbon atoms")

    parser.add_argument(
        "--m", "--show-methyls",
        type=bool,
        help='''Show element symbols for methyl groups
                     (implied if show-carbons is True)''')

    parser.add_argument(
        "--y", "--hydrogens",
        default="keep",
        choices="keep add delete".split(),
        help="""How to deal with explicit hydrogen atoms.
                One of 'keep', 'add' or 'delete'. Note that
                'add' will also trigger calculation of new
                coordinates for the entire molecule.
                Option 'keep' does nothing""")

    parser.add_argument(
        "--o", "--aromatic-circles",
        type=bool,
        default=False,
        help="Draw circles instead of double bonds inside aromatic rings")

    parser.add_argument(
        "--f", "--fancy-bonds",
        type=bool,
        default=False,
        help="Draw fancier double and triple bonds")

    parser.add_argument(
        "--g", "--markers",
        type=str,
        help="""Give each atom and each bond a unique
                marker that can be used for attaching
                electron movement arrows.
                With value 'a', atom 2 will be labeled
                @{a2}, and its bond to atom 5 @{a2-5}.""")

    parser.add_argument(
        "--n", "--atom-numbers",
        type=bool,
        default=False,
        help="""Show the molfile number of each atom next to it.
                     When this option is set, charges and implicit
                     hydrogens will not be shown""")

    parser.add_argument(
        "--s", "--bond-scale",
        type=str,
        default="normalize",
        choices="normalize keep scale".split(),
        help="""How to scale the lengths of bonds
                     (one of 'keep', 'scale', or 'normalize')""")

    parser.add_argument(
        "--t", "--bond-stretch",
        type=float,
        default=1.0,
        help="""Used as scaling factor (with --bond-scale=scale)
                or average (with --bond-scale=normalize) for bond
                lengths""")

    # key="chemfig_command",
    parser.add_argument(
        "--w", "--wrap-chemfig",
        type=bool,
        help=r"Wrap generated code into \chemfig{...} command")

    parser.add_argument(
        "--l", "--submol-name",
        type=str,
        help=r"""If a name is given, wrap generated code into
                      chemfig \definesubmol{name}{...} command""")

    parser.add_argument(
        "--e", "--entry-atom",
        default=None,
        help="""Number of first atom to be rendered. Relevant only
                     if generated code is to be used as sub-molecule""")

    parser.add_argument(
        "--x", "--exit-atom",
        default=None,
        help="""Number of last atom to be rendered. Relevant only
                     if generated code is to be used as sub-molecule""")

    # NOTE(meawoppl) - likely broken as ported
    parser.add_argument(
        "--k", "--cross-bond",
        default=None,
        help="""Specify bonds that should be drawn on top of others
                they cross over. Give the start and the end atoms.
                Example for one bond: --cross-bond=5-6
                Example for two bonds: --crossbond=4-8,12-13""")

    parser.add_argument(
        "target",
        metavar="TARGET",
        type=str,
        required=True,
        help="A filename or smiles input based on --i")

    # NOTE(meawoppl) - PORTED FROM HARDCODED.  Don't reccomend changing
    parser.add_argument(
        "--input_mode",
        choices=["auto"],  # "auto molfile molblock smilesfile smiles".split()?
        default="auto")

    parser.add_argument(
        "--relative_angles",
        default=False,
        choices=[False])

    parser.add_argument(
        "--bond_round",
        default=3,
        choices=[3],
        help="round bond lengths to this many decimal digits")

    parser.add_argument(
        "--angle_round",
        default=1,
        choices=[1],
        help="round angles to this many digits")

    parser.add_argument(
        "--quadrant_tolerance",
        default=0.1,
        choices=[0.1],
        help="tolerance for angle impingement on atom quadrants, range 0 to 1")

    return parser


if __name__ == '__main__':
    parser = getParser()
    parser.print_help()
