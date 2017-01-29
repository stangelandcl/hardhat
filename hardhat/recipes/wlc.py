import os
import shutil
from .base import GnuRecipe
from ..version import extension_regex

class Extra:
    pass

class WlcRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WlcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6592579153f8d58f9be5a0226b5cca5d' \
                      'b5f944283abb489891817f853ff53a92'
                
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
        self.version = '12ee97835577cbd312678725c8341e71cac0fcbd'
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
        self.chck.version = '0036426a605933d0c05fcab7441f95d61e679349'
        self.chck.url = 'https://github.com/Cloudef/chck/archive/$version.tar.gz'
        self.chck.sha256 = 'f8a29358c72fa1d5e66b422a968e5101' \
                           'be67bc985e46f40410db407057befddb'
        
        self.extra_downloads = [self.chck]

    def extract(self):
        super(WlcRecipe, self).extract()
        dir = os.path.join(self.directory, 'lib', 'chck')
        shutil.rmtree(dir)
        self.log_dir('extract', dir, 'extracting %s' % self.chck.filename)    
        self.extract_into(self.chck.filename, os.path.dirname(dir))
        self.log_dir('extract', dir, 'moving chck')
        os.rename(os.path.join(os.path.dirname(dir), 'chck-%s' % self.chck.version), dir)
