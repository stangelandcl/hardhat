from .base import SetupPyRecipe


class DatashaderRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(DatashaderRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9760f29f277f9aaeb3e9988e66f62f8a' \
                      'ddda57bae8a408e3284b0ee967305131'

        self.name = 'datashader'
        self.version = '0.3.2'
        self.pydepends = ['numba', 'numpy']
        self.url = 'https://github.com/bokeh/$name/archive/$version.tar.gz'
