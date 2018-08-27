from .base import GnuRecipe


class CorkscrewRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CorkscrewRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ba28a7d123fe607b87ff9d399b33e754' \
                      '9d9ef1a13ae3b61e8f61982e8ae5571d'

        self.name = 'corkscrew'
        self.version = 'a94f745b40077172b8fe7d77e2d583b9cf900281'
        self.url = self.github_commit('bryanpkc')
        self.depends = ['autotools']
        self.configure_args = [self.shell_args + ['autoreconf', '--install'],
	                       self.configure_args]

