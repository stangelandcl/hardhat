from .base import GnuRecipe


class DejavuFontsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DejavuFontsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fa9ca4d13871dd122f61258a80d01751' \
                      'd603b4d3ee14095d65453b4e846e17d7'
        self.depends = ['fontconfig']
        self.name = 'dejavu-fonts'
        self.version = '2.37'
        self.url = 'http://sourceforge.net/projects/dejavu/files/dejavu/' \
                   '$version/dejavu-fonts-ttf-$version.tar.bz2'
        self.install_args = [['install', '-v', '-d', '-m755',
                              '%s/share/fonts/dejavu' % self.prefix_dir],
                             ['install', '-v', '-m644', 'ttf/*.ttf',
                              '%s/share/fonts/dejavu' % self.prefix_dir]]

    def configure(self):
        pass

    def compile(self):
        pass

    def post_install(self):
        self.log_dir('post-install', self.directory, 'fc-cache')
        self.run_exe(['fc-cache'], self.directory, self.environment)
