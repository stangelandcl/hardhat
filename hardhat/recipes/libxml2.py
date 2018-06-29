import os
from .base import GnuRecipe


class LibXml2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXml2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ff879b0d9142564bfe63df9753df936f' \
                      '05150afdd7bae07261f12d4dad33ba4a'

        self.name = 'libxml2'
        self.version = '2.9.8'
        self.depends = ['icu', 'python2', 'xz', 'zlib']
        self.url = 'https://github.com/GNOME/libxml2/archive/v$version.tar.gz'
        self.version_url = 'https://github.com/GNOME/libxml2/releases/'
        self.version_regex = r'v(?P<version>\d+\.\d+\.\d+)\.tar\.gz'

#        self.configure_args += ['--without-python']

        self.configure_args = [
            self.shell_args + ['autogen.sh'],
            self.configure_args +
            ['--with-history',
             '--with-icu',
             '--with-python=%s' %
            os.path.join(self.prefix_dir, 'bin', 'python2')]]
