from .base import PipBaseRecipe


class SixRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SixRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '70e8a77beed4562e7f14fe23a786b54f' \
                      '6296e34344c23bc42f07b15018ff98e9'
        self.name = 'six'
        self.version = '1.11.0'
