from .base import GnuRecipe


class GMimeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GMimeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e0a170fb264c2ae4cecd852f4e7aaddb'  \
                      '8d58e8f3f0b569ce2d2a4704f55bdf65'

#        self.depends = ['gobject-introspection', 'vala']
        self.name = 'gmime'
        self.version = '2.6.20'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gmime/' \
                   '%s/gmime-$version.tar.xz' % short_version

        self.configure_strip_cross_compile()
        self.configure_args += [
            '--build=%s' % self.target_triplet,
            '--host=%s' % self.target_triplet,
            '--disable-vala']
