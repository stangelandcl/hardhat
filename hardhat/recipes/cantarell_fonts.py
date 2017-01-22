from .base import GnuRecipe


class CantarellFontsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CantarellFontsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '14a228aa0b516dfc367b434a850f955a' \
                      '00c57fc549cbb05348e2b150196a737f'
        self.depends = ['fontconfig']
        self.name = 'cantarell-fonts'
        self.version = '0.0.25'
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/cantarell-fonts/' \
                   '0.0/cantarell-fonts-$version.tar.xz'

    def post_install(self):
        self.log_dir('post-install', self.directory, 'fc-cache')
        self.run_exe(['fc-cache'], self.directory, self.environment)
