from .base import GnuRecipe


class ZeroMQRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ZeroMQRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '04aac57f081ffa3a2ee5ed04887be9e2' \
                      '05df3a7ddade0027460b8042432bdbcf'

        self.name = 'zeromq'
        self.version = '4.1.5'
        version_dash = self.short_version.replace('.', '-')
        self.url = 'https://github.com/zeromq/zeromq%s/releases/' \
                   'download/v$version/zeromq-$version.tar.gz' % version_dash
