from .base import GnuRecipe


class GtkDocRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GtkDocRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '911e29e302252c96128965ee1f4067d5' \
                      '431a88e00ad1023a8bc1d6b922af5715'

        self.name = 'gtk-doc'
        self.version = '1.28'
        self.depends = ['docbook-xml', 'docbook-xsl', 'itstool', 'libxslt',
                        'python2-six']
        self.version_regex = '(?P<version>\d+\.\d+)/'
        self.version_url = 'https://download.gnome.org/sources/gtk-doc/'
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/$name/' \
                   '$version/$name-$version.tar.xz'

        self.configure_args += ['--with-xml-catalog=%s/etc/xml/catalog'
                                % self.prefix_dir,
                                '--with-python=python3']
