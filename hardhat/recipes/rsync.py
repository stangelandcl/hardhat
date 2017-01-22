from .base import GnuRecipe


class RsyncRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RsyncRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ecfa62a7fa3c4c18b9eccd8c16eaddee' \
                      '4bd308a76ea50b5c02a5840f09c0a1c2'

        self.name = 'rsync'
        self.depends = ['zlib']
        self.version = '3.1.2'
        self.url = 'https://www.samba.org/ftp/rsync/src/rsync-$version.tar.gz'
        self.configure_args += ['--without-included-zlib']
