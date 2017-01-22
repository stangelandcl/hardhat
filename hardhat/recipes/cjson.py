from .base import GnuRecipe


class CJsonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CJsonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'df549298ea6515058648eaacc62bcc4f' \
                      '82fa34f8b93af7753e30eb35c3841c7d'

        self.name = 'cJSON'
        self.version = '1.2.0'
        self.url = 'https://github.com/DaveGamble/cJSON/archive/' \
                   'v$version.tar.gz'
        self.compile_args += ['PREFIX=%s' % self.prefix_dir]
        self.install_args += ['install', 'PREFIX=%s' % self.prefix_dir]

    def configure(self):
        pass
