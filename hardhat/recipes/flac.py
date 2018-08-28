from .base import GnuRecipe


class FlacRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FlacRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '91cfc3ed61dc40f47f050a109b086106' \
                      '67d73477af6ef36dcad31c31a4a8d53f'
        self.name = 'flac'
        self.depends = ['doxygen', 'libogg', 'yasm']
        self.version = '1.3.2'
        self.url = 'http://downloads.xiph.org/releases/flac/' \
                   'flac-$version.tar.xz'

        self.configure_args += ['--disable-thorough-tests']
        self.environment_strip_lto()
