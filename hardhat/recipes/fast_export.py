from .base import GnuRecipe


class FastExportRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FastExportRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '15124825f8f18bbae874f155ea8168d5' \
                      '4775f906d50ca8dc59efc86eeb491615'

        self.name = 'fast-export'
        self.version = 'v170101'
        self.url = 'https://github.com/frej/fast-export/archive/' \
                   '$version.tar.gz'
        self.install_args = ['cp', 'hg*', '%s/bin' % self.prefix_dir]

    def configure(self):
        pass

    def compile(self):
        pass
