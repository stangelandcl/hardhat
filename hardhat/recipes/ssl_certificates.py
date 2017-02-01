import os
import shutil
from .base import Recipe, TarballRecipe, Extractor
from ..util import make_executable, patch


class Extra:
    pass


class SSLCertificatesRecipe(TarballRecipe, Recipe):
    def __init__(self, *args, **kwargs):
        super(SSLCertificatesRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8e35348f5f96108116a92f5c5755991c' \
                      '7da66e30bddcb4112dc3ddda851c6b2a'

        self.name = 'ssl-certificates'
        self.version = '20170119'
        self.depends = ['openssl']
        self.url = 'http://anduin.linuxfromscratch.org/BLFS/other/' \
                   'make-ca.sh-$version'
        self.directory = os.path.join(self.base_extract_dir,
                                      'ssl-certificates-%s' % self.version)
        self.certdata = Extra()
        self.certdata.url = 'http://anduin.linuxfromscratch.org/BLFS/other/' \
                            'certdata.txt'
        self.certdata.name = 'certdata'
        self.certdata.version = '20161024'
        self.certdata.sha256 = '8c0fd6fb9c71cee859dfe7cca660a5c9' \
                               'dc6a573e2be345ecfa9191605d9d6ad2'

        self.extra_downloads = [self.certdata]
        self.verify_ssl_certificate = False

    def extract(self):
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.makedirs(self.directory)
        self.script = os.path.join(self.directory,
                                   os.path.basename(self.filename))
        shutil.copy2(self.filename, self.script)

    def patch(self):
        self.log_dir('patch', self.directory, 'add prefix to script paths')
        src = 'PKIDIR="/etc/pki"'
        dst = 'PKIDIR="%s/etc/pki"' % self.prefix_dir
        patch(self.script, src, dst)

        src = 'SSLDIR="/etc/ssl"'
        dst = 'SSLDIR="%s/etc/ssl"' % self.prefix_dir
        patch(self.script, src, dst)

        src = 'CERTUTIL="/usr/bin/certutil"'
        dst = 'CERTUTIL="%s/bin/certutil"' % self.prefix_dir
        patch(self.script, src, dst)

        src = 'KEYTOOL="/opt/jdk/bin/keytool"'
        dst = 'KEYTOOL="%s/jdk/bin/keytool"' % self.prefix_dir
        patch(self.script, src, dst)

        src = 'OPENSSL="/usr/bin/openssl"'
        dst = 'OPENSSL="%s/bin/openssl"' % self.prefix_dir
        patch(self.script, src, dst)

        src = '/usr/bin/c_rehash'
        dst = '%s/bin/c_rehash' % self.prefix_dir
        patch(self.script, src, dst)

    def configure(self):
        self.log_dir('configure', self.directory, 'making script executable')
        make_executable(self.script)

        f = os.path.join(self.directory,
                         os.path.basename(self.certdata.filename))
        shutil.copy2(self.certdata.filename, f)

    def install(self):
        self.log_dir('install', self.directory, 'generating ssl certificates')
        args = self.shell_args + [self.script, '-f']
        self.run_exe(args, self.directory, self.environment)
