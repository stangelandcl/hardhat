from .base import GnuRecipe


class LibEventRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibEventRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '71c2c49f0adadacfdbe6332a372c38cf' \
                      '9c8b7895bb73dabeaa53cdcc1d4e1fa3'

        self.name = 'libevent'
        self.version = '2.0.22'
        self.depends = ['openssl']
        self.url = 'http://downloads.sourceforge.net/levent/' \
                   'libevent-$version-stable.tar.gz'
