from .base import GnuRecipe
from ..urls import Urls


class CyrusSaslRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CyrusSaslRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4ec6df83bd80ad0b73cce3f409a98699' \
                      '24fde4c2ad2da803e4349727386e2f98'

        self.name = 'cyrus-sasl'
        self.depends = ['autotools', 'openssl']
        self.version = '497c716c5f5f2ad6a1d189615b21b8d2741c3f71'
        self.url = Urls.github_commit('cyrusimap', self.name, self.version)
        self.environment['CFLAGS'] += \
            ' -Wno-unused-const-variable -Wno-pointer-sign'
        self.configure_args = self.shell_args + [
            'autogen.sh',
            '--prefix=%s' % self.prefix_dir,
            '--with-sysroot=%s' % self.prefix_dir,
            '--with-plugindir=%s/lib/sasl2' % self.prefix_dir,
            '--with-configdir=%s/lib/sasl2' % self.prefix_dir]
