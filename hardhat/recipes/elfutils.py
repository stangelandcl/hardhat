from .base import GnuRecipe


class ElfUtilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ElfUtilsRecipe, self).__init__(*args, **kwargs)

        self.name = 'elfutils'
        self.version = '0.169'
        self.depends = ['valgrind']
        self.url = 'https://sourceware.org/elfutils/ftp/$version/' \
                   'elfutils-$version.tar.bz2'

        self.environment['CFLAGS'] += ' -Wno-error=maybe-uninitialized' \
            ' -Wno-error=unused-but-set-variable -Wno-error=unused-variable' \
            ' -Wno-error=null-dereference'
        self.environment_strip_lto()

        # From linux from scratch. Avoids conflicts with binutils patches
        self.configure_args += ['--program-prefix="eu-"']
