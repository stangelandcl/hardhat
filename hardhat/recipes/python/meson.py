from .base import SetupPyRecipe


class MesonRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(MesonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c513eca90e0d70bf14cd1eaafea2fa91' \
                      'cf40a73326a7ff61f08a005048057340'
                
        self.pythons = ['python3']
        self.python = 'python3'
        self.name = 'meson'
        self.version = '0.43.0'
        self.url = 'https://github.com/mesonbuild/meson/releases/download/' \
                   '$version/meson-$version.tar.gz'
                                
    @property
    def provides(self):
        return ['meson']
