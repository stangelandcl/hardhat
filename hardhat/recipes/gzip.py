from .base import GnuRecipe
from ..urls import Urls


class GzipRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GzipRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ae506144fc198bd8f81f1f4ad19ce63d' \
                      '5a2d65e42333255977cf1dcf1479089a'

        self.name = 'gzip'
        self.version = '1.9'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')

    def patch(self):
        self.log_dir('patch', self.directory, 'patch for glibc 1.28')
        args = [['sed', '-i', "'s/IO_ftrylockfile/IO_EOF_SEEN/'", 'lib/*.c'],
                ['echo', '"#define _IO_IN_BACKUP 0x100"', '>>', 'lib/stdio-impl.h']]

        for arg in args:
            self.run_exe(arg, self.directory, self.environment)
