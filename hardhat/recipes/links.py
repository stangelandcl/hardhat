import os
from .base import GnuRecipe


class LinksRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LinksRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f70d0678ef1c5550953bdc27b12e72d5' \
                      'de86e53b05dd59b0fc7f07c507f244b8'

        self.name = 'links'
        self.version = '2.14'
        self.depends = [
            'libjpeg-turbo',
            'libpng',
            'librsvg',
            'libtiff',
            'openssl',
            'xorg-libs']
        self.url = 'http://links.twibright.com/download/links-$version.tar.bz2'
        self.configure_args += ['--enable-graphics']
