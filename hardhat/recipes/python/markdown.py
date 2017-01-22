from .base import PipBaseRecipe


class MarkdownRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(MarkdownRecipe, self).__init__(*args, **kwargs)

        self.name = 'markdown'
        self.version = '2.6.6'
        self.sha256 = '9a292bb40d6d29abac8024887bcfc115' \
                      '9d7a32dc1d6f1f6e8d6d8e293666c504'
