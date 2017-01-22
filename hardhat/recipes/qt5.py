import os
from .base import GnuRecipe


class Qt5Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Qt5Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c86684203be61ae7b33a6cf33c23ec37' \
                      '7f246d697bd9fb737d16f0ad798f89b7'

        self.name = 'qt5'
# 5.7 and 5.8 at least require openssl 1.0.x not 1.1.x
        self.version = '5.7.1'
        self.depends = ['cacert', 'dbus', 'fontconfig',
                        'glib', 'gst-plugins-base', 'icu',
                        'libjpeg-turbo', 'libmng', 'libpng', 'libtiff',
                        'mesa', 'openssl', 'pkgconfig', 'sqlite3', 'xorg-libs']
        self.url = 'http://download.qt.io/official_releases/qt/%s/$version/' \
                   'single/qt-everywhere-opensource-src-$version.tar.gz' \
                   % self.short_version

        # qt expects a C++ compiler as a linker. Otherwise failure occurs
        self.environment['QMAKE_LINK'] = self.environment['CXX']
        self.environment['QMAKE_LINK_SHLIB'] = self.environment['CXX']
        self.environment['LD'] = self.environment['CXX']

        # No LTO
        self.environment_strip_lto()

        # to fix "warning: libQtCLucene.so.4, needed by ... libQtHelp.so"
        self.environment['LDFLAGS'] += ' -Wl,-rpath-link,%s/lib' \
                                       % (self.directory)

        self.configure_args = self.shell_args + [
            './configure',
            '-prefix %s' % (self.prefix_dir),
            '-confirm-license',
            '-opensource',
            '-release',
            '-xplatform', 'linux-g++',
            '-dbus-linked',
            '-openssl-linked',
            '-system-sqlite',
#            '-no-phonon',
#            '-no-phonon-backend',
#            '-no-webkit',
#            '-no-rpath',
            '-no-openvg',
#            '-nomake', 'demos',
            '-nomake', 'examples',
            '-optimized-qmake',
            '-no-use-gold-linker',
# missing some xcb libraries. Add them and this can be removed.
            '-qt-xcb'
            ]
#        self.compile_args = ['make']

    def patch(self):
        self.log_dir('patch', self.directory, 'use local X11 directories')
        filename = os.path.join(self.directory,
                                'qtbase', 'mkspecs',
                                'linux-g++-64', 'qmake.conf')
        with open(filename, 'rt') as f:
            text = f.read()

        text = text.replace('/usr/X11R6/include',
                            '%s/include' % self.prefix_dir)
        text = text.replace('/usr/X11R6/lib64',
                            '%s/lib' % self.prefix_dir)
        text = text.replace('/usr/X11R6/lib',
                            '%s/lib' % self.prefix_dir)

        with open(filename, 'wt') as f:
            f.write(text)
