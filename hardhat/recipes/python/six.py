from .base import PipBaseRecipe


class SixRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(SixRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '105f8d68616f8248e24bf0e9372ef04d' \
                      '3cc10104f1980f54d57b2ce73a5ad56a'
        self.name = 'six'
        self.version = '1.10.0'
