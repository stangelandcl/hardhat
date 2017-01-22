import os
from .base import GnuRecipe


class LibXml2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXml2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '4de9e31f46b44d34871c22f54bfc5439' \
                      '8ef124d6f7cafb1f4a5958fbcd3ba12d'
        self.name = 'libxml2'
        self.version = '2.9.3'
        self.depends = ['icu', 'python2', 'xz', 'zlib']
        self.url = 'ftp://xmlsoft.org/libxml2/libxml2-$version.tar.gz'
#        self.configure_args += ['--without-python']

        self.configure_args += ['--with-history',
                                '--with-icu',
                                '--with-python=%s' %
                                os.path.join(self.prefix_dir, 'bin', 'python2')]
