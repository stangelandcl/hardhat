import os
import shutil
from .base import GnuRecipe, SourceMixin
from ..urls import Urls

# Emacs 25
# http://diobla.info/blog-archive/modules-tut.html


class EmacsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(EmacsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1cf4fc240cd77c25309d15e18593789c' \
                      '8dbfba5c2b44d8f77c886542300fd32c'
        self.name = 'emacs'
        self.version = '26.1'
        self.url = 'http://mirrors.kernel.org/gnu/emacs/emacs-$version.tar.xz'
#        self.url = 'http://git.savannah.gnu.org/cgit/emacs.git/snapshot/' \
#                   'emacs-$version.tar.gz'

        self.depends = ['autotools',
                        'dejavu-fonts',
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


class EmacsSourceRecipe(SourceMixin, EmacsRecipe):
    def __init__(self, *args, **kwargs):
        super(EmacsSourceRecipe, self).__init__(*args, **kwargs)
