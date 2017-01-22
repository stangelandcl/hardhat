from .base import PipBaseRecipe


class SphinxRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SphinxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8e6a77a20b2df950de322fc32f3b5086' \
                      '97d9d654fe984e3cc88f446a5b4c17c5'

        self.name = 'sphinx'
        self.version = '1.5.1'
        self.pypi_name = 'Sphinx'
        self.pydepends = ['alabaster', 'babel', 'docutils', 'imagesize',
                          'jinja2', 'pygments',
                          'requests',
                          'six', 'snowballstemmer']
