from .base import GnuRecipe


class PciUtilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PciUtilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3a99141a9f40528d0a0035665a06dc37' \
                      'ddb1ae341658e51b50a76ecf86235efc'

        self.description = 'contains lspci for inspecting PCI devices'
        self.name = 'pciutils'
        self.version = '3.5.2'
        self.depends = ['automake', 'bison']
        self.url = 'https://www.kernel.org/pub/software/utils/pciutils/' \
                   'pciutils-3.5.2.tar.xz'

        self.compile_args += ['PREFIX=%s' % self.prefix_dir,
                              'SHAREDDIR=%s/share/hwdata' % self.prefix_dir,
                              'SHARED=yes']

        self.install_args += ['PREFIX=%s' % self.prefix_dir,
                              'SHAREDDIR=%s/share/hwdata' % self.prefix_dir,
                              'SHARED=yes',
                              'install-lib']

    def configure(self):
        pass
