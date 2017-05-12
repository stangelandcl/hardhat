import os
from string import Template
from .base import GnuRecipe
from ..util import patch


class FirefoxRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FirefoxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4ed1b23ea7c08f81a08817ddf3b4f068' \
                      '49e01420ee074008b6f390366e95b7d0'
        self.name = 'firefox'
        self.version = '53.0'
        self.version_regex = r'(?P<version>\d+\.\d+(\.\d+)*)'
        self.version_url = 'https://ftp.mozilla.org/pub/mozilla.org/firefox/' \
                           'releases/'
        self.depends = ['alsa-lib',
                        'autoconf',
                        'autoconf2.13',
                        'cargo',
                        'curl',
                        'dbus-glib',
                        'gconf',
                        'graphite2',
                        'gtk2',
#                        'gtk3',
                        'harfbuzz',
                        'hunspell',
                        'icu',
                        'libevent',
                        'libjpeg-turbo',
                        'libpng',
                        'libproxy',
                        'libwebp',
                        'libvpx',
                        'nspr',
                        'nss',
                        'openssl',
                        'python2',
                        'sqlite3',
                        'ssl-certificates',
                        'startup-notification',
                        'unzip',
                        'yasm',
                        'zip',
                        'zlib'
                        ]
        self.url = 'https://ftp.mozilla.org/pub/mozilla.org/firefox/' \
                   'releases/$version/source/firefox-$version.source.tar.xz'

        self.compile_args = ['make', '-f', 'client.mk']
        self.install_args = [
            ['make', '-f', 'client.mk', 'install', 'INSTALL_SDK='],
            ['mkdir', '-pv', '%s/lib/mozilla/plugins' % self.prefix_dir],
            ['ln', '-sfv',
             '../../mozilla/plugins',
             '%s/lib/firefox-%s/browser' % (self.prefix_dir, self.version)]
            ]
        # for cert.h
        self.environment['CPPFLAGS'] += ' -I%s/include/nss' % self.prefix_dir
        self.environment_strip_lto()

    def configure(self):
        pass

    def extract(self):
        super(FirefoxRecipe, self).extract()
        self.directory = os.path.join(self.directory,
                                      '%s-%s' % (self.name, self.version))

    def patch(self):
        mozconfig = Template(r'''
# If you have a multicore machine, all cores will be used by default.
# If desired, you can reduce the number of cores used, e.g. to 1, by
# uncommenting the next line and setting a valid number of CPU cores.
mk_add_options MOZ_MAKE_FLAGS="-j${cpus}"
ac_add_options --target=${target}
ac_add_options --disable-gold

# If you have installed dbus-glib, comment out this line:
#ac_add_options --disable-dbus

# If you have installed dbus-glib, and you have installed (or will install)
# wireless-tools, and you wish to use geolocation web services, comment out
# this line
#ac_add_options --disable-necko-wifi

# Uncomment this option if you wish to build with gtk+-2
ac_add_options --enable-default-toolkit=cairo-gtk2

# Uncomment these lines if you have installed optional dependencies:
ac_add_options --enable-system-hunspell
ac_add_options --enable-startup-notification

# Comment out following option if you have PulseAudio installed
ac_add_options --disable-pulseaudio

# If you have installed GConf, comment out this line
#ac_add_options --disable-gconf

# Comment out following options if you have not installed
# recommended dependencies:
ac_add_options --enable-system-sqlite
ac_add_options --with-system-libevent
ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-icu

# If you are going to apply the patch for system graphite
# and system harfbuzz, uncomment these lines:
ac_add_options --with-system-graphite2
ac_add_options --with-system-harfbuzz

# Stripping is now enabled by default.
# Uncomment these lines if you need to run a debugger:
#ac_add_options --disable-strip
#ac_add_options --disable-install-strip

# The BLFS editors recommend not changing anything below this line:
ac_add_options --prefix=${prefix}
ac_add_options --enable-application=browser

ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --disable-tests

# disable for debugging
#ac_add_options --disable-optimize
#ac_add_options --enable-debug


ac_add_options --enable-gio
ac_add_options --enable-official-branding
ac_add_options --enable-safe-browsing
ac_add_options --enable-url-classifier

# From firefox-40, using system cairo causes firefox to crash
# frequently when it is doing background rendering in a tab.
#ac_add_options --enable-system-cairo
ac_add_options --enable-system-ffi
ac_add_options --enable-system-pixman

ac_add_options --with-pthreads

ac_add_options --with-system-bz2
ac_add_options --with-system-jpeg
ac_add_options --with-system-png
ac_add_options --with-system-zlib

mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/firefox-build-dir
''').substitute(cpus=self.cpu_count,
                prefix=self.prefix_dir,
                target=self.target_triplet)
        file = os.path.join(self.directory, 'mozconfig')
        with open(file, 'wt') as f:
            f.write(mozconfig)

        src = r"cpp = list(buildconfig.substs['CPP'])"
        dst = r"cpp = buildconfig.substs['CPP'].split()"
        file = os.path.join(self.directory, 'dom/bindings/GenerateCSS2PropertiesWebIDL.py')
        patch(file, src, dst)

        file = os.path.join(self.directory, 'layout/style/GenerateCSSPropsGenerated.py')
        patch(file, src, dst)

        # Fix install failure when --enable-debug is specified
        # Only enable this if --enable debug is specified
