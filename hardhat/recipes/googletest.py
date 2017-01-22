from .base import GnuRecipe


class GoogleTestRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GoogleTestRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '380e47212f8103402848e8054939ab8f' \
                      'd13f6eeb1c4513a101d3cfbd38de16a6'
        self.name = 'googletest'
        self.version = 'ec44c6c1675c25b9827aacd08c02433cccde7780'
        self.depends = ['cmake']
        self.url = self.github_commit('google')

        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]
