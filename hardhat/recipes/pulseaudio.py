from .base import GnuRecipe


class PulseAudioRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PulseAudioRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6e422dbdc9fd11c0cb6af869e5eda73d' \
                      'c24a8be3c14725440edd51ce6b464444'

        self.name = 'pulseaudio'
        self.version = '12.0'
        self.depends = ['gdbm', 'intltool', 'json-c', 'libsndfile']
        self.url = 'http://freedesktop.org/software/pulseaudio/releases/' \
                   'pulseaudio-$version.tar.xz'
        self.configure_strip_cross_compile()
        self.configure_args += [
            '--without-caps',
            '--with-sysroot=%s' % self.prefix_dir,
            '--with-udev-rules-dir=%s/udev/rules.d' % self.prefix_dir]
        self.environment['CFLAGS'] += ' -fno-strict-aliasing'
