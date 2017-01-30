import os
from string import Template
from .base import GnuRecipe
from ..util import patch


class FirefoxRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FirefoxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '30ba00ba716ea1eeda526e2ccc8642f8' \
                      'd18a836793fde50e87a4fcb9d9fccca9'

        self.name = 'firefox'
        self.version = '51.0.1'
        self.version_regex = r'(?P<version>\d+\.\d+(\.\d+)*)'
        self.version_url = 'https://ftp.mozilla.org/pub/mozilla.org/firefox/' \
                           'releases/'
        self.depends = ['alsa-lib',
                        'autoconf',
                        'autoconf2.13',
                        'curl',
                        'dbus-glib',
                        'gconf',
                        'graphite2',
                        'gtk3',
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
        self.environment['CFLAGS'] = ' -O0 -g -ggdb3'
        self.environment['CXXFLAGS'] = ' -O0 -g -ggdb3'

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
#ac_add_options --enable-default-toolkit=cairo-gtk2

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
ac_add_options --disable-strip
ac_add_options --disable-install-strip

# The BLFS editors recommend not changing anything below this line:
ac_add_options --prefix=${prefix}
ac_add_options --enable-application=browser

ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --disable-tests

# disable for debugging
ac_add_options --disable-optimize
ac_add_options --enable-debug


ac_add_options --enable-gio
ac_add_options --enable-official-branding
ac_add_options --enable-safe-browsing
ac_add_options --enable-url-classifier

# From firefox-40, using system cairo causes firefox to crash
# frequently when it is doing background rendering in a tab.
#ac_add_options --enable-system-cairo
ac_add_options --enable-system-ffi
ac_add_options --enable-system-pixman

#ac_add_options --with-pthreads

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
        src = r'''#ifdef MOZ_DEBUG'''
        dst = r'''#ifndef MOZ_DEBUG'''
        file = os.path.join(self.directory, 'browser/installer/package-manifest.in')
        patch(file, src, dst)

        system = r'''
Submitted By: Ken Moffat <ken at linuxfromscratch dot org>
Date: 2017-01-24
Initial Package Version: 51.0
Upstream Status: Waiting for review (mozilla bug 847568)
Origin: OpenBSD (via gentoo)
Description: Allow use of system versions of graphite2 and harfbuzz.  This
should be regarded as experimental.  Add the options --with-system-graphite2
and --with-system-harfbuzz to use this (needs recent versions of both).
The source of this latest version is from
https://dev.gentoo.org/~anarchy/mozilla/patchsets/firefox-51.0-patches-04.tar.xz

Previous versions of the patch were at https://dev.gentoo.org/~axs/mozilla/patchsets/

diff --git a/build/moz.configure/old.configure b/build/moz.configure/old.configure
--- a/build/moz.configure/old.configure
+++ b/build/moz.configure/old.configure
@@ -279,16 +279,18 @@ def old_configure_options(*options):
     '--with-nspr-prefix',
     '--with-nss-exec-prefix',
     '--with-nss-prefix',
     '--with-pthreads',
     '--with-qemu-exe',
     '--with-sixgill',
     '--with-soft-float',
     '--with-system-bz2',
+    '--with-system-graphite2',
+    '--with-system-harfbuzz',
     '--with-system-icu',
     '--with-system-jpeg',
     '--with-system-libevent',
     '--with-system-libvpx',
     '--with-system-nspr',
     '--with-system-nss',
     '--with-system-png',
     '--with-system-zlib',
diff --git a/config/Makefile.in b/config/Makefile.in
--- a/config/Makefile.in
+++ b/config/Makefile.in
@@ -44,16 +44,18 @@ export:: $(export-preqs)
 		-DMOZ_SYSTEM_HUNSPELL=$(MOZ_SYSTEM_HUNSPELL) \
 		-DMOZ_SYSTEM_BZ2=$(MOZ_SYSTEM_BZ2) \
 		-DMOZ_SYSTEM_ZLIB=$(MOZ_SYSTEM_ZLIB) \
 		-DMOZ_SYSTEM_PNG=$(MOZ_SYSTEM_PNG) \
 		-DMOZ_SYSTEM_JPEG=$(MOZ_SYSTEM_JPEG) \
 		-DMOZ_SYSTEM_LIBEVENT=$(MOZ_SYSTEM_LIBEVENT) \
 		-DMOZ_SYSTEM_LIBVPX=$(MOZ_SYSTEM_LIBVPX) \
 		-DMOZ_SYSTEM_ICU=$(MOZ_SYSTEM_ICU) \
+		-DMOZ_SYSTEM_GRAPHITE2=$(MOZ_SYSTEM_GRAPHITE2) \
+		-DMOZ_SYSTEM_HARFBUZZ=$(MOZ_SYSTEM_HARFBUZZ) \
 		$(srcdir)/system-headers $(srcdir)/stl-headers | $(PERL) $(topsrcdir)/nsprpub/config/make-system-wrappers.pl system_wrappers
 	$(INSTALL) system_wrappers $(DIST)

 GARBAGE_DIRS += system_wrappers
 endif

 ifdef WRAP_STL_INCLUDES
 ifdef GNU_CXX
diff --git a/config/system-headers b/config/system-headers
--- a/config/system-headers
+++ b/config/system-headers
@@ -1327,8 +1327,16 @@ unicode/udatpg.h
 unicode/uenum.h
 unicode/unorm.h
 unicode/unum.h
 unicode/ustring.h
 unicode/utypes.h
 #endif
 libutil.h
 unwind.h
+#if MOZ_SYSTEM_GRAPHITE2==1
+graphite2/Font.h
+graphite2/Segment.h
+#endif
+#if MOZ_SYSTEM_HARFBUZZ==1
+harfbuzz/hb-ot.h
+harfbuzz/hb.h
+#endif
diff --git a/extensions/spellcheck/hunspell/glue/moz.build b/extensions/spellcheck/hunspell/glue/moz.build
--- a/extensions/spellcheck/hunspell/glue/moz.build
+++ b/extensions/spellcheck/hunspell/glue/moz.build
@@ -31,9 +31,9 @@ IPDL_SOURCES = [

 EXPORTS.mozilla += [
      'RemoteSpellCheckEngineChild.h',
      'RemoteSpellCheckEngineParent.h',
 ]

 # This variable is referenced in configure.in.  Make sure to change that file
 # too if you need to change this variable.
-DEFINES['HUNSPELL_STATIC'] = True
+DEFINES['HUNSPELL_STATIC'] = not CONFIG['MOZ_SYSTEM_HUNSPELL']
diff --git a/gfx/graphite2/moz-gr-update.sh b/gfx/graphite2/moz-gr-update.sh
--- a/gfx/graphite2/moz-gr-update.sh
+++ b/gfx/graphite2/moz-gr-update.sh
@@ -1,11 +1,12 @@
 #!/bin/bash

 # Script used to update the Graphite2 library in the mozilla source tree
+# and bump version for --with-system-graphite2

 # This script lives in gfx/graphite2, along with the library source,
 # but must be run from the top level of the mozilla-central tree.

 # Run as
 #
 #    ./gfx/graphite2/moz-gr-update.sh RELEASE
 #
@@ -32,22 +33,26 @@ echo "This directory contains the Graphi
 echo "$TARBALL" >> gfx/graphite2/README.mozilla
 echo ""
 echo "See" $0 "for update procedure." >> gfx/graphite2/README.mozilla

 # fix up includes because of bug 721839 (cstdio) and bug 803066 (Windows.h)
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
 echo changes to gfx/graphite2/src/moz.build
 echo

 echo
 echo Now use hg commands to create a patch for the mozilla tree.
diff --git a/gfx/moz.build b/gfx/moz.build
--- a/gfx/moz.build
+++ b/gfx/moz.build
@@ -2,26 +2,30 @@
 # vim: set filetype=python:
 # This Source Code Form is subject to the terms of the Mozilla Public
 # License, v. 2.0. If a copy of the MPL was not distributed with this
 # file, You can obtain one at http://mozilla.org/MPL/2.0/.

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
     'angle',
     'src',
     'qcms',
     'gl',
     'layers',
-    'graphite2/src',
-    'harfbuzz/src',
     'ots/src',
     'thebes',
     'ipc',
     'vr',
     'config',
 ]

 if CONFIG['MOZ_ENABLE_SKIA']:
diff --git a/gfx/thebes/moz.build b/gfx/thebes/moz.build
--- a/gfx/thebes/moz.build
+++ b/gfx/thebes/moz.build
@@ -281,13 +281,16 @@ if CONFIG['MOZ_WIDGET_TOOLKIT'] in ('and
     CXXFLAGS += CONFIG['CAIRO_FT_CFLAGS']

 if CONFIG['MOZ_WIDGET_TOOLKIT'] in ('gtk2', 'gtk3'):
     CXXFLAGS += CONFIG['MOZ_PANGO_CFLAGS']

 LOCAL_INCLUDES += CONFIG['SKIA_INCLUDES']
 LOCAL_INCLUDES += ['/media/libyuv/include']

-DEFINES['GRAPHITE2_STATIC'] = True
+if CONFIG['MOZ_SYSTEM_GRAPHITE2']:
+    CXXFLAGS += CONFIG['MOZ_GRAPHITE2_CFLAGS']
+else:
+    DEFINES['GRAPHITE2_STATIC'] = True

 if CONFIG['CLANG_CXX']:
     # Suppress warnings from Skia header files.
     SOURCES['gfxPlatform.cpp'].flags += ['-Wno-implicit-fallthrough']
diff --git a/old-configure.in b/old-configure.in
--- a/old-configure.in
+++ b/old-configure.in
@@ -5215,16 +5215,61 @@ if test "$USE_FC_FREETYPE"; then
         else
             FT2_CFLAGS="$FT2_CFLAGS $_FONTCONFIG_CFLAGS"
             FT2_LIBS="$FT2_LIBS $_FONTCONFIG_LIBS"
         fi
     ])
 fi

 dnl ========================================================
+dnl Check for harfbuzz
+dnl ========================================================
+
+MOZ_ARG_WITH_BOOL(system-harfbuzz,
+[  --with-system-harfbuzz  Use system harfbuzz (located with pkgconfig)],
+MOZ_SYSTEM_HARFBUZZ=1,
+MOZ_SYSTEM_HARFBUZZ=)
+
+if test -n "$MOZ_SYSTEM_HARFBUZZ"; then
+    PKG_CHECK_MODULES(MOZ_HARFBUZZ, harfbuzz >= 1.2.6)
+    CFLAGS="$CFLAGS $MOZ_HARFBUZZ_CFLAGS"
+    CXXFLAGS="$CXXFLAGS $MOZ_HARFBUZZ_CXXFLAGS"
+fi
+
+AC_SUBST(MOZ_SYSTEM_HARFBUZZ)
+
+dnl ========================================================
+dnl Check for graphite2
+dnl ========================================================
+
+MOZ_ARG_WITH_BOOL(system-graphite2,
+[  --with-system-graphite2 Use system graphite2 (located with pkgconfig)],
+MOZ_SYSTEM_GRAPHITE2=1,
+MOZ_SYSTEM_GRAPHITE2=)
+
+if test -n "$MOZ_SYSTEM_GRAPHITE2"; then
+    PKG_CHECK_MODULES(MOZ_GRAPHITE2, graphite2)
+
+    dnl graphite2.pc has bogus version, check manually
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
+fi
+
+AC_SUBST(MOZ_SYSTEM_GRAPHITE2)
+
+dnl ========================================================
 dnl Check for pixman and cairo
 dnl ========================================================

 MOZ_TREE_CAIRO=1
 MOZ_ARG_ENABLE_BOOL(system-cairo,
 [  --enable-system-cairo   Use system cairo (located with pkgconfig)],
 MOZ_TREE_CAIRO=,
 MOZ_TREE_CAIRO=1 )
diff --git a/toolkit/library/moz.build b/toolkit/library/moz.build
--- a/toolkit/library/moz.build
+++ b/toolkit/library/moz.build
@@ -241,16 +241,22 @@ if CONFIG['MOZ_SYSTEM_LIBVPX']:
     OS_LIBS += CONFIG['MOZ_LIBVPX_LIBS']

 if not CONFIG['MOZ_TREE_PIXMAN']:
     OS_LIBS += CONFIG['MOZ_PIXMAN_LIBS']

 if CONFIG['MOZ_ALSA']:
     OS_LIBS += CONFIG['MOZ_ALSA_LIBS']

+if CONFIG['MOZ_SYSTEM_GRAPHITE2']:
+    OS_LIBS += CONFIG['MOZ_GRAPHITE2_LIBS']
+
+if CONFIG['MOZ_SYSTEM_HARFBUZZ']:
+    OS_LIBS += CONFIG['MOZ_HARFBUZZ_LIBS']
+
 if CONFIG['HAVE_CLOCK_MONOTONIC']:
     OS_LIBS += CONFIG['REALTIME_LIBS']

 if CONFIG['MOZ_WIDGET_TOOLKIT'] == 'android':
     OS_LIBS += [
         'GLESv2',
     ]

'''
        self.apply_patch(self.directory, system)

        # Temporary debugging code
        src = r'''static bool
equal(const char* s1, const char* s2)
{
    return !strcmp(s1, s2);
}'''

        dst = r'''static bool
equal(const char* s1, const char* s2)
{
    if(!s1)
    {
        if(!s2)
        {
            printf("equal: comparing null to null\n");
            return false;
        }
        printf("equal: comparing null to %s\n", s2);
        return false;
    }
    else if(!s2)
    {
        printf("equal: comparing %s to null\n", s1);
        return false;
    }
    return !strcmp(s1, s2);
}'''
        file = os.path.join(self.directory, 'js/src/builtin/Intl.cpp')
        patch(file, src, dst)

        src = r'''UEnumeration* values = ucol_getKeywordValuesForLocale("co", locale.ptr(), false, &status);
'''
        dst = r'''printf("Using locale=%s\n", locale.ptr()); UEnumeration* values = ucol_getKeywordValuesForLocale("co", locale.ptr(), false, &status);'''
        patch(file, src, dst)
