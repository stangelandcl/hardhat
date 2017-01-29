from .base import GnuRecipe


class Extra:
    pass


class LibPngRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibPngRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '266743a326986c3dbcee9d89b640595f' \
                      '6b16a293fd02b37d8c91348d317b73f9'

        self.name = 'libpng'
        self.version = '1.6.26'
        self.depends = ['zlib']
        self.url = 'http://download.sourceforge.net/$name/' \
                   '$name-$version.tar.xz'

        self.apng = Extra()
        self.apng.name = 'libpng-apng'
        self.apng.version = self.version
        self.apng.url = 'http://downloads.sourceforge.net/libpng-apng/' \
                        'libpng-$version-apng.patch.gz'
        self.apng.sha256 = '01dec904d91ee8c90a9a78f253d01d8f' \
                           'ac0e37a3f4beacb60e136ea7c814d72c'
        self.extra_downloads = [self.apng]

    def patch(self):
        self.log_dir('patch', self.directory, 'provide apng support')
        cmd = 'gzip -cd %s | patch -p1' % self.apng.filename
        self.run_exe(cmd, self.directory, self.environment)
