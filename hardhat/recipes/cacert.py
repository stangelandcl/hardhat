import os
import shutil
from .base import Recipe, Downloader
from hardhat.util import save_url


class CACertRecipe(Downloader, Recipe):
    def __init__(self, *args, **kwargs):
        super(CACertRecipe, self).__init__(*args, **kwargs)
        self.name = 'cacert'
        self.version = '1.0'
        self.depends = ['openssl']
        self.sha256 = 'e62a07e61e5870effa81b430e1900778' \
                      '943c228bd7da1259dd6a955ee2262b47'
        self.url = 'http://curl.haxx.se/ca/cacert.pem'
        self.directory = os.path.dirname(self.filename)
        self.verify_ssl_certificate = False

    def clean(self):
        files = [os.path.join(self.prefix_dir, 'ssl', 'ca-bundle.crt'),
                 os.path.join(self.prefix_dir, 'ssl', 'cert.pem')]

        for file in files:
            self.log_dir('clean', 'removing %s' % file)
            if os.path.lexists(file):
                os.remove(file)

    def install(self):
        src = os.path.join(self.directory, 'cacert.pem')

        # Curl
        dst = os.path.join(self.prefix_dir, 'ssl', 'ca-bundle.crt')
        self.log('install', 'copy %s to %s' % (src, dst))
        shutil.copy2(src, dst)
        src = dst

        # Python/OpenSSL
        dst = os.path.join(self.prefix_dir, 'ssl', 'cert.pem')
        self.log('install', 'symlink %s to %s' % (src, dst))
        os.symlink(src, dst)

#        tmpfile = os.path.join(self.tmp_dir, 'ca-bundle.crt.tmp')
#        bundlefile = CACertRecipe.bundle_path(self.prefix_dir)
#        self.log('install', 'download mozilla bundle to %s ' % bundlefile)
#        save_url('https://mkcert.org/generate/', tmpfile)
#        os.rename(tmpfile, bundlefile)

    def post_install(self):
        self.log_dir('post_install', self.prefix_dir, 'c_rehash')
        self.run_exe(['c_rehash'], self.prefix_dir, self.environment)

    @staticmethod
    def bundle_path(prefix_dir):
        return os.path.join(prefix_dir, 'ssl/ca-bundle.crt')

    @staticmethod
    def certs_path(prefix_dir):
        return os.path.join(prefix_dir, 'ssl/certs')
