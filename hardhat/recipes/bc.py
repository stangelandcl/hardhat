import os
from .base import GnuRecipe


class BcRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7ee4abbcfac03d8a6e1a8a3440558a3d' \
                      '239d6b858585063e745c760957725ecc'

        self.description = 'Command-line calculator.' \
                           ' Use `bc -l` for floating point.'

        self.name = 'bc'
        self.version = '1.06.95'
        self.depends = ['flex', 'readline', 'texinfo']
        self.url = 'http://alpha.gnu.org/gnu/bc/bc-$version.tar.bz2'

        self.configure_args += ['--with-readline']

    def _patch(self, file, replace):
        with open(file, 'rt') as f:
            text = f.read()
        text = replace(text)
        with open(file, 'wt') as f:
            f.write(text)

    def patch(self):
        # From Linux From Scratch's bc patch - with following header
        # Submitted By: Bruce Dubbs (bdubbs at linuxfromscratch dot org)
        # Date: 2014-04-18
        # Initial Package Version: 1.06.95
        # Origin: Gentoo
        # Description: Fixes memory leaks and an uninitialized variable

        bc = os.path.join(self.directory, 'bc')

        file = os.path.join(bc, 'storage.c')
        self._patch(file, lambda text: text.replace(
            '      f->f_body = (char *) bc_malloc (BC_START_SIZE);',
            '      f->f_void = FALSE;\n'
            '      f->f_body = (char *) bc_malloc (BC_START_SIZE);'))

        file = os.path.join(bc, 'util.c')
        self._patch(file, lambda text: text.replace(
            'if (namekind != FUNCT)',
            ''))

        old = \
"""
				}
				}
			| expression '+' expression
"""

        new = \
"""
				}
				free($2);
				}
			| expression '+' expression
"""

        file = os.path.join(bc, 'bc.y')
        self._patch(file, lambda text: text.replace(old, new))
