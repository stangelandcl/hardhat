from .base import GnuRecipe


class GMimeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GMimeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '75ec6033f9192488ff37745792c107b3' \
                      'd0ab0a36c2d3e4f732901a771755d7e0'
#        self.depends = ['gobject-introspection', 'vala']
        self.name = 'gmime'
        self.version = '3.2.0'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gmime/' \
                   '%s/gmime-$version.tar.xz' % short_version

        self.configure_strip_cross_compile()
        self.configure_args += [
            '--build=%s' % self.target_triplet,
            '--host=%s' % self.target_triplet,
            '--disable-vala']
