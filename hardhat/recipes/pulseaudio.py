from .base import GnuRecipe


class PulseAudioRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PulseAudioRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c3d3d66b827f18fbe903fe3df647013f' \
                      '09fc1e2191c035be1ee2d82a9e404686'

        self.name = 'pulseaudio'
        self.version = '9.0'
        self.depends = ['intltool', 'json-c', 'libsndfile']
        self.url = 'http://freedesktop.org/software/pulseaudio/releases/' \
                   'pulseaudio-$version.tar.xz'
        self.configure_strip_cross_compile()
        self.configure_args += [
            '--without-caps',
            '--with-sysroot=%s' % self.prefix_dir,
            '--with-udev-rules-dir=%s/udev/rules.d' % self.prefix_dir]
        self.environment['CFLAGS'] += ' -fno-strict-aliasing'
