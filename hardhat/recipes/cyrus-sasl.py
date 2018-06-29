from .base import GnuRecipe
from ..urls import Urls


class CyrusSaslRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CyrusSaslRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8d95201b4f2c2ec4c0ebafd01c00d7d1' \
                      'e0f2513352b3f850ae2723a90c6c6789'

        self.name = 'cyrus-sasl'
        self.depends = ['autotools', 'openssl']
        self.version = '2.1.27-rc8'
        self.version_regex = \
            'cyrus-sasl-(?P<version>\d+\.\d+\.\d+-rc\d+)\.tar\.gz'
        self.url = 'https://www.cyrusimap.org/releases/cyrus-sasl-$version.tar.gz'
        self.environment['CFLAGS'] += \
            ' -Wno-unused-const-variable -Wno-pointer-sign'
        self.configure_args +=[
            '--with-sysroot=%s' % self.prefix_dir,
            '--with-plugindir=%s/lib/sasl2' % self.prefix_dir,
            '--with-configdir=%s/lib/sasl2' % self.prefix_dir,
            '--enable-static',
            '--enable-shared']
