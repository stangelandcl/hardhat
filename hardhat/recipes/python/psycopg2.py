from .base import PipBaseRecipe


class Psycopg2Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Psycopg2Recipe, self).__init__(*args, **kwargs)

        self.name = 'psycopg2'
        self.depends = ['postgres']
        self.version = '2.6.1'
        self.sha256 = '6acf9abbbe757ef75dc2ecd9d91ba749' \
                      '547941abaffbe69ff2086a9e37d4904c'
