from .base import GnuRecipe


class ClispRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ClispRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8132ff353afaa70e6b19367a25ae3d5a' \
                      '43627279c25647c220641fed00f8e890'

        self.name = 'clisp'
        self.version = '2.49'
        self.depends = ['libsigsegv']
        self.url = 'http://downloads.sourceforge.net/project/clisp/' \
                   'clisp/$version/clisp-$version.tar.bz2'
        self.configure_args += ['--cbc']
        self.configure_strip_cross_compile()
        # If not set CLISP src/makemake generates a makefile with
        # LIBS=... -R... and gcc cannot evaluate a -R parameter
        self.environment['LTLIBSIGSEGV'] = '-lsigsegv'
        self.environment['LIBSIGSEGV'] = '-lsigsegv'
        self.environment['LD'] = 'ld'
        self.environment['CC'] = 'gcc'
