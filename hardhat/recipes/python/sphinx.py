from .base import PipBaseRecipe


class SphinxRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SphinxRecipe, self).__init__(*args, **kwargs)
        self.name = 'sphinx'
        self.version = '1.5.5'
        self.pypi_name = 'Sphinx'
        self.pydepends = ['alabaster', 'babel', 'docutils', 'imagesize',
                          'jinja2', 'pygments',
                          'requests',
                          'six', 'snowballstemmer']
