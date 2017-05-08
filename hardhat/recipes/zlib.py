import os
from .base import GnuRecipe, hash_file


class ZlibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ZlibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c3e5e9fdd5004dcb542feda5ee4f0ff0' \
                      '744628baf8ed2dd5d66f8ca1197cb1a1'
        self.name = 'zlib'
        self.version = '1.2.11'
        self.url = 'http://zlib.net/zlib-$version.tar.gz'
        self.configure_args = ['./configure',
                               '--prefix=%s' % (self.prefix_dir)]
