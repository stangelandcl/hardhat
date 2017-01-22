from .base import PipBaseRecipe


class CsvSortRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CsvSortRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '83945dc610af41473b6ffa3dfe85eb43' \
                      'fb4c418ad383ca5a8bf651eb590ae321'

        self.name = 'csvsort'
        self.version = '1.3'
