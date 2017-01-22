from .base import X11BaseRecipe


class LibXcompositeRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXcompositeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ede250cd207d8bee4a338265c3007d7a' \
                      '68d5aca791b6ac41af18e9a2aeb34178'

        self.name = 'libXcomposite'
        self.version = '0.4.4'
        self.depends = ['libXfixes']
