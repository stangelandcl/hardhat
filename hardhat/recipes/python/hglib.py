from .base import PipBaseRecipe


class HgLibRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(HgLibRecipe, self).__init__(*args, **kwargs)

        self.name = 'hglib'
        self.pypi_name = 'python-hglib'
        self.version = '2.2'
        self.sha256 = 'ce678914d6a6b69b340cec8e2f92da72' \
                      '72ea015ef5973cde74d2c5010b8a9015'

