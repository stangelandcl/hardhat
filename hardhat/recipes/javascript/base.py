from ..base import GnuRecipe


class NpmBaseRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NpmBaseRecipe, self).__init__(*args, **kwargs)
        self.depends = ['nodejs']

    def init(self):
        super(NpmBaseRecipe, self).init()

        self.install_args = ['npm', 'install', '-g',
                             '%s@%s' % (self.name, self.version)]

    def configure_args(self):
        pass

    def compile_args(self):
        pass
