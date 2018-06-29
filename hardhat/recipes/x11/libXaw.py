from .base import X11BaseRecipe


class LibXawRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXawRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8ef8067312571292ccc2bbe94c41109d' \
                      'cf022ea5a4ec71656a83d8cce9edb0cd'
        self.name = 'libXaw'
        self.version = '1.0.13'
        self.depends = ['libXext', 'libXmu', 'libXpm', 'libXt']
