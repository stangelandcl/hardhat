from .base import PipBaseRecipe


class TestPathRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(TestPathRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f16b2cb3b03e1ada4fb0200b265a4446' \
                      'f92f3ba4b9d88ace34f51c54ab6d294e'

        self.name = 'testpath'
        self.version = '0.3'
