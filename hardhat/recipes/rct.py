from .base import GnuRecipe


class RctRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RctRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '327360b9bbf9b9a084983567c2db5697' \
                      '7062ee35522a1db4ff730c2c0cb1c8b7'

        self.name = 'rct'
        self.version = '606780ca30e0dd020b3f870293b32d7fbcc9805d'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['cmake']
        self.url = self.github_commit('Andersbakken')
        self.configure_args = [
            'cmake',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '-DCMAKE_EXPORT_COMPILE_COMMANDS=1',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DFORCE_BASH_COMPLETION_INSTALLATION=ON']
