import os
from .base import GnuRecipe


class CCacheRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CCacheRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3b02a745da1cfa9eb438af7147e0fd35' \
                      '45e2f6163de9e5b07da86f58859f04ec'

        self.name = 'ccache'
        self.version = '3.3.3'
        self.url = 'https://www.samba.org/ftp/ccache/ccache-$version.tar.xz'

    def install(self):
        super(CCacheRecipe, self).install()

        # set sloppiness for precompiled headers
        conf = r'''
max_size = 5.0G
sloppiness=pch_defines,time_macros
'''
        dir = os.path.join(self.prefix_dir, '.ccache')
        self.log_dir('install', dir, 'adding ccache.conf')
        if not os.path.exists(dir):
            os.makedirs(dir)

        file = os.path.join(dir, 'ccache.conf')
        with open(file, 'wt') as f:
            f.write(conf)
