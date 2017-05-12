from .base import GnuRecipe


class HiColorIconThemeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(HiColorIconThemeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9cc45ac3318c31212ea2d8cb99e64020' \
                      '732393ee7630fa6c1810af5f987033cc'

        self.name = 'hicolor-icon-theme'
        self.version = '0.15'
        self.depends = ['gtk3']
        self.url = 'http://pkgs.fedoraproject.org/repo/pkgs/' \
                   'hicolor-icon-theme/hicolor-icon-theme-$version.tar.xz/' \
                   'md5/6aa2b3993a883d85017c7cc0cfc0fb73/' \
                   'hicolor-icon-theme-$version.tar.xz'

    def post_install(self):
        self.run_exe(['gtk-update-icon-cache',
                      '%s/share/icons/hicolor' % self.prefix_dir],
                     self.directory,
                     self.environment)
