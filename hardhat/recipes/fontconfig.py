import os
from .base import GnuRecipe
from ..util import patch


class FontConfigRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FontConfigRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b449a3e10c47e1d1c7a6ec6e2016cca7' \
                      '3d3bd68fbbd4f0ae5cc6b573f7d6c7f3'

        self.depends = ['freetype']
        self.name = 'fontconfig'
        self.version = '2.12.1'
        self.url = 'http://www.freedesktop.org/software/fontconfig/release/' \
                   'fontconfig-$version.tar.bz2'
        self.configure_args += ['--sysconfdir=%s/etc' % self.prefix_dir,
                                '--localstatedir=%s/var' % self.prefix_dir,
                                '--disable-docs',
                                '--with-default-fonts=%s/share/fonts'
                                % self.prefix_dir
                                ]
