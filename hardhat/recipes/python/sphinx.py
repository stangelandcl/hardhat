from .base import PipBaseRecipe


class SphinxRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SphinxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4064ea6c56feeb268838cb8fbbee507d' \
                      '0c3d5d92fa63a7df935a916b52c9e2f5'

        self.name = 'sphinx'
        self.version = '1.5.5'
        self.pypi_name = 'Sphinx'
        self.pydepends = ['alabaster', 'babel', 'docutils', 'imagesize',
                          'jinja2', 'pygments',
                          'requests',
                          'six', 'snowballstemmer']
