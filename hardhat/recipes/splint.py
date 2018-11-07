import os
import shutil
import sys
from .base import GnuRecipe, SourceMixin
from ..util import patch

class Extra:
    def __init__(self):
        self.name = 'splint-doc'
        self.sha256 = None
        self.version = '3.1.2'


class SplintRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SplintRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c78db643df663313e3fa9d5651183918' \
                      '25dd937617819c6efc7966cdf444fb0a'
        self.name = 'splint'
        self.version = '3.1.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://www.splint.org/download.html'
        self.depends = ['autotools', 'bison', 'flex', 'wget']
        self.url = 'http://www.splint.org/downloads/splint-$version.src.tgz'
        self.environment_strip_lto()
        self.configure_strip_cross_compile()
        self.configure_args += ['ac_cv_lib_fl_yywrap=yes',
                                'INSTALL="%s/bin/install -p"' % self.prefix_dir]
        self.environment['AUTOMAKE'] = 'automake'
        self.compile_args = ['make', '-j1']
        self.doc_url = 'http://www.splint.org/manual/manual.html'

    def download(self):
        self.log_dir('download', self.directory, 'downloading')
        args = ['wget', self.url, '-O', self.filename]
        self.run_exe(args, self.tmp_dir, self.environment)

        self.log_dir('download', self.directory, 'downloading docs')
        self.docfile = os.path.join(os.path.dirname(self.filename),
                                    'splint-manual.html')
        args = ['wget', self.doc_url, '-O', self.docfile]
        self.run_exe(args, self.tmp_dir, self.environment)


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

    def install(self):
        super(SplintRecipe, self).install()

        self.log_dir('install', self.directory, 'installing docs')
        shutil.copy2(self.docfile,
                     os.path.join(self.prefix_dir, 'share', 'doc',
                                  os.path.basename(self.docfile)))

#        sys.exit(1)

class SplintSrcRecipe(SourceMixin, SplintRecipe):
    def __init__(self, *args, **kwargs):
        super(SplintSrcRecipe, self).__init__(*args, **kwargs)
