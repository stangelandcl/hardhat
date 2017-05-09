from .base import GnuRecipe


class ElfUtilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ElfUtilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9412fac7b30872b738bc1ed1ebcaed54' \
                      '493c26ef9a67887913498c17b10f3bc2'
        self.name = 'elfutils'
        self.version = '0.169'
        self.depends = ['valgrind']
        self.url = 'https://sourceware.org/elfutils/ftp/$version/' \
                   'elfutils-$version.tar.bz2'

        self.environment['CFLAGS'] += ' -Wno-error=maybe-uninitialized' \
            ' -Wno-error=unused-but-set-variable -Wno-error=unused-variable' \
            ' -Wno-error=null-dereference -Wno-error=format-truncation='
        self.environment_strip_lto()

        # From linux from scratch. Avoids conflicts with binutils patches
        self.configure_args += ['--program-prefix="eu-"']