#        src = r'''#ifdef MOZ_DEBUG'''
#        dst = r'''#ifndef MOZ_DEBUG'''
#        file = os.path.join(self.directory, 'browser/installer/package-manifest.in')
#        patch(file, src, dst)

        system = r'''
Submitted By: Ken Moffat <ken at linuxfromscratch dot org>
Date: 2017-02-08
Initial Package Version: 52.0
Upstream Status: Waiting for review (mozilla bug 847568)
Origin: OpenBSD (via gentoo)
Description: Allow use of system versions of graphite2 and harfbuzz.  This
should be regarded as experimental.  Add the options --with-system-graphite2
and --with-system-harfbuzz to use this (needs recent versions of both).
The source of this latest version is from
https://dev.gentoo.org/~anarchy/mozilla/patchsets/firefox-5r.0-patches-07.tar.xz
where the patch has been separated into graphite and harfbuzz patches.
Previous versions of the patch were at https://dev.gentoo.org/~axs/mozilla/patchsets/

diff -Naur a/config/Makefile.in b/config/Makefile.in
--- a/config/Makefile.in	2016-10-31 20:15:27.000000000 +0000
+++ b/config/Makefile.in	2017-03-07 23:25:43.449654415 +0000
@@ -41,6 +41,8 @@
 	$(PYTHON) -m mozbuild.action.preprocessor $(DEFINES) $(ACDEFINES) \
 		-DMOZ_TREE_CAIRO=$(MOZ_TREE_CAIRO) \
 		-DMOZ_TREE_PIXMAN=$(MOZ_TREE_PIXMAN) \
+		-DMOZ_SYSTEM_GRAPHITE2=$(MOZ_SYSTEM_GRAPHITE2) \
+		-DMOZ_SYSTEM_HARFBUZZ=$(MOZ_SYSTEM_HARFBUZZ) \
 		-DMOZ_SYSTEM_HUNSPELL=$(MOZ_SYSTEM_HUNSPELL) \
 		-DMOZ_SYSTEM_BZ2=$(MOZ_SYSTEM_BZ2) \
 		-DMOZ_SYSTEM_ZLIB=$(MOZ_SYSTEM_ZLIB) \
diff -Naur a/config/system-headers b/config/system-headers
--- a/config/system-headers	2017-02-27 16:10:59.000000000 +0000
+++ b/config/system-headers	2017-03-07 23:25:43.449654415 +0000
@@ -1267,6 +1267,15 @@
 libsn/sn-monitor.h
 libsn/sn-util.h
 #endif
+#if MOZ_SYSTEM_GRAPHITE2==1
+graphite2/Font.h
+graphite2/Segment.h
+#endif
+#if MOZ_SYSTEM_HARFBUZZ==1
+harfbuzz/hb-glib.h
+harfbuzz/hb-ot.h
+harfbuzz/hb.h
+#endif
 #if MOZ_SYSTEM_HUNSPELL==1
 hunspell.hxx
 #endif
diff -Naur a/dom/base/moz.build b/dom/base/moz.build
--- a/dom/base/moz.build	2017-02-27 16:11:01.000000000 +0000
+++ b/dom/base/moz.build	2017-03-07 23:25:37.009713947 +0000
@@ -478,6 +478,9 @@
 if CONFIG['MOZ_X11']:
     CXXFLAGS += CONFIG['TK_CFLAGS']

+if CONFIG['MOZ_SYSTEM_HARFBUZZ']:
+    CXXFLAGS += CONFIG['MOZ_HARFBUZZ_CFLAGS']
+
 GENERATED_FILES += [
     'PropertyUseCounterMap.inc',
     'UseCounterList.h',
diff -Naur a/gfx/graphite2/moz-gr-update.sh b/gfx/graphite2/moz-gr-update.sh
--- a/gfx/graphite2/moz-gr-update.sh	2016-07-25 21:22:05.000000000 +0100
+++ b/gfx/graphite2/moz-gr-update.sh	2017-03-07 23:25:43.449654415 +0000
@@ -1,6 +1,7 @@
 #!/bin/bash

 # Script used to update the Graphite2 library in the mozilla source tree
+# and bump version for --with-system-graphite2

 # This script lives in gfx/graphite2, along with the library source,
 # but must be run from the top level of the mozilla-central tree.
@@ -37,12 +38,16 @@
 #find gfx/graphite2/ -name "*.cpp" -exec perl -p -i -e "s/<cstdio>/<stdio.h>/;s/Windows.h/windows.h/;" {} \;
 #find gfx/graphite2/ -name "*.h" -exec perl -p -i -e "s/<cstdio>/<stdio.h>/;s/Windows.h/windows.h/;" {} \;

+# chase version for --with-system-graphite2
+perl -p -i -e "s/[0-9]+\,[0-9]+\,[0-9]+/$RELEASE/ and tr/./,/ \
+  if /GR2_VERSION_REQUIRE/" old-configure.in
+
 # summarize what's been touched
 echo Updated to $RELEASE.
 echo Here is what changed in the gfx/graphite2 directory:
 echo

-hg stat gfx/graphite2
+hg stat old-configure.in gfx/graphite2

 echo
 echo If gfx/graphite2/src/files.mk has changed, please make corresponding
diff -Naur a/gfx/harfbuzz/README-mozilla b/gfx/harfbuzz/README-mozilla
--- a/gfx/harfbuzz/README-mozilla	2017-02-27 16:10:58.000000000 +0000
+++ b/gfx/harfbuzz/README-mozilla	2017-03-07 23:25:37.009713947 +0000
@@ -19,3 +19,8 @@

 If the collection of source files changes, manual updates to moz.build may be
 needed, as we don't use the upstream makefiles.
+
+The in-tree copy may be omitted during build by --with-system-harfbuzz.
+Make sure to keep pkg-config version check within toolkit/moz.configure in sync
+with checkout version or increment latest tag by one if it's not based
+on upstream release.
diff -Naur a/gfx/moz.build b/gfx/moz.build
--- a/gfx/moz.build	2016-10-31 20:15:31.000000000 +0000
+++ b/gfx/moz.build	2017-03-07 23:25:43.449654415 +0000
@@ -7,6 +7,12 @@
 if CONFIG['MOZ_TREE_CAIRO']:
     DIRS += ['cairo']

+if not CONFIG['MOZ_SYSTEM_GRAPHITE2']:
+    DIRS += ['graphite2/src' ]
+
+if not CONFIG['MOZ_SYSTEM_HARFBUZZ']:
+    DIRS += ['harfbuzz/src']
+
 DIRS += [
     '2d',
     'ycbcr',
@@ -15,8 +21,6 @@
     'qcms',
     'gl',
     'layers',
-    'graphite2/src',
-    'harfbuzz/src',
     'ots/src',
     'thebes',
     'ipc',
diff -Naur a/gfx/skia/generate_mozbuild.py b/gfx/skia/generate_mozbuild.py
--- a/gfx/skia/generate_mozbuild.py	2017-02-27 16:10:59.000000000 +0000
+++ b/gfx/skia/generate_mozbuild.py	2017-03-07 23:25:37.009713947 +0000
@@ -140,6 +140,9 @@
         '-Wno-unused-private-field',
     ]

+if CONFIG['MOZ_SYSTEM_HARFBUZZ']:
+    CXXFLAGS += CONFIG['MOZ_HARFBUZZ_CFLAGS']
+
 if CONFIG['MOZ_WIDGET_TOOLKIT'] in ('gtk2', 'gtk3', 'android'):
     CXXFLAGS += CONFIG['MOZ_CAIRO_CFLAGS']
     CXXFLAGS += CONFIG['CAIRO_FT_CFLAGS']
diff -Naur a/gfx/skia/moz.build b/gfx/skia/moz.build
--- a/gfx/skia/moz.build	2017-02-27 16:10:59.000000000 +0000
+++ b/gfx/skia/moz.build	2017-03-07 23:25:37.009713947 +0000
@@ -750,6 +750,9 @@
         '-Wno-unused-private-field',
     ]

+if CONFIG['MOZ_SYSTEM_HARFBUZZ']:
+    CXXFLAGS += CONFIG['MOZ_HARFBUZZ_CFLAGS']
+
 if CONFIG['MOZ_WIDGET_TOOLKIT'] in ('gtk2', 'gtk3', 'android'):
     CXXFLAGS += CONFIG['MOZ_CAIRO_CFLAGS']
     CXXFLAGS += CONFIG['CAIRO_FT_CFLAGS']
diff -Naur a/gfx/thebes/moz.build b/gfx/thebes/moz.build
--- a/gfx/thebes/moz.build	2017-02-27 16:11:01.000000000 +0000
+++ b/gfx/thebes/moz.build	2017-03-07 23:25:43.449654415 +0000
@@ -266,7 +266,13 @@
 LOCAL_INCLUDES += CONFIG['SKIA_INCLUDES']
 LOCAL_INCLUDES += ['/media/libyuv/include']

-DEFINES['GRAPHITE2_STATIC'] = True
+if CONFIG['MOZ_SYSTEM_GRAPHITE2']:
+    CXXFLAGS += CONFIG['MOZ_GRAPHITE2_CFLAGS']
+else:
+    DEFINES['GRAPHITE2_STATIC'] = True
+
+if CONFIG['MOZ_SYSTEM_HARFBUZZ']:
+    CXXFLAGS += CONFIG['MOZ_HARFBUZZ_CFLAGS']

 if CONFIG['CLANG_CXX']:
     # Suppress warnings from Skia header files.
diff -Naur a/intl/unicharutil/util/moz.build b/intl/unicharutil/util/moz.build
--- a/intl/unicharutil/util/moz.build	2016-10-31 20:15:32.000000000 +0000
+++ b/intl/unicharutil/util/moz.build	2017-03-07 23:25:37.009713947 +0000
@@ -42,4 +42,7 @@
 if CONFIG['ENABLE_INTL_API']:
     USE_LIBS += ['icu']

+if CONFIG['MOZ_SYSTEM_HARFBUZZ']:
+    CXXFLAGS += CONFIG['MOZ_HARFBUZZ_CFLAGS']
+
 DIST_INSTALL = True
diff -Naur a/netwerk/dns/moz.build b/netwerk/dns/moz.build
--- a/netwerk/dns/moz.build	2016-10-31 20:15:27.000000000 +0000
+++ b/netwerk/dns/moz.build	2017-03-07 23:25:37.009713947 +0000
@@ -66,6 +66,9 @@
     '/netwerk/base',
 ]

+if CONFIG['MOZ_SYSTEM_HARFBUZZ']:
+    CXXFLAGS += CONFIG['MOZ_HARFBUZZ_CFLAGS']
+
 if CONFIG['ENABLE_INTL_API']:
     DEFINES['IDNA2008'] = True
     USE_LIBS += ['icu']
diff -Naur a/old-configure.in b/old-configure.in
--- a/old-configure.in	2017-02-27 16:11:06.000000000 +0000
+++ b/old-configure.in	2017-03-07 23:25:43.449654415 +0000
@@ -5023,6 +5023,27 @@
 fi

 dnl ========================================================
+dnl Check for graphite2
+dnl ========================================================
+if test -n "$MOZ_SYSTEM_GRAPHITE2"; then
+    dnl graphite2.pc has bogus version, check manually
+    _SAVE_CFLAGS=$CFLAGS
+    CFLAGS="$CFLAGS $MOZ_GRAPHITE2_CFLAGS"
+    AC_TRY_COMPILE([ #include <graphite2/Font.h>
+                     #define GR2_VERSION_REQUIRE(major,minor,bugfix)  \
+                             ( GR2_VERSION_MAJOR * 10000 + GR2_VERSION_MINOR \
+                               * 100 + GR2_VERSION_BUGFIX >= \
+                               (major) * 10000 + (minor) * 100 + (bugfix) )
+                   ], [
+                     #if !GR2_VERSION_REQUIRE(1,3,8)
+                     #error "Insufficient graphite2 version."
+                     #endif
+                   ], [],
+                   [AC_MSG_ERROR([--with-system-graphite2 requested but no working libgraphite2 found])])
+    CFLAGS=$_SAVE_CFLAGS
+fi
+
+dnl ========================================================
 dnl Check for pixman and cairo
 dnl ========================================================

diff -Naur a/toolkit/library/moz.build b/toolkit/library/moz.build
--- a/toolkit/library/moz.build	2017-02-27 16:11:04.000000000 +0000
+++ b/toolkit/library/moz.build	2017-03-07 23:25:43.449654415 +0000
@@ -229,6 +229,12 @@
 if CONFIG['MOZ_SYSTEM_PNG']:
     OS_LIBS += CONFIG['MOZ_PNG_LIBS']

+if CONFIG['MOZ_SYSTEM_GRAPHITE2']:
+    OS_LIBS += CONFIG['MOZ_GRAPHITE2_LIBS']
+
+if CONFIG['MOZ_SYSTEM_HARFBUZZ']:
+    OS_LIBS += CONFIG['MOZ_HARFBUZZ_LIBS']
+
 if CONFIG['MOZ_SYSTEM_HUNSPELL']:
     OS_LIBS += CONFIG['MOZ_HUNSPELL_LIBS']

diff -Naur a/toolkit/moz.configure b/toolkit/moz.configure
--- a/toolkit/moz.configure	2017-02-27 16:11:04.000000000 +0000
+++ b/toolkit/moz.configure	2017-03-07 23:25:43.449654415 +0000
@@ -338,6 +338,34 @@
 add_old_configure_assignment('FT2_CFLAGS',
                              delayed_getattr(ft2_info, 'cflags'))

+# Graphite2
+# ==============================================================
+option('--with-system-graphite2',
+       help="Use system graphite2 (located with pkgconfig)")
+
+@depends('--with-system-graphite2')
+def check_for_graphite2(value):
+    return bool(value)
+
+system_graphite2 = pkg_check_modules('MOZ_GRAPHITE2', 'graphite2',
+                                     when=check_for_graphite2)
+
+set_config('MOZ_SYSTEM_GRAPHITE2', depends_if(system_graphite2)(lambda _: True))
+
+# HarfBuzz
+# ==============================================================
+option('--with-system-harfbuzz',
+       help="Use system harfbuzz (located with pkgconfig)")
+
+@depends('--with-system-harfbuzz')
+def check_for_harfbuzz(value):
+    return bool(value)
+
+system_harfbuzz = pkg_check_modules('MOZ_HARFBUZZ', 'harfbuzz >= 1.3.3',
+                                    when=check_for_harfbuzz)
+
+set_config('MOZ_SYSTEM_HARFBUZZ', depends_if(system_harfbuzz)(lambda _: True))
+
 # Apple platform decoder support
 # ==============================================================
 @depends(toolkit)
'''
        self.apply_patch(self.directory, system)
