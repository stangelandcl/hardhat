from .base import GnuRecipe


class NeonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NeonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'db0bd8cdec329b48f53a6f00199c92d5' \
                      'ba40b0f015b153718d1b15d3d967fbca'
        self.name = 'neon'
        self.version = '0.30.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['openssl']
        self.url = 'https://fossies.org/linux/www/neon-$version.tar.gz'
        self.configure_args += ['--with-ssl']
