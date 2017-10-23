import os
import shutil
from .base import GnuRecipe
from ..urls import Urls

# Emacs 25
# http://diobla.info/blog-archive/modules-tut.html


class EmacsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(EmacsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '253ac5e7075e594549b83fd9ec116a9d' \
                      'c37294d415e2f21f8ee109829307c00b'
        self.name = 'emacs'
        self.version = '25.3'
        self.url = 'http://mirrors.kernel.org/gnu/emacs/emacs-$version.tar.xz'
#        self.url = 'http://git.savannah.gnu.org/cgit/emacs.git/snapshot/' \
#                   'emacs-$version.tar.gz'

        self.depends = ['dejavu-fonts',
                        'fontconfig',
                        'giflib',
#                        'gnome-icon-theme',
                        'gnutls',
#                        'gtk3',
                        'imagemagick',
                        'libjpeg-turbo', 'libpng',
                        'libtiff', 'libxml2',
                        'motif', # for X11
                        'ncurses', 'zlib']

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
        self.configure_args = [['autoreconf', '-iv'],
                               self.configure_args]

    def install(self):
        src = os.path.join(self.directory, 'src', 'emacs-module.h')
        dst = os.path.join(self.prefix_dir, 'include', 'emacs-module.h')

        shutil.copy2(src, dst)

        super(EmacsRecipe, self).install()
