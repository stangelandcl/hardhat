from .base import GnuRecipe


class LwanRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LwanRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e0d6f9840070c80c3ef6c0fe90583cfb' \
                      '09a4549260f3f4115becad9872ece1e4'

        self.name = 'lwan'
        self.depends = ['cmake', 'zlib']
        self.version = '171f5fe464f675bfb0924de43508dc07e3927f2c'
        self.url = self.github_commit('lpereira')
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]
