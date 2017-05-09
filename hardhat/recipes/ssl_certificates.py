import os
import shutil
from .base import Recipe, TarballRecipe, Extractor
from ..util import make_executable, patch


class Extra:
    pass


class SSLCertificatesRecipe(TarballRecipe, Recipe):
    def __init__(self, *args, **kwargs):
        super(SSLCertificatesRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '99e16c076801d5539f2b11cb972398f2' \
                      '923652bd91e33832134b7faeb707eb02'

        self.name = 'ssl-certificates'
        self.version = '20170425'
        self.depends = ['openssl']
        self.url = 'http://anduin.linuxfromscratch.org/BLFS/other/' \
                   'make-ca.sh-$version'
        self.directory = os.path.join(self.base_extract_dir,
                                      'ssl-certificates-%s' % self.version)
        self.certdata = Extra()
        self.certdata.url = 'http://anduin.linuxfromscratch.org/BLFS/other/' \
                            'certdata.txt'
        self.certdata.name = 'certdata'
        self.certdata.version = '20170508'
        self.certdata.sha256 = None
                               

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
