from ..base import Recipe, MakeInstall


class OpamBaseRecipe(MakeInstall, Recipe):
    def __init__(self, *args, **kwargs):
        super(OpamBaseRecipe, self).__init__(*args, **kwargs)
        self.env_init = ['eval',
                         '`opam config env --root=%s/opam`' % self.prefix_dir,
                         '&&']
        self.directory = self.prefix_dir
        self.environment['CC'] = 'gcc'
        self.environment['CXX'] = 'g++'

    def init(self):
        self.install_args = self.env_init + [
            'opam',
            'install',
            '-j%s' % self.cpu_count,
            '--yes',
            '%s.%s' % (self.name, self.version)]

    def install(self):
        self.log_dir('install', self.directory, 'installing')
        super(OpamBaseRecipe, self).install()
