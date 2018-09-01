from .base import GnuRecipe


class QtWebEngineRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(QtWebEngineRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '389d9f42ca393ac11ec8932ce9771766' \
                      'dec91a4c761ffb685cc429c2a760d48c'
        self.name = 'qtwebengine'
        self.version = '5.11.1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'nss', 'qt5']
        self.url = 'https://download.qt.io/archive/qt/%s/$version/' \
                   'submodules/qtwebengine-everywhere-src-$version.tar.xz' \
                   % self.short_version
        self.configure_args = ['qmake']
