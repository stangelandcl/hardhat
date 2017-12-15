from .base import PipBaseRecipe


class PythonSlugifyRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PythonSlugifyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e674f0d45eaeb5c47b7d4771319889a3' \
                      '9b15ee87aa62c3b2fcc33cf34e94fc98'
        self.name = 'python-slugify'
        self.version = '1.1.4'  # for python-nvd3
        self.pydepends = ['unidecode']
