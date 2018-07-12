from .base import PipBaseRecipe


class SphinxRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SphinxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd45480a229edf70d84ca9fae3784162b' \
                      '1bc75ee47e480ffe04a4b7f21a95d76d'
        self.name = 'sphinx'
        self.version = '1.7.5'
        self.pypi_name = 'Sphinx'
        self.pydepends = ['alabaster',
                          'babel',
                          'docutils',
                          'imagesize',
                          'jinja2',
                          'packaging',
                          'pygments',
                          'requests',
                          'setuptools',
                          'six',
                          'snowballstemmer',
                          'sphinxcontrib-websupport']
