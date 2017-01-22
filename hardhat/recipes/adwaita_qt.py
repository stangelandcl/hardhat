import os
from .base import GnuRecipe


class AdwaitaQtRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AdwaitaQtRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '48ccf17088afb77e98fe409f4dc6fdcc' \
                      'd035bbdbcb51f0c2f0da00ef204daba0'

        self.name = 'adwaita-qt'
        self.version = '0.4'
        self.depends = ['qt5']
        self.url = 'https://github.com/MartinBriza/adwaita-qt/archive/' \
                   '$version.tar.gz'

        self.configure_args = [
            'cmake',
            '-DCMAKE_INSTALL_PREFIX:PATH=%s' % self.prefix_dir,
#            '-DUSE_QT4=ON',
            '..']

    def configure(self):
        self.directory = os.path.join(self.directory, 'build')
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)
        super(AdwaitaQtRecipe, self).configure()

    def install(self):
        super(AdwaitaQtRecipe, self).install()

        conf = '%s/etc/xdg/Trolltech.conf' % self.prefix_dir
        with open(conf, 'wt') as f:
            f.write("""[Qt]
style=adwaita
""")
