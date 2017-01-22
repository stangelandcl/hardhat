from .base import GnuRecipe


class DesktopFileUtilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DesktopFileUtilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6c094031bdec46c9f621708f919084e1' \
                      'cb5294e2c5b1e4c883b3e70cb8903385'

        self.name = 'desktop-file-utils'
        self.version = '0.23'
        self.depends = ['emacs', 'glib']
        self.url = 'http://freedesktop.org/software/desktop-file-utils/' \
                   'releases/desktop-file-utils-$version.tar.xz'
