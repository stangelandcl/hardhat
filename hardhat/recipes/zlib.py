import os
from .base import GnuRecipe, hash_file


class ZlibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ZlibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8d7e9f698ce48787b6e1c67e6bff79e4' \
                      '87303e66077e25cb9784ac8835978017'

        self.name = 'zlib'
        self.version = '1.2.10'
        self.url = 'http://zlib.net/zlib-$version.tar.gz'
        self.configure_args = ['./configure',
                               '--prefix=%s' % (self.prefix_dir)]
