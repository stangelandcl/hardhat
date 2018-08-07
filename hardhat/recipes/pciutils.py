from .base import GnuRecipe


class PciUtilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PciUtilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fcc0431cc951c3563f1e4f946d27c8e2' \
                      '161cfd81f25316e6bd783fa6118469e0'
        self.description = 'contains lspci for inspecting PCI devices'
        self.name = 'pciutils'
        self.version = '3.6.1'
        self.depends = ['automake', 'bison']
        self.url = 'https://www.kernel.org/pub/software/utils/pciutils/' \
                   'pciutils-$version.tar.xz'

        self.compile_args += ['PREFIX=%s' % self.prefix_dir,
                              'SHAREDDIR=%s/share/hwdata' % self.prefix_dir,
                              'SHARED=yes']

        self.install_args += ['PREFIX=%s' % self.prefix_dir,
                              'SHAREDDIR=%s/share/hwdata' % self.prefix_dir,
                              'SHARED=yes',
                              'install-lib']

    def configure(self):
        pass
