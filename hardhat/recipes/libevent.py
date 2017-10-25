from .base import GnuRecipe


class LibEventRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibEventRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '965cc5a8bb46ce4199a47e9b2c9e1cae' \
                      '3b137e8356ffdad6d94d3b9069b71dc2'

        self.name = 'libevent'
        self.version = '2.1.8'
        self.depends = ['openssl']
        self.url = 'https://github.com/libevent/libevent/releases/download/' \
                   'release-$version-stable/libevent-$version-stable.tar.gz'
