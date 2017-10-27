from ..base import Recipe, MakeInstall


class NpmBaseRecipe(MakeInstall, Recipe):
    def __init__(self, *args, **kwargs):
        super(NpmBaseRecipe, self).__init__(*args, **kwargs)
        self.depends = ['nodejs']
        self.directory = '/tmp'

    def init(self):
        super(NpmBaseRecipe, self).init()

        self.install_args = ['npm', 'install', '-g',
                             '%s@%s' % (self.name, self.version)]
