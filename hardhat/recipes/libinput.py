from .base import GnuRecipe


class LibInputRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibInputRecipe, self).__init__(*args, **kwargs)
        self.name = 'libinput'
        self.version = '1.11.3'
        self.depends = ['check', 'doxygen', 'dot', 'gtk3',
                        'libevdev', 'meson', 'mtdev', 'ninja']
        # libwacom - not working yet
        self.url = 'http://www.freedesktop.org/software/libinput/' \
                   'libinput-$version.tar.xz'
        self.configure_args = ['meson',
                               '--prefix=%s' % self.prefix_dir,
                               '--buildtype=release',
                               '-Dlibwacom=false',
                               'builddir/']
        self.compile_args = ['ninja',
                             '-C',
                             'builddir/',
                             'install']
        # sudo udevadm hwdb --update
    def install(self):
        pass
