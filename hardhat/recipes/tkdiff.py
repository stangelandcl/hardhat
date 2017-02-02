from .base import GnuRecipe


class TkDiffRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TkDiffRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '734bb417184c10072eb64e8d27424533' \
                      '8e41b7fdeff661b5ef30e89f3e3aa357'
        self.name = 'tkdiff'
        self.version = '4.2'
        self.depends = ['tcl', 'tk']
        self.url = 'https://downloads.sourceforge.net/project/tkdiff/tkdiff/' \
                   '$version/tkdiff-$version.tar.gz'

        self.install_args = ['cp', 'tkdiff', '%s/bin' % self.prefix_dir]

    def configure(self):
        pass

    def compile(self):
        pass
