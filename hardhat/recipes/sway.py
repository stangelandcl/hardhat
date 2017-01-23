from .base import GnuRecipe
from ..version import extension_regex


class SwayRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SwayRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3d4d18afc849db8704d8da9cb69eb121' \
                      'ea92b27d7fa556acdcc6708f05c84964'
        self.name = 'sway'
        self.depends = ['gdk-pixbuf', 'cairo',
                        'json-c', 'libcap', 'pango',
                        'pcre', 'pkgconfig',
                        'wayland', 'wlc']
        self.version = '0.11'
        self.version_regex = r'(?P<version>\d+\.\d+(-rc\d+)?)' \
            + extension_regex
        self.version_url = 'https://github.com/SirCmpwn/sway/releases'
        self.url = 'https://github.com/SirCmpwn/sway/archive/$version.tar.gz'
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]

    def install(self):
        super(SwayRecipe, self).install()

        self.log_dir('install', self.directory, 'setuid')
        exe = '%s/bin/sway' % self.prefix_dir
        args = ['sudo', 'chown', 'root', exe]
        args = ['sudo', 'chmod', '+s', exe]

