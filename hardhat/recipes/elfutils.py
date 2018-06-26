import os
from .base import GnuRecipe
from ..util import patch


class ElfUtilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ElfUtilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1f844775576b79bdc9f9c717a50058d0' \
                      '8620323c1e935458223a12f249c9e066'
        self.name = 'elfutils'
        self.version = '0.170'
        self.depends = ['valgrind']
        self.url = 'https://sourceware.org/elfutils/ftp/$version/' \
                   'elfutils-$version.tar.bz2'

        self.environment['CFLAGS'] += ' -Wno-error=maybe-uninitialized' \
            ' -Wno-error=unused-but-set-variable -Wno-error=unused-variable' \
            ' -Wno-error=null-dereference -Wno-error=format-truncation='
        self.environment_strip_lto()

        # From linux from scratch. Avoids conflicts with binutils patches
        self.configure_args += ['--program-prefix="eu-"']

    def patch(self):
        self.log_dir('patch', self.directory, 'patch packed error')
        src = '__attribute__ ((packed, aligned (ALIGN_PRSTATUS)))'
        dst = 'attribute_packed __attribute__ ((aligned (ALIGN_PRSTATUS)))'
        filename = os.path.join(self.directory, 'backends/linux-core-note.c')
        patch(filename, src, dst)
