from .base import PipBaseRecipe


class Jinja2Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Jinja2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '2333eae399fb538f934d661f7debab8a' \
                      '9736002c343c8e95c56f1e413076c0ce'

        self.name = 'jinja2'
        self.version = '2.9.2'
        self.pypi_name = 'Jinja2'
        self.depends = ['python-markupsafe']
