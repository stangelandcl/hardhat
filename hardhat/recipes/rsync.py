from .base import GnuRecipe


class RsyncRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RsyncRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '55cc554efec5fdaad70de921cd5a5eeb' \
                      '6c29a95524c715f3bbf849235b0800c0'
        self.name = 'rsync'
        self.depends = ['zlib']
        self.version = '3.1.3'
        self.url = 'https://www.samba.org/ftp/rsync/src/rsync-$version.tar.gz'
        self.configure_args += ['--without-included-zlib']
