from .base import PipBaseRecipe


class SphinxContribWebSupportRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SphinxContribWebSupportRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9de47f375baf1ea07cdb3436ff39d7a9' \
                      'c76042c10a769c52353ec46e4e8fc3b9'

        self.version = '1.1.0'
        self.name = 'sphinxcontrib-websupport'
