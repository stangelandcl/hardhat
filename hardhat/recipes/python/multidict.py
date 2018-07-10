from .base import PipBaseRecipe


class MultiDictRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(MultiDictRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5ba766433c30d703f6b2c17eb0b6826c' \
                      '6f898e5f58d89373e235f07764952314'
        self.name = 'multidict'
        self.version = '4.3.1'
