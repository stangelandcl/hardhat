from .base import GnuRecipe


class MonkeyRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MonkeyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9033e49178a6ee351b5e1e761c746418' \
                      '4e00695647f4547257b921a9db5908ee'
        self.name = 'monkey'
        self.version = '464776f485f822b0caf041e6a740944eae8686b0'
        self.url = self.github_commit('monkey')
        self.configure_args = [
            'cmake',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '-DCMAKE_BUILD_TYPE=Release',
            '-DMK_SYSTEM_MALLOC=True',
            '-DMK_PLUGIN_FASTCGI=False',
            '-DCMAKE_VERBOSE_MAKEFILE=ON']

#        self.compile_args = ['make', '-j1']

    def need_configure(self):
        return True
