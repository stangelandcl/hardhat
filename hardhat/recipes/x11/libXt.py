from .base import X11BaseRecipe


class LibXtRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXtRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '46eeb6be780211fdd98c5109286618f6' \
                      '707712235fdd19df4ce1e6954f349f1a'

        self.name = 'libXt'
        self.version = '1.1.5'
        self.depends = ['libX11', 'libICE', 'libSM']
