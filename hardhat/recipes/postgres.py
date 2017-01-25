import os
from .base import GnuRecipe


class PostgresRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PostgresRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e5101e0a49141fc12a7018c6dad59469' \
                      '4d3a3325f5ab71e93e0e51bd94e51fcd'

        self.name = 'postgres'
        self.version = '9.6.1'
        self.url = 'https://ftp.postgresql.org/pub/source/' \
                   'v$version/postgresql-$version.tar.bz2'
        self.depends = ['libxml2', 'openldap', 'openssl', 'python3',
                        'readline', 'zlib']
        self.configure_args += [
            '--with-ldap',
            '--with-openssl',
            '--with-python',
            '--with-readline',
            '--with-zlib',
            '--enable-nls',
            '--enable-thread-safety']
        self.environment['PYTHON'] = os.path.join(self.prefix_dir,
                                                  'bin', 'python3')
        self.compile_args += ['world']
        self.install_args = ['make', 'install-world']
#        self.environment['LIBS'] = '-lrt -lncursesw'  # for libreadline

    def need_configure(self):
        return True