from .base import GnuRecipe


class Re2cRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Re2cRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cf56e0de3f335f6a22d3e8c06b8b450d' \
                      '858a4e7875ea1b01c9233e084b90cb52'
        self.name = 're2c'
        self.version = '1.0.3'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'http://re2c.org/install/install.html'
        self.url = 'https://github.com/skvadrik/re2c/releases/download/' \
                   '$version/re2c-$version.tar.gz'
