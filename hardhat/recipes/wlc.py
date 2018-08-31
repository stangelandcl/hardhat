import os
import shutil
from .base import GnuRecipe
from ..version import extension_regex

class Extra:
    pass

class WlcRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WlcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a7d0e4c17bc657c9395eeb7e3b2ef118' \
                      '7699af9d2c61cf2033bb906bafdfc029'
        self.name = 'wlc'
        self.depends = ['doxygen',
                        'eudev',
                        'libdrm',
                        'libinput',
                        'libxcb',
                        'libxkbcommon',
                        'mesa',
                        'pixman',
                        'wayland',
                        'wayland-protocols',
                        'xcb-util-image',
                        'xcb-util-wm',
                        'xorg-libs']
        self.version = '6542c16652df147523245fc547d2a5ff4088a0cb'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)' \
            + extension_regex
        self.version_url = 'https://github.com/Cloudef/wlc/releases'
        self.url = 'https://github.com/Cloudef/wlc/archive/$version.tar.gz'
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]
        self.chck = Extra()
        self.chck.name = 'chck'
        self.chck.version = '0400fb5e9cf8fd84f7ad5f59822fa2c9d48e1267'
        self.chck.url = 'https://github.com/Cloudef/chck/archive/$version.tar.gz'
        self.chck.sha256 = '6fed7d3b9ae5b2d1827b6a4121209543' \
                           '5419c98f405358faf2daaeaa1a6c403a'

        self.extra_downloads = [self.chck]

    def extract(self):
        super(WlcRecipe, self).extract()
        dir = os.path.join(self.directory, 'lib', 'chck')
        shutil.rmtree(dir)
        self.log_dir('extract', dir, 'extracting %s' % self.chck.filename)
        self.extract_into(self.chck.filename, os.path.dirname(dir))
        self.log_dir('extract', dir, 'moving chck')
        os.rename(os.path.join(os.path.dirname(dir), 'chck-%s' % self.chck.version), dir)
