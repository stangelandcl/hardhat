from .base import PipBaseRecipe


class BabelRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(BabelRecipe, self).__init__(*args, **kwargs)

        self.name = 'babel'
        self.version = '2.3.4'
        self.pypi_name = 'Babel'
        self.depends = ['python-pytz']
        self.sha256 = 'c535c4403802f6eb38173cd4863e419e' \
                      '2274921a01a8aad8a5b497c131c62875'
