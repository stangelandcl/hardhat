import os
import shutil
from .base import GnuRecipe
from ..urls import Urls

# Emacs 25
# http://diobla.info/blog-archive/modules-tut.html


class EmacsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(EmacsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '763344b90db4d40e9fe90c5d14748a9d' \
                      'bd201ce544e2cf0835ab48a0aa4a1c67'

        self.name = 'emacs'
        self.version = '25.1'
        self.url = Urls.gnu_template(self.name, self.version)

        self.depends = ['dejavu-fonts',
                        'fontconfig',
                        'giflib',
#                        'gnome-icon-theme',
                        'gnutls',
#                        'gtk3',
                        'imagemagick',
                        'libjpeg-turbo', 'libpng',
                        'libtiff', 'libxml2', 'ncurses', 'zlib']

        env = self.environment
        env['OPT'] = \
            '-O2 -falign-functions=1 -falign-jumps=1 -falign-loops=1'
        env['CFLAGS'] = env['CFLAGS_NO_OPT'] + ' ' + env['OPT']
        env['CXXFLAGS'] = env['CFLAGS']
        env['CPPFLAGS'] = env['CFLAGS']
#        env['CFLAGS'] = ' -O0 -g -ggdb3'
#        env['CXXFLAGS'] = ' -O0 -g -ggdb3'
#        env['CPPFLAGS'] = ' -DDEBUG'

        env['LD_OPT'] = ''
        env['LDFLAGS'] = env['LDFLAGS_NO_OPT']

        self.configure_args += ['--without-makeinfo',
                                '--with-modules',
                                '--with-x-toolkit=lucid',
#                                '--with-xwidgets'
#                                '--without-x',
#                                '--enable-link-time-optimization'
#                                '--enable-checking',
#                                '--enable-asserts'
                                ]

    def install(self):
        src = os.path.join(self.directory, 'src', 'emacs-module.h')
        dst = os.path.join(self.prefix_dir, 'include', 'emacs-module.h')

        shutil.copy2(src, dst)

        super(EmacsRecipe, self).install()
