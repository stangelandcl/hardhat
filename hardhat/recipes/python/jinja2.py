from .base import PipBaseRecipe


class Jinja2Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Jinja2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ddaa01a212cd6d641401cb01b605f4a4' \
                      'd9f37bfc93043d7f760ec70fb99ff9ff'

        self.name = 'jinja2'
        self.version = '2.9.6'
        self.pypi_name = 'Jinja2'
        self.depends = ['python-markupsafe']
