from .base import PipBaseRecipe


class PandocFiltersRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PandocFiltersRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ec8bcd100d081db092c57f93462b1861' \
                      'bcfa1286ef126f34da5cb1d969538acd'

        self.name = 'pandocfilters'
        self.version = '1.4.1'
