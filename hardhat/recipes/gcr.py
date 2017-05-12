from .base import GnuRecipe


class GcrRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GcrRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '90572c626d8a708225560c42b4421f79' \
                      '41315247fa1679d4ef569bde7f4bb379'

        self.name = 'gcr'
        self.version = '3.20.0'
        self.depends = ['glib', 'gnupg', 'gobject-introspection',
                        'gtk3', 'gtk-doc', 'libgcript', 'libtasn1', 'libxslt',
                        'p11-kit']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gcr/' \
                   '$short_version/gcr-$version.tar.xz'
        self.configure_args = [
            ['sed', '-i', '-r',
             r"""'s:"(/desktop):"/org/gnome\1:'""", 'schema/*.xml'],
            self.configure_args + [
                '--sysconfdir=%s/etc' % self.prefix_dir,
                '--enable-vala=no']]
