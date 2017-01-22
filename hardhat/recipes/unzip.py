from .base import GnuRecipe


class UnzipRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(UnzipRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '036d96991646d0449ed0aa952e4fbe21' \
                      'b476ce994abc276e49d30e686708bd37'
        self.name = 'unzip'
        self.version = '60'
        self.url = 'http://downloads.sourceforge.net/infozip/' \
                   'unzip$version.tar.gz'

        self.compile_args = ['make',
                             '-f',
                             'unix/Makefile',
                             'generic']

        self.install_args = ['make',
                             'prefix=%s' % self.prefix_dir,
                             'MANDIR=%s/share/man/man1' % self.prefix_dir,
                             '-f',
                             'unix/Makefile',
                             'install']

    def configure(self):
        pass
