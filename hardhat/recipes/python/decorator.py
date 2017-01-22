from .base import PipBaseRecipe


class DecoratorRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DecoratorRecipe, self).__init__(*args, **kwargs)

        self.name = 'decorator'
        self.version = '4.0.9'
        self.sha256 = '90022e83316363788a55352fe39cfbed' \
                      '357aa3a71d90e5f2803a35471de4bba8'
