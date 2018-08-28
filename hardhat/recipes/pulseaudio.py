from .base import GnuRecipe


class PulseAudioRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PulseAudioRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '809668ffc296043779c984f53461c2b3' \
                      '987a45b7a25eb2f0a1d11d9f23ba4055'
        self.name = 'pulseaudio'
        self.version = '12.2'
        self.depends = ['gdbm', 'intltool', 'json-c', 'libsndfile']
        self.url = 'http://freedesktop.org/software/pulseaudio/releases/' \
                   'pulseaudio-$version.tar.xz'
        self.configure_strip_cross_compile()
        self.configure_args += [
            '--disable-bluez4',
            '--disable-bluez5',
            '--disable-rpath',
            '--without-caps',
            '--disable-tests',
            '--disable-default-build-tests',
            '--with-sysroot=%s' % self.prefix_dir,
            '--with-udev-rules-dir=%s/udev/rules.d' % self.prefix_dir]
        self.environment['CFLAGS'] += ' -fno-strict-aliasing'
        # This may not be required. it was an attempted fix that didn't work
        self.environment['LDFLAGS'] += ' -L%s/src/.libs' % self.directory

