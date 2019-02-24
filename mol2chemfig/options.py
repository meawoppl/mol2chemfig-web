'''
option declarations. The options will be used to update the
settings dict in module common.
'''
import mol2chemfig.optionparser as op


def getParser():
    '''
    make sure the parser is created anew on each request
    '''

    parser = op.OptionParser()

    parser.append(
        op.BoolOption(
            "help",
            "h",
            default=False,
            help_text="Print help message and exit"))

    parser.append(
        op.BoolOption(
            "version",
            "b",
            default=False,
            help_text="Print program version and exit"))

    parser.append(
        op.SelectOption(
            "input",
            "i",
            key="input",
            default="file",
            valid_range="direct file pubchem".split(),
            help_text="""How to interpret the argument. With 'file', mol2chemfig
                         expects a filename. With 'direct', the argument is
                         intrepreted directly; don't forget to put quotes around
                         it. With 'pubchem', the argument is treated as an
                         identifier for the PubChem database."""))

    parser.append(
        op.BoolOption(
            "terse",
            "z",
            default=False,
            help_text="""Remove all whitespace and comments from the output.
                         If you can still read it afterwards, Bill Gates
                         wants your resume"""))

    parser.append(
        op.BoolOption(
            "strict",
            "r",
            default=True,
            help_text="""Abide by Indigo's chemical structure validation.
                         If true, mol2chemfig will fail if Indigo reports
                         that something is wrong with the molecule, like
                         a carbon with five bonds. If false, mol2chemfig
                         will ignore such errors"""))

    parser.append(
        op.IntOption(
            "indent",
            "d",
            default=4,
            help_text="""Number of spaces to use for indenting molecule
                         branches in generated code. Without effect when
                         'terse' option is passed. Affects only the generated
                         tex code, not the rendered molecule"""))

    parser.append(
        op.BoolOption(
            "recalculate-coordinates",
            "u",
            key="recalculate_coordinates",
            help_text="""Discard existing coordinate and calculate new
                         ones from covalent structure. For smiles input,
                         this is performed implicitly"""))

    parser.append(
        op.FloatOption(
            "angle",
            "a",
            key="rotate",
            default=0.0,
            help_text="Rotate molecule counterclockwise by this angle"))

    parser.append(
        op.BoolOption(
            "relative-angles",
            "v",
            key="relative_angles",
            default=False,
            help_text="Use relative bond angles"))

    parser.append(
        op.BoolOption(
            "flip",
            "p",
            key="flip_horizontal",
            default=False,
            help_text="Flip the structure horizontally"))

    parser.append(
        op.BoolOption(
            "flop",
            "q",
            key="flip_vertical",
            default=False,
            help_text="Flip the structure vertically"))

    parser.append(
        op.BoolOption(
            "show-carbons",
            "c",
            key="show_carbons",
            help_text="Show element symbol for carbon atoms"))

    parser.append(
        op.BoolOption(
            "show-methyls",
            "m",
            key="show_methyls",
            help_text='''Show element symbols for methyl groups
                        (implied if show-carbons is True)'''))

    parser.append(
        op.SelectOption(
            "hydrogens",
            "y",
            key="hydrogens",
            # default="keep",
            valid_range="keep add delete".split(),
            help_text="""How to deal with explicit hydrogen atoms.
                        One of 'keep', 'add' or 'delete'. Note that
                        'add' will also trigger calculation of new
                        coordinates for the entire molecule.
                        Option 'keep' does nothing"""))

    parser.append(
        op.BoolOption(
            "aromatic-circles",
            "o",
            key="aromatic_circles",
            default=False,
            help_text="Draw circles instead of double bonds inside aromatic rings"))

    parser.append(
        op.BoolOption(
            "fancy-bonds",
            "f",
            key="fancy_bonds",
            default=False,
            help_text="Draw fancier double and triple bonds"))

    parser.append(
        op.StringOption(
            "markers",
            "g",
            help_text="""Give each atom and each bond a unique
                        marker that can be used for attaching
                        electron movement arrows.
                        With value 'a', atom 2 will be labeled
                        @{a2}, and its bond to atom 5 @{a2-5}."""))

    parser.append(
        op.BoolOption(
                    "atom-numbers",
                    "n",
                    key="atom_numbers",
                    default=False,
                    help_text="""Show the molfile number of each atom next to it.
                                When this option is set, charges and implicit
                                hydrogens will not be shown"""))

    parser.append(
        op.SelectOption(
            "bond-scale",
            "s",
            key="bond_scale",
            # default="normalize",
            valid_range="normalize keep scale".split(),
            help_text="""How to scale the lengths of bonds
                        (one of 'keep', 'scale', or 'normalize')"""))

    parser.append(
        op.FloatOption(
            "bond-stretch",
            "t",
            key="bond_stretch",
            default=1.0,
            help_text="""Used as scaling factor (with --bond-scale=scale)
                        or average (with --bond-scale=normalize) for bond
                        lengths"""))

    parser.append(
        op.BoolOption(
            "wrap-chemfig",
            "w",
            key="chemfig_command",
            help_text=r"Wrap generated code into \chemfig{...} command"))

    parser.append(
        op.StringOption(
            "submol-name",
            "l",
            key="submol_name",
            help_text=r"""If a name is given, wrap generated code into
                          chemfig \definesubmol{name}{...} command"""))

    parser.append(
        op.IntOption(
            "entry-atom",
            "e",
            key="entry_atom",
            default=None,
            help_text="""Number of first atom to be rendered. Relevant only
                         if generated code is to be used as sub-molecule"""))

    parser.append(
        op.IntOption(
            "exit-atom",
            "x",
            key="exit_atom",
            default=None,
            help_text="""Number of last atom to be rendered. Relevant only
                        if generated code is to be used as sub-molecule"""))

    parser.append(
        op.RangeOption(
            "cross-bond",
            "k",
            key="cross_bond",
            default=None,
            help_text="""Specify bonds that should be drawn on top of others
                         they cross over. Give the start and the end atoms.
                         Example for one bond: --cross-bond=5-6
                         Example for two bonds: --crossbond=4-8,12-13"""))

    return parser


if __name__ == '__main__':
    parser = getParser()
    print(parser.format_help(indent=32, linewidth=80, separator=''))
    print()
    shorts, longs = parser.format_for_getopt()
    print(longs)
    print(shorts)

    # list unused option letters
    from string import ascii_lowercase as letters
    print("unused short options:", ','.join(set(letters) - set(shorts)))

    #print
    #tags = parser.form_tags()
    #print tags
    #for tag in tags:
        #print tag
        #print