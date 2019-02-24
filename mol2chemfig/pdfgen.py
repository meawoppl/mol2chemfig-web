'''
generate a pdf from a parsed mol2chemfig molecule.
return the result in a string.
'''
import os
import subprocess
import tempfile

MOLQ_TEX = 'molecule.tex'
MOLQ_PDF = 'molecule.pdf'

THIS_DIR, _ = os.path.split(os.path.dirname(os.path.abspath(__file__)))

STYLE_FILE_NAME = 'mol2chemfig.sty'
with open(os.path.join(THIS_DIR, STYLE_FILE_NAME)) as f:
    STYLE_FILE_CONTENTS = f.read()


class DirCtx:
    def __init__(self, todir: str):
        self._to = todir

    def __enter__(self):
        self._previous = os.getcwd()
        os.chdir(self._to)

    def __exit__(self, *args):
        os.chdir(self._previous)


def call_latex(source: str, files={}) -> bytes:
    assert source in files

    with tempfile.TemporaryDirectory() as tempdir:
        with DirCtx(tempdir):
            for name, contents in files.items():
                with open(name, "w") as f:
                    f.write(contents)

            latex_call = ("pdflatex" "-interaction=nonstopmode", source)
            try:
                subprocess.check_call(latex_call)
            except subprocess.CalledProcessError as e:
                print("Failed Running Latex: " + latex_call)
                print(e.output)
                raise
            
            target = source.replace(".tex", ".pdf")
            with open(target, 'rb') as f:
                return f.read()


def pdfgen(mol):
    with tempfile.TemporaryDirectory() as tempdir:
        chemfig = mol.render_server()
        width, height = mol.dimensions()

        atomsep = 16

        latex = latex_template.format(
            width=width, height=height, atomsep=atomsep, chemfig=chemfig)

        return call_latex(
            MOLQ_TEX,
            files={STYLE_FILE_NAME: STYLE_FILE_CONTENTS, MOLQ_TEX: latex})


latex_template = r'''
\documentclass{minimal}
\usepackage{xcolor, mol2chemfig}
\usepackage[margin=(margin)spt,papersize={{width}pt, {height}pt}]{geometry}

\usepackage[helvet]{sfmath}
\setcrambond{2.5pt}{0.4pt}{1.0pt}
\setbondoffset{1pt}
\setdoublesep{2pt}
\setatomsep{{atomsep}pt}
\renewcommand{\printatom}[1]{\fontsize{8pt}{10pt}\selectfont{\ensuremath{\mathsf{#1}}}}

\setlength{\parindent}{0pt}
\setlength{\fboxsep}{0pt}
\begin{document}
\vspace*{\fill}
\vspace{-8pt}
\begin{center}
{chemfig}
\end{center}
\vspace*{\fill}
\end{document}
'''
