import os
from hardhat.util import patch
from .base import GnuRecipe


class LibUnwindRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibUnwindRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1de38ffbdc88bd694d10081865871cd2' \
                      'bfbb02ad8ef9e1606aee18d65532b992'

        self.name = 'libunwind'
        self.version = '1.2'
        self.url = 'http://download.savannah.gnu.org/releases/libunwind/' \
                   'libunwind-$version.tar.gz'

    def patch(self):
        filename = os.path.join(self.directory, 'src', 'Makefile.in')
        src = ['libunwind_coredump_la_LIBADD =',
               'libunwind_elf32_la_LIBADD =',
               'libunwind_elf64_la_LIBADD =',
               'libunwind_elfxx_la_LIBADD =']
        for s in src:
            patch(filename, s, s + ' $(LIBLZMA)')

#        filename = os.path.join(self.directory, 'configure')
#        src = '-lzma'
#        dst = '-llzma'
#        patch(filename, src, dst)
