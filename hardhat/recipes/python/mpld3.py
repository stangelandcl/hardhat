from .base import PipBaseRecipe


class Mpld3Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Mpld3Recipe, self).__init__(*args, **kwargs)

        self.name = 'mpld3'
        self.version = '0.2'
        self.pydepends = ['jinja2', 'matplotlib']
        self.sha256 = '6388fec56a683991b8f4b7ddb8b7c8c0' \
                      '6cddb25491a0b503eef9a028ac16fa78'
