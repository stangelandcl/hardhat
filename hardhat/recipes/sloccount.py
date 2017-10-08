from .base import GnuRecipe


class SloccountRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SloccountRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fa7fa2bbf2f627dd2d0fdb958bd8ec45' \
                      '27231254c120a8b4322405d8a4e3d12b'
        self.name = 'sloccount'
        self.version = '2.26'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'perl']
        self.url = 'https://www.dwheeler.com/sloccount/sloccount-$version.tar.gz'
        self.compile_args += ['PREFIX=%s' % self.prefix_dir]
        self.install_args += ['PREFIX=%s' % self.prefix_dir]

    def need_configure(self):
        return False
