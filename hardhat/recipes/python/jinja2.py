from .base import PipBaseRecipe


class Jinja2Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Jinja2Recipe, self).__init__(*args, **kwargs)
        self.name = 'jinja2'
        self.version = '2.9.6'
        self.pypi_name = 'Jinja2'
        self.depends = ['python-markupsafe']
