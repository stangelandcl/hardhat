from .base import GnuRecipe


class PulseAudioRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PulseAudioRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f2521c525a77166189e3cb9169f75c2e' \
                      'e2b82fa3fcf9476024fbc2c3a6c9cd9e'

        self.name = 'pulseaudio'
        self.version = '11.1'
        self.depends = ['gdbm', 'intltool', 'json-c', 'libsndfile']
        self.url = 'http://freedesktop.org/software/pulseaudio/releases/' \
                   'pulseaudio-$version.tar.xz'
        self.configure_strip_cross_compile()
        self.configure_args += [
            '--disable-bluez4',
            '--disable-bluez5',
            '--disable-rpath',
            '--without-caps',
            '--disable-tests',
            '--disable-default-build-tests',
            '--with-sysroot=%s' % self.prefix_dir,
            '--with-udev-rules-dir=%s/udev/rules.d' % self.prefix_dir]
        self.environment['CFLAGS'] += ' -fno-strict-aliasing'
        # This may not be required. it was an attempted fix that didn't work
        self.environment['LDFLAGS'] += ' -L%s/src/.libs' % self.directory

    def patch(self):
        # from http://www.linuxfromscratch.org/patches/blfs/svn/
        # pulseaudio-11.1-glibc_2.27_fix-1.patch
        text = r'''Submitted By: Ken Moffat <ken at linuxfromscratch dot org>
Date: 2018-02-10
Initial Package Version: 11.1
Upstream Status: Applied
Origin: Upstream
Description: Fixes breakage caused by glibc-2.27.

>From 01239c23f57e74ec40c92144d22fe153ee65f4ff Mon Sep 17 00:00:00 2001
From: Tanu Kaskinen <tanuk at iki.fi>
Date: Wed, 24 Jan 2018 03:51:49 +0200
Subject: [PATCH] memfd-wrappers: only define memfd_create() if not already
 defined

glibc 2.27 is to be released soon, and it will provide memfd_create().
If glibc provides the function, we must not define it ourselves,
otherwise building fails due to conflict between the two implementations
of the same function.

BugLink: https://bugs.freedesktop.org/show_bug.cgi?id=104733
---
 configure.ac                   | 3 +++
 src/pulsecore/memfd-wrappers.h | 7 ++++---
 2 files changed, 7 insertions(+), 3 deletions(-)

diff --git a/configure.ac b/configure.ac
index 013918f1a..1095ae8cb 100644
--- a/configure.ac
+++ b/configure.ac
@@ -607,6 +607,9 @@ AS_IF([test "x$enable_memfd" = "xyes" && test "x$HAVE_MEMFD" = "x0"],
     [AC_MSG_ERROR([*** Your Linux kernel does not support memfd shared memory.
                   *** Use linux v3.17 or higher for such a feature.])])

+AS_IF([test "x$HAVE_MEMFD" = "x1"],
+    AC_CHECK_FUNCS([memfd_create]))
+
 AC_SUBST(HAVE_MEMFD)
 AM_CONDITIONAL([HAVE_MEMFD], [test "x$HAVE_MEMFD" = x1])
 AS_IF([test "x$HAVE_MEMFD" = "x1"], AC_DEFINE([HAVE_MEMFD], 1, [Have memfd shared memory.]))
diff --git a/src/pulsecore/memfd-wrappers.h b/src/pulsecore/memfd-wrappers.h
index 3bed9b2b1..c7aadfd3c 100644
--- a/src/pulsecore/memfd-wrappers.h
+++ b/src/pulsecore/memfd-wrappers.h
@@ -20,13 +20,14 @@
   License along with PulseAudio; if not, see <http://www.gnu.org/licenses/>.
 ***/

-#ifdef HAVE_MEMFD
+#if defined(HAVE_MEMFD) && !defined(HAVE_MEMFD_CREATE)

 #include <sys/syscall.h>
 #include <fcntl.h>

 /*
- * No glibc wrappers exist for memfd_create(2), so provide our own.
+ * Before glibc version 2.27 there was no wrapper for memfd_create(2),
+ * so we have to provide our own.
  *
  * Also define memfd fcntl sealing macros. While they are already
  * defined in the kernel header file <linux/fcntl.h>, that file as
@@ -63,6 +64,6 @@ static inline int memfd_create(const char *name, unsigned int flags) {
 #define F_SEAL_WRITE    0x0008  /* prevent writes */
 #endif

-#endif /* HAVE_MEMFD */
+#endif /* HAVE_MEMFD && !HAVE_MEMFD_CREATE */

 #endif
--
2.15.1
'''
        self.apply_patch(self.directory, text)
