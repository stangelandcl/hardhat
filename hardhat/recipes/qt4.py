import os
from .base import GnuRecipe


class Qt4Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Qt4Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e2882295097e47fe089f8ac741a95fef' \
                      '47e0a73a3f3cdf21b56990638f626ea0'

        self.name = 'qt4'
        self.version = '4.8.7'
        self.depends = ['cacert', 'dbus', 'fontconfig',
                        'glib', 'gst-plugins-base', 'icu',
                        'libjpeg-turbo', 'libmng', 'libpng', 'libtiff',
                        'mesa', 'openssl', 'pkgconfig', 'xorg-libs']
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://download.qt-project.org/official_releases/qt/' \
                   '%s/$version/qt-everywhere-opensource-src-$version.tar.gz' \
                   % (short_version)

        # qt expects a C++ compiler as a linker. Otherwise failure occurs
        self.environment['QMAKE_LINK'] = self.environment['CXX']
        self.environment['QMAKE_LINK_SHLIB'] = self.environment['CXX']
        self.environment['LD'] = self.environment['CXX']

        # No LTO
        self.environment_strip_lto()

        # to fix "warning: libQtCLucene.so.4, needed by ... libQtHelp.so"
        self.environment['LDFLAGS'] += ' -Wl,-rpath-link,%s/lib' \
                                       % (self.directory)

        self.environment['CXXFLAGS'] += ' -std=gnu++98'
        self.environment['CFLAGS'] += ' -std=gnu++98'

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
            '-no-phonon',
            '-no-phonon-backend',
            '-no-webkit',
#            '-no-rpath',
            '-no-openvg',
            '-nomake', 'demos',
            '-nomake', 'examples',
            '-optimized-qmake'
            ]

    def patch(self):
        self.log_dir('patch', self.directory, 'use local X11 directories')
        filename = os.path.join(self.directory, 'mkspecs',
                                'common', 'linux.conf')
        with open(filename, 'rt') as f:
            text = f.read()

        text = text.replace('/usr/X11R6/include',
                            '%s/include' % self.prefix_dir)
        text = text.replace('/usr/X11R6/lib',
                            '%s/lib' % self.prefix_dir)

        with open(filename, 'wt') as f:
            f.write(text)
