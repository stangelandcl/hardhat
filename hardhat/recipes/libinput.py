from .base import GnuRecipe


class LibInputRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibInputRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f31191d96e425b4f16319842279d6594' \
                      '6d9d983dcd3d9e466ae1206aa10ecb06'
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
