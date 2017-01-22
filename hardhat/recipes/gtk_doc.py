from .base import GnuRecipe


class GtkDocRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GtkDocRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1ea46ed400e6501f975acaafea31479c' \
                      'ea8f32f911dca4dff036f59e6464fd42'

        self.name = 'gtk-doc'
        self.version = '1.25'
        self.depends = ['docbook-xml', 'docbook-xsl', 'itstool', 'libxslt']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/$name/' \
                   '$version/$name-$version.tar.xz'

        self.configure_args += ['--with-xml-catalog=%s/etc/xml/catalog'
                                % self.prefix_dir]
