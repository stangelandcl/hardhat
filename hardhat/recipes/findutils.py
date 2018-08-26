from .base import GnuRecipe
from ..urls import Urls


class FindUtilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FindUtilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ded4c9f73731cd48fec3b6bdaccce896' \
                      '473b6d8e337e9612e16cf1431bb1169d'

        self.name = 'findutils'
        self.version = '4.6.0'
        self.url = Urls.gnu_template(self.name, self.version)

    def patch(self):
        args = [['sed', '-i', "'s/IO_ftrylockfile/IO_EOF_SEEN/'", 'gl/lib/*.c'],
                ['sed', '-i', "'/unistd/a #include <sys/sysmacros.h>'", 'gl/lib/mountlist.c'],
                ['echo', '"#define _IO_IN_BACKUP 0x100"', '>>', 'gl/lib/stdio-impl.h']]
        for arg in args:
            self.run_exe(arg, self.directory, self.environment)
