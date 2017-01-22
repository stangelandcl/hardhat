from .base import PipBaseRecipe


class QTConsoleRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(QTConsoleRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '25ec7d345528b3e8f3c91be349dd3c69' \
                      '9755f206dc4b6ec668e2e5dd60ea18ef'

        self.name = 'qtconsole'
        self.version = '4.2.1'
