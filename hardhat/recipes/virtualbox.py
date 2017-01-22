from .base import GnuRecipe


class VirtualBoxRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(VirtualBoxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9134b04ca21ca23534e2300aab5ab7ff' \
                      '60d21b56bfd2e21504316bfee73afa87'

        self.name = 'virtualbox'
        self.depends = ['openwatcom']
        self.version = '5.0.24'
        self.url = 'http://download.virtualbox.org/virtualbox/$version/' \
                   'VirtualBox-$version.tar.bz2'
        self.configure_args = self.shell_args + [
            './configure',
            '--out-path=%s' % self.prefix_dir
            ]
