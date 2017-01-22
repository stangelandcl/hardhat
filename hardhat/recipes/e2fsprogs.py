from .base import GnuRecipe


class E2FsProgsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(E2FsProgsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '744ca4e9a8e6c943601b2744d1ae658e' \
                      '5f37d35b5ea5b1dea86985320bd87f37'

        self.name = 'e2fsprogs'
        self.version = '1.43.3'
        self.url = 'https://www.kernel.org/pub/linux/kernel/people/tytso/' \
                   'e2fsprogs/v$version/e2fsprogs-$version.tar.xz'
        self.configure_args += ['--enable-elf-shlibs',
                                '--disable-libblkid',
                                '--disable-libuuid',
                                '--disable-uuidd',
                                '--disable-fsck']
        self.install_args += ['install-libs']
