from .base import SetupPyRecipe


class MuRepoRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(MuRepoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '311cc6731798db32c6164e806afeb592' \
                      '7308a31bd86449f3bb419d6d97d916b5'
                
        self.pythons = ['python3']
        self.python = 'python3'
        self.depends = ['git']
        self.name = 'mu-repo'
        self.version = '1.6.0'
        version = self.version.replace('.', '_')
        self.url = 'https://github.com/fabioz/mu-repo/archive/mu_repo_%s.tar.gz' % version


    @property
    def provides(self):
        return ['mu-repo']


