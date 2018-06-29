from .base import GnuRecipe


class QemuRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(QemuRecipe, self).__init__(*args, **kwargs)
        self.name = 'qemu'
        self.version = '2.12.0'
        self.depends = ['alsa-lib',
                        'bzip2',
                        'check',
                        'curl',
                        'glib',
                        'gnutls',
                        'gtk2',
                        'gtk3',
                        'libgcrypt',
                        'libssh2',
                        'libusb',
                        'lzo',
                        'mesa',
                        'nettle',
                        'ncurses',
                        'python2',
                        'sdl2',
                        'vte28',
                        'xorg-libs',
                        'yasm']
        self.url = 'http://wiki.qemu.org/download/qemu-$version.tar.bz2'
        self.configure_args += ['--with-sdlabi=2.0',
                                '--with-gtkabi=3.0',
                                '--audio-drv-list=alsa',
                                '--target-list=x86_64-softmmu']
        self.configure_strip_cross_compile()
        self.environment['CPP'] = 'gcc'
        self.environment['AS'] = 'yasm'
