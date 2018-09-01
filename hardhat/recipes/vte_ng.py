from .base import GnuRecipe


class VteNgRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(VteNgRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fb402d5c082b44297d1c0161570950d2' \
                      'a6bde5ec512c0bf700f32076662da6b9'
        self.name = 'vte-ng'
        self.version = '0.52.2.a'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'gdk-pixbuf', 'pango', 'pcre2', 'vala']
        self.version_url = 'https://github.com/thestinger/vte-ng/releases'
        self.url = 'https://github.com/thestinger/vte-ng/archive/$version.tar.gz'
        self.environment['NOCONFIGURE'] = '1'
        self.configure_args = [self.shell_args + ['./autogen.sh'],
                               self.configure_args + ['--enable-vala=no']]
        self.compile_args = ['make', '-j1']
