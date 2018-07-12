from .base import PipBaseRecipe


class CChardetRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(CChardetRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9c9269208b9f8d7446dbd970f6544ce4' \
                      '8104096efab0f769ee5918066ba1ee7e'

        self.name = 'cchardet'
        self.version = '2.1.1'
