from .base import GnuRecipe


class Extra:
    pass


class LibPngRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibPngRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4245b684e8fe829ebb76186327bb37ce' \
                      '5a639938b219882b53d64bd3cfc5f239'

        self.name = 'libpng'
        self.version = '1.6.29'
        self.depends = ['zlib']
        self.url = 'http://download.sourceforge.net/$name/' \
                   '$name-$version.tar.xz'

        self.apng = Extra()
        self.apng.name = 'libpng-apng'
        self.apng.version = self.version
        self.apng.url = 'http://downloads.sourceforge.net/libpng-apng/' \
                        'libpng-$version-apng.patch.gz'
        self.apng.sha256 = '06f3c9b23f61a5a16310170d10a29d0b' \
                           'a1a9350e23b8ce90ae870333b513285b'
        self.extra_downloads = [self.apng]

    def patch(self):
        self.log_dir('patch', self.directory, 'provide apng support')
        cmd = 'gzip -cd %s | patch -p1' % self.apng.filename
        self.run_exe(cmd, self.directory, self.environment)
