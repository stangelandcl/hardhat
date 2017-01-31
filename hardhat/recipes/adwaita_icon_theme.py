import os
from .base import GnuRecipe


class AdwaitaIconThemeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AdwaitaIconThemeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c18bf6e26087d9819a962c77288b291e' \
                      'fab25d0419b73d909dd771716a45dcb7'

        self.name = 'adwaita-icon-theme'
        self.version = '3.22.0'
        self.version_regex = r'(?P<version>\d+\.\d+(\.\d+)?)'
        self.version_url = 'http://ftp.gnome.org/pub/gnome/sources/' \
                           'adwaita-icon-theme/'
        self.depends = ['git', 'gtk3', 'librsvg']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/' \
                   'adwaita-icon-theme/%s/' \
                   'adwaita-icon-theme-$version.tar.xz' % self.short_version

    def extract_into(self, filename, directory):
        '''Extra into existing directory'''
        args = ['tar', 'xf', filename, '-C',
                directory, '--strip=1']
        self.log_dir('extract', directory,
                     'extract %s' % filename)
        self.run_exe(args, directory, self.environment)


    def extract(self):
        os.makedirs(self.extract_dir)
        self.extract_into(self.filename, self.extract_dir)

    def post_install(self):
        self.run_exe(['gtk-update-icon-cache',
                      '%s/share/icons/Adwaita' % self.prefix_dir],
                     self.directory,
                     self.environment)
