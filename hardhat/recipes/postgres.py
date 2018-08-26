import os
import shutil
from .base import GnuRecipe


class Extra:
    def __init__(self, name):
        self.name = name


class PostgresRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PostgresRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1b60812310bd5756c62d93a9f93de8c2' \
                      '8ea63b0df254f428cd1cf1a4d9020048'

        self.name = 'postgres'
        self.version = '10.4'
        self.url = 'https://ftp.postgresql.org/pub/source/' \
                   'v$version/postgresql-$version.tar.bz2'
        self.depends = ['libxml2', 'openldap', 'openssl', 'python3',
                        'readline', 'zlib']
        self.configure_args += [
            '--with-icu',
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
        self.doc_version = self.version.split('.')[0]
        self.doc.url = 'https://www.postgresql.org/files/documentation/pdf/' \
                       '%s/postgresql-%s-US.pdf' % (self.doc_version,
                                                    self.doc_version)

        self.doc.sha256 = '97b2709e81b0579491950562da112eaf' \
                          '6485b86515002360626f84b7514cedaf'

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
