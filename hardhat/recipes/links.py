import os
from .base import GnuRecipe


class LinksRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LinksRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '82f03038d5e050a65681b9888762af41' \
                      'c40fd42dec7e59a8d630bfb0ee134a3f'
        self.name = 'links'
        self.version = '2.16'
        self.depends = [
            'libjpeg-turbo',
            'libpng',
            'librsvg',
            'libtiff',
            'openssl',
            'xorg-libs']
        self.url = 'http://links.twibright.com/download/links-$version.tar.bz2'
        self.configure_args += ['--enable-graphics']
