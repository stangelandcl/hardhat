from .base import PipBaseRecipe


class ChardetRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(ChardetRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e53e38b3a4afe6d1132de62b7400a4ac' \
                      '363452dc5dfcf8d88e8e0cce663c68aa'

        self.name = 'chardet'
        self.version = '2.3.0'
