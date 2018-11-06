import os
import sys
from .base import GnuRecipe
from ..util import patch


class SplintRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SplintRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c78db643df663313e3fa9d5651183918' \
                      '25dd937617819c6efc7966cdf444fb0a'
        self.name = 'splint'
        self.version = '3.1.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://www.splint.org/download.html'
        self.depends = ['autotools', 'bison', 'flex']
        self.url = 'http://www.splint.org/downloads/splint-$version.src.tgz'
        self.environment_strip_lto()
        self.configure_strip_cross_compile()
        self.configure_args += ['ac_cv_lib_fl_yywrap=yes',
                                'INSTALL="%s/bin/install -p"' % self.prefix_dir]
        self.environment['AUTOMAKE'] = 'automake'
        self.compile_args = ['make', '-j1']

    def patch(self):
        file = os.path.join(self.directory, 'src', 'signature.y')
        src = '%pure_parser'
        dst = '%pure-parser'
        patch(file, src, dst)

        file = os.path.join(self.directory, 'src', 'Makefile.am')
        src = '$(RM) signature.tab.c'
        dst = '$(RM) -f signature.tab.c'
        patch(file, src, dst)

        file = os.path.join(self.directory, 'configure.ac')
        src = 'AM_INIT_AUTOMAKE(AC_PACKAGE_TARNAME, AC_PACKAGE_VERSION, AC_PACKAGE_BUGREPORT)'
        dst = 'AM_INIT_AUTOMAKE'
        patch(file, src, dst)

        file = os.path.join(self.directory, 'test', 'Makefile.am')
        src = 'sizesigns.expect \\'
        dst = ''
        patch(file, src, dst)

        self.run_exe(['autoreconf', '-i'], self.directory, self.environment)
        file = os.path.join(self.directory, 'lib', 'Makefile.in')
        src = '\t  $(INSTALL_DATA) $$files "$(DESTDIR)$(splintlibdir)" || exit $$?; \\\n'
        dst = '\t  cp -t $(DESTDIR)$(splintlibdir) $$files || exit $$?; \\\n'
        patch(file, src, dst)

#        sys.exit(1)
