import os
from .base import GnuRecipe


class AdwaitaQtRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AdwaitaQtRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c2c0c71b131d0e3e58ee108570796cf7' \
                      '0b35dccaa64ce17915d4486de5e91513'
        self.name = 'adwaita-qt'
        self.version = '1.0'
        self.depends = ['qt5']
        self.url = 'https://github.com/FedoraQt/adwaita-qt/archive/' \
                   '$version.tar.gz'
        self.version_url = 'https://github.com/FedoraQt/adwaita-qt/releases/'
        self.version_regex = r'''(?P<version>\d+\.\d+)\.tar\.gz'''

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
