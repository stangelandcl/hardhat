import os
from .base import GnuRecipe


class Qt5Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Qt5Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '39602cb08f9c96867910c375d783eed0' \
                      '0fc4a244bffaa93b801225d17950fb2b'

        self.name = 'qt5'
# 5.7 and 5.8 at least require openssl 1.0.x not 1.1.x
        self.version = '5.11.1'
        self.depends = ['cacert', 'dbus', 'fontconfig',
                        'glib', 'gst-plugins-base', 'icu',
                        'libjpeg-turbo', 'libmng', 'libpng', 'libtiff',
                        'mesa', 'openssl', 'pkgconfig', 'sqlite3', 'xorg-libs']
        self.url = 'http://download.qt.io/official_releases/qt/%s/$version/' \
                   'single/qt-everywhere-src-$version.tar.xz' \
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
#        self.compile_args = ['make', '-j1']

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

        text = r'''
Submitted By: Ken Moffat <ken at linuxfromscratch dot org>
Date: 2018-08-13
Initial Package Version: 5.11.1
Upstream Status: Unknown
Origin: Fedora
Description: Fixes build with glibc-2.28.

diff -Naur a/qtbase/mkspecs/linux-g++/qplatformdefs.h b/qtbase/mkspecs/linux-g++/qplatformdefs.h
--- a/qtbase/mkspecs/linux-g++/qplatformdefs.h	2018-06-15 08:29:31.000000000 +0100
+++ b/qtbase/mkspecs/linux-g++/qplatformdefs.h	2018-08-13 04:04:57.168980072 +0100
@@ -72,7 +72,9 @@
 #include <sys/time.h>
 #include <sys/shm.h>
 #include <sys/socket.h>
+#if 0
 #include <sys/stat.h>
+#endif
 #include <sys/wait.h>
 #include <netinet/in.h>

diff -Naur a/qtbase/src/corelib/io/qfilesystemengine_unix.cpp b/qtbase/src/corelib/io/qfilesystemengine_unix.cpp
--- a/qtbase/src/corelib/io/qfilesystemengine_unix.cpp	2018-06-15 08:29:31.000000000 +0100
+++ b/qtbase/src/corelib/io/qfilesystemengine_unix.cpp	2018-08-13 04:04:57.168980072 +0100
@@ -50,7 +50,9 @@
 #include <pwd.h>
 #include <stdlib.h> // for realpath()
 #include <sys/types.h>
+#if 0
 #include <sys/stat.h>
+#endif
 #include <unistd.h>
 #include <stdio.h>
 #include <errno.h>
@@ -91,7 +93,9 @@
 #  include <sys/syscall.h>
 #  include <sys/sendfile.h>
 #  include <linux/fs.h>
+#if 0
 #  include <linux/stat.h>
+#endif

 // in case linux/fs.h is too old and doesn't define it:
 #ifndef FICLONE
@@ -105,13 +109,13 @@
 #    undef SYS_renameat2
 #    undef SYS_statx
 #    undef STATX_BASIC_STATS
-#  else
-#    if !QT_CONFIG(renameat2) && defined(SYS_renameat2)
+#  else
+#    if 0 && !QT_CONFIG(renameat2) && defined(SYS_renameat2)
 static int renameat2(int oldfd, const char *oldpath, int newfd, const char *newpath, unsigned flags)
 { return syscall(SYS_renameat2, oldfd, oldpath, newfd, newpath, flags); }
 #    endif

-#    if !QT_CONFIG(statx) && defined(SYS_statx)
+#    if 0 && !QT_CONFIG(statx) && defined(SYS_statx)
 static int statx(int dirfd, const char *pathname, int flag, unsigned mask, struct statx *statxbuf)
 { return syscall(SYS_statx, dirfd, pathname, flag, mask, statxbuf); }
 #    elif !QT_CONFIG(statx) && !defined(SYS_statx)
'''
        self.apply_patch(self.directory, text)
