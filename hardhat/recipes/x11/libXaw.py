from .base import X11BaseRecipe


class LibXawRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXawRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '96fc314874fce9979556321d1d6ee00b' \
                      '5baf32fb333b7278853b4983bc3cdbf6'

        self.name = 'libXaw'
        self.version = '1.0.12'
        self.depends = ['libXext', 'libXmu', 'libXpm', 'libXt']
