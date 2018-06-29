from .base import GnuRecipe


class LibXsltRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXsltRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2d9123cd4f142905fe2d281a5318ef74' \
                      'a9217bd17501fbc4213460fbf747d01a'

        self.name = 'libxslt'
        self.version = '1.1.32'
        self.depends = ['gcrypt', 'libxml2', 'python2']
        self.version_regex = 'v(?P<version>\d+\.\d+\.\d+)\.tar\.gz'
        self.version_url = 'https://github.com/GNOME/libxslt/releases'
        self.url = 'https://github.com/GNOME/libxslt/archive/v$version.tar.gz'
        self.configure_args = [self.shell_args + ['./autogen.sh'],
                               self.configure_args]
