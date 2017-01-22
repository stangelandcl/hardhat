import os
from .base import GnuRecipe


class TclRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TclRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ce26d5b9c7504fc25d2f10ef0b82b14c' \
                      'f117315445b5afa9e673ed331830fb53'

        self.name = 'tcl'
        self.version = '8.6.5'
        self.url = 'http://downloads.sourceforge.net/tcl/' \
                   '$name$version-src.tar.gz'

        self.configure_args += ['--enable-64bit',
                                '--enable-threads',
                                '--enable-shared']

        self.configure_strip_cross_compile()
        self.environment['LIBS'] += ' -lm'

    @property
    def directory(self):
        d = super(TclRecipe, self).directory
        return os.path.join(d, 'unix')

    def compile(self):
        try:
            super(TclRecipe, self).compile()
        except Exception as e:
            print('ignoring compile error: %s' % e)
