import os
from .base import GnuRecipe


class QmakeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(QmakeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e2882295097e47fe089f8ac741a95fef' \
                      '47e0a73a3f3cdf21b56990638f626ea0'

        self.description = 'qmake without all the other assorted qt stuff'
        self.name = 'qmake'
        self.version = '4.8.7'
        short_version = '.'.join(self.version.split('.')[:2])
        self.url = 'http://download.qt-project.org/official_releases/qt/' \
                   '%s/$version/qt-everywhere-opensource-src-$version.tar.gz' \
                   % (short_version)
        self.configure_strip_cross_compile()
        self.configure_args += [
            '-release',
            '-opensource',
            '-confirm-license',
            '-fast',
            '-largefile',
            '-system-proxies',
            '-no-qt3support',
            '-no-multimedia',
            '-no-audio-backend',
            '-no-phonon',
            '-no-phonon-backend',
            '-no-svg',
            '-no-webkit',
            '-no-javascript-jit',
            '-no-script',
            '-no-declarative-debug',
            '-no-gif',
            '-no-libtiff',
            '-no-libpng',
            '-no-libmng',
            '-no-libjpeg',
            '-no-openssl',
            '-make tools',
            '-optimized-qmake',
            '-no-nis',
            '-no-cups',
            '-no-iconv',
            '-no-dbus',
            '-no-gui',

            '-no-opengl',
            '-no-openvg',
            '-no-gtkstyle',
            '-no-sm',
            '-no-xshape',
            '-no-xvideo',
            '-no-xsync',
            '-no-xcursor',
            '-no-xinerama',
            '-no-xfixes',
            '-no-xrandr',
            '-no-xrender',
            '-no-mitshm',
            '-no-fontconfig',
            '-no-xinput',
            '-no-xkb',
            '-no-glib']
        self.install_args = ['make', 'install_mkspecs', 'install_qmake']

    def compile(self):
        pass
