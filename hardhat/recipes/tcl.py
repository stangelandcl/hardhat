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

        # Leave a copy of TCL in src instead of build because it shouldn't
        # be deleted. expect uses private headers (tclInt.h) from the src/build
        # directory of TCL
        self.extract_dir = os.path.join(self.prefix_dir, 'src',
                                        'tcl-%s' % self.short_version)
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

    def post_install(self):
        super(TclRecipe, self).post_install()
        self.log_dir('post_install', self.directory, 'cleaning build files')
        self.run_exe(['make', 'clean'], self.directory, self.environment)
