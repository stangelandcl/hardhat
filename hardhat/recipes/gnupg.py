import os
from .base import GnuRecipe


class GnupgRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GnupgRecipe, self).__init__(*args, **kwargs)
        self.name = 'gnupg'
        self.version = '2.2.8'
        self.depends = ['gcrypt', 'libassuan', 'libksba', 'npth']
        self.url = 'https://www.gnupg.org/ftp/gcrypt/gnupg/' \
                   'gnupg-$version.tar.bz2'
        self.configure_strip_cross_compile()
        self.environment['CFLAGS'] += ' -Wno-return-type'
        self.environment['CPPFLAGS'] = \
            self.environment['CPPFLAGS'].replace('-DNDEBUG', '')

    def install(self):
        super(GnupgRecipe, self).install()
        bin = os.path.join(self.prefix_dir, 'bin')
        src = os.path.join(bin, 'gpg2')
        dst = os.path.join(bin, 'gpg')
        if os.path.exists(dst):
            os.remove(dst)
        os.symlink(src, dst)
