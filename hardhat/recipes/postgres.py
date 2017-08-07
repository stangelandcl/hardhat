import os
import shutil
from .base import GnuRecipe


class Extra:
    def __init__(self, name):
        self.name = name


class PostgresRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PostgresRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0187b5184be1c09034e74e44761505e5' \
                      '2357248451b0c854dddec6c231fe50c9'

        self.name = 'postgres'
        self.version = '9.6.2'
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
        self.doc = Extra('postgres-doc')
        self.doc.url = 'https://www.postgresql.org/files/documentation/pdf/' \
                       '%s/postgresql-%s-US.pdf' % (self.short_version,
                                                    self.short_version)
        self.doc.sha256 = '09d5110f81e7a55399fe49d2c7d5ff88' \
                          '94836597c039d209026182e216510d9e'
        self.doc.version = self.version
        self.extra_downloads.append(self.doc)
#        self.environment['LIBS'] = '-lrt -lncursesw'  # for libreadline

    def need_configure(self):
        return True

    def install(self):
        super(PostgresRecipe, self).install()

        dir = os.path.join(self.prefix_dir, 'share', 'doc')
        name = os.path.basename(self.doc.filename)
        filename = os.path.join(dir, name)
        self.log_dir('install', self.directory, 'copy doc to %s' % filename)
        if not os.path.exists(dir):
            os.makedirs(dir)

        shutil.copy(self.doc.filename, filename)
