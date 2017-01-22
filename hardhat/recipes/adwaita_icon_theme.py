from .base import GnuRecipe


class AdwaitaIconThemeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AdwaitaIconThemeRecipe, self).__init__(*args, **kwargs)
        self.name = 'adwaita-icon-theme'
        self.version = '3.22.0'
        self.version_regex = r'(?P<version>\d+\.\d+(\.\d+)?)'
        self.version_url = 'http://ftp.gnome.org/pub/gnome/sources/' \
                           'adwaita-icon-theme/'
        self.depends = ['git', 'gtk3', 'librsvg', 'inkscape', '']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/' \
                   'adwaita-icon-theme/%s/' \
                   'adwaita-icon-theme-$version.tar.xz' % self.short_version

    def post_install(self):
        self.run_exe(['gtk-update-icon-cache'],
                     self.directory,
                     self.environment)
        self.run_exe(['gtk-encode-symbolic-svg'],
                     self.directory,
                     self.environment)
