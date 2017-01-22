from .base import X11BaseRecipe


class LibXxf86vmRecipe(X11BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXxf86vmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'afee27f93c5f31c0ad582852c0fb36d5' \
                      '0e4de7cd585fcf655e278a633d85cd57'

        self.name = 'libXxf86vm'
        self.version = '1.1.4'
        self.depends = ['libX11', 'libXext']
