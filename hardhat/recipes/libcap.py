import os
from .base import GnuRecipe
from ..util import patch


class LibCapRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibCapRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '693c8ac51e983ee678205571ef272439' \
                      'd83afe62dd8e424ea14ad9790bc35162'

        self.name = 'libcap'
        self.version = '2.25'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/ggreer/the_silver_searcher/' \
                           'releases'
        self.depends = ['autotools', 'pcre', 'pkgconfig', 'xz', 'zlib']
        self.url = 'https://www.kernel.org/pub/linux/libs/security/' \
                   'linux-privs/libcap2/libcap-$version.tar.xz'

        # disable gperf. It generates invalid code
        # it uses size_t without include stdlib.h
        self.compile_args += ['BUILD_GPERF=no']
        self.install_args = ['make',
                             'RAISE_SETFCAP=no',
                             'BUILD_GPERF=no',
                             'lib=lib',
                             'prefix=%s' % self.prefix_dir,
                             'install']

    def configure(self):
        pass
