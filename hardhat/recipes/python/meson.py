from .base import SetupPyRecipe


class MesonRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(MesonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '92d8afd921751261e36151643464efd3' \
                      '394162f69efbe8cd53e0a66b1cf395eb'
        self.pythons = ['python3']
        self.python = 'python3'
        self.name = 'meson'
        self.version = '0.47.2'
        self.url = 'https://github.com/mesonbuild/meson/releases/download/' \
                   '$version/meson-$version.tar.gz'

    @property
    def provides(self):
        return ['meson']
