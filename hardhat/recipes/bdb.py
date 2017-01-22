import os
from .base import GnuRecipe


class BerkeleyDBRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BerkeleyDBRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e0a992d740709892e81f9d93f06daf30' \
                      '5cf73fb81b545afe72478043172c3628'

        self.name = 'bdb'
        self.version = '5.3.28'
        self.url = 'http://download.oracle.com/berkeley-db/db-$version.tar.gz'

        self.configure_args = self.shell_args + [
            '../dist/configure',
            '--build=%s' % (self.build_triplet),
            '--host=%s' % (self.host_triplet),
            '--prefix=%s' % (self.prefix_dir),
            '--enable-compat185',
            '--enable-sql',
            '--enable-cxx',
            '--enable-stl',
            '--enable-dbm',
            '--enable-shared',
            '--enable-static'
            ]

    def extract(self):
        super(BerkeleyDBRecipe, self).extract()

        self.directory = os.path.join(self.directory, 'build_unix')
