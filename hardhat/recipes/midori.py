from .base import GnuRecipe


class MidoriRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MidoriRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '424d3177599abbc1eb1a1ad7928dd280' \
                      'a62006e992f2fada2e059375a9609a77'

        self.name = 'midori'
        self.version = '0.5.11'
        self.depends = ['cmake', 'gcr', 'gtk3',
                        'libnotify', 'librsvg',
                        'webkitgtk', 'vala']
        self.url = 'http://www.midori-browser.org/downloads/' \
                   'midori_$version_all_.tar.bz2'
        self.configure_args = [
            'cmake',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '-DCMAKE_BUILD_TYPE=Release',
            '-DUSE_ZEITGEIST=OFF',
            '-DHALF_BRO_INCOM_WEBKIT2=ON',
            '-DUSE_GTK3=1',
            '-DCMAKE_INSTALL_DOCDIR=%s/share/doc/midori' % self.prefix_dir]
