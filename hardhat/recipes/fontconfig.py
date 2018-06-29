import os
from .base import GnuRecipe
from ..util import patch


class FontConfigRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FontConfigRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '91dde8492155b7f34bb95079e79be92f' \
                      '1df353fcc682c19be90762fd3e12eeb9'

        self.depends = ['freetype']
        self.name = 'fontconfig'
        self.version = '2.13.0'
        self.url = 'http://www.freedesktop.org/software/fontconfig/release/' \
                   'fontconfig-$version.tar.bz2'
        self.configure_args += ['--sysconfdir=%s/etc' % self.prefix_dir,
                                '--localstatedir=%s/var' % self.prefix_dir,
                                '--disable-docs',
                                '--with-default-fonts=%s/share/fonts'
                                % self.prefix_dir
                                ]
    def patch(self):
        file = os.path.join(self.directory, 'src', 'fcobjshash.h')
        os.remove(file)
