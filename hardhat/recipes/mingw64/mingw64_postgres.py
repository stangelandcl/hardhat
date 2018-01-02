import os
import shutil
from .base import Mingw64BaseRecipe


class Extra:
    def __init__(self, name):
        self.name = name


class Mingw64PostgresRecipe(Mingw64BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64PostgresRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3ccb4e25fe7a7ea6308dea103cac2029' \
                      '63e6b746697366d72ec2900449a5e713'
        self.name = 'mingw64-postgres'
        self.version = '10.1'
        self.url = 'https://ftp.postgresql.org/pub/source/' \
                   'v$version/postgresql-$version.tar.bz2'
        self.depends = ['mingw64-openssl', 'mingw64-zlib']
        self.configure_args += [
            '--without-icu',
            '--without-ldap',
            '--with-openssl',
            '--without-python',
            '--without-readline',
            '--without-zlib',
            '--without-perl',
            '--enable-nls',
            '--enable-thread-safety']
        self.install_args = ['make', 'install']
#        self.environment['LIBS'] = '-lrt -lncursesw'  # for libreadline

    def need_configure(self):
        return True

    def extract(self):
        super(Mingw64BaseRecipe, self).extract()
        self.directory = os.path.join(self.directory, 'src/interfaces/libpq')
