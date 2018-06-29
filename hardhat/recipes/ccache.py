import os
from .base import GnuRecipe


class CCacheRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CCacheRecipe, self).__init__(*args, **kwargs)

        self.name = 'ccache'
        self.version = '3.4.2'
        self.url = 'https://www.samba.org/ftp/ccache/ccache-$version.tar.xz'

    def install(self):
        super(CCacheRecipe, self).install()

        # set sloppiness for precompiled headers
        conf = r'''
max_size = 5.0G
sloppiness=pch_defines,time_macros
compression = true
compression_level = 1
'''
        dir = os.path.join(self.prefix_dir, '.ccache')
        self.log_dir('install', dir, 'adding ccache.conf')
        if not os.path.exists(dir):
            os.makedirs(dir)

        file = os.path.join(dir, 'ccache.conf')
        with open(file, 'wt') as f:
            f.write(conf)
