import os
from .base import GnuRecipe
from ..util import patch


class NssRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NssRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2c643d3c08d6935f4d325f40743719b6' \
                      '990aa25a79ec2f8f712c99d086672f62'

        self.name = 'nss'
        self.depends = ['nspr', 'p11-kit', 'sqlite3']
        self.version = '3.38'
        self.version_regex = r'(?P<version>\d+\.\d+(\.\d+)*)'
        s = self.version.replace('.', '_')
        self.url = 'https://ftp.mozilla.org/pub/mozilla.org/security/nss/' \
                   'releases/NSS_%s_RTM/src/nss-$version.tar.gz' % s

        self.compile_args = [
            'make', '-j1', 'BUILD_OPT=1',
            'NSPR_INCLUDE_DIR=%s/include/nspr' % self.prefix_dir,
            'USE_SYSTEM_ZLIB=1',
            'ZLIB_LIBS=-lz',
            'USE_64=1',
            'NSS_USE_SYSTEM_SQLITE=1',
            'PREFIX=%s' % self.prefix_dir]

        self.environment['CFLAGS'] += ' -Wno-error=int-in-bool-context'
        self.environment['CXXFLAGS'] += ' -Wno-error=int-in-bool-context'

        self.install_args = [
            ('install -v -m755 Linux*/lib/*.so %s/lib'
             % self.prefix_dir).split(),
            ('install -v -m644 Linux*/lib/{*.chk,libcrmf.a} %s/lib'
             % self.prefix_dir).split(),
            ('install -v -m755 -d %s/include/nss'
             % self.prefix_dir).split(),
            ('cp -v -RL {public,private}/nss/* %s/include/nss'
             % self.prefix_dir).split(),
            ('chmod -v 644 %s/include/nss/*' % self.prefix_dir).split(),
            ('install -v -m755 Linux*/bin/{certutil,nss-config,pk12util}'
             ' %s/bin' % self.prefix_dir).split(),
            ('install -v -m644 Linux*/lib/pkgconfig/nss.pc %s/lib/pkgconfig'
             % self.prefix_dir).split()
            ]

    def configure(self):
        pass

    def install(self):
        self.directory = os.path.join(self.directory, '..', 'dist')
        super(NssRecipe, self).install()
        self.log_dir('install', self.directory, 'using system certificates')
        cmd = r'''rm -f ${HARDHAT_PREFIX}/lib/libnssckbi.so && \
ln -sfv ${HARDHAT_PREFIX}/lib/libp11-kit.so ${HARDHAT_PREFIX}/lib/libnssckbi.so
'''
        self.run_exe(cmd, self.directory, self.environment)

    def patch(self):
        text = r'''
Submitted By:            DJ Lucas <dj_AT_linuxfromscratch_DOT_org>
Date:                    2016-12-27
Initial Package Version: 3.12.4
Upstream Status:         Not applicable
Origin:                  Self, rediffed for nss-3.28.
Description:             Adds auto-generated nss.pc and nss-config script, and
                         allows building without nspr in the source tree.
                         For 3.35, Requires: updated to nspr >= 4.18.

diff -Naurp nss-3.28-orig/nss/Makefile nss-3.28/nss/Makefile
--- nss-3.28-orig/nss/Makefile	2016-12-21 05:56:27.000000000 -0600
+++ nss-3.28/nss/Makefile	2016-12-26 22:24:52.695146032 -0600
@@ -46,7 +46,7 @@ include $(CORE_DEPTH)/coreconf/rules.mk
 # (7) Execute "local" rules. (OPTIONAL).                              #
 #######################################################################

-nss_build_all: build_nspr all latest
+nss_build_all: all latest

 nss_clean_all: clobber_nspr clobber

diff -Naurp nss-3.28-orig/nss/config/Makefile nss-3.28/nss/config/Makefile
--- nss-3.28-orig/nss/config/Makefile	1969-12-31 18:00:00.000000000 -0600
+++ nss-3.28/nss/config/Makefile	2016-12-26 22:20:40.008205774 -0600
@@ -0,0 +1,40 @@
+CORE_DEPTH = ..
+DEPTH      = ..
+
+include $(CORE_DEPTH)/coreconf/config.mk
+
+NSS_MAJOR_VERSION = `grep "NSS_VMAJOR" ../lib/nss/nss.h | awk '{print $$3}'`
+NSS_MINOR_VERSION = `grep "NSS_VMINOR" ../lib/nss/nss.h | awk '{print $$3}'`
+NSS_PATCH_VERSION = `grep "NSS_VPATCH" ../lib/nss/nss.h | awk '{print $$3}'`
+PREFIX = /usr
+
+all: export libs
+
+export:
+	# Create the nss.pc file
+	mkdir -p $(DIST)/lib/pkgconfig
+	sed -e "s,@prefix@,$(PREFIX)," \
+	    -e "s,@exec_prefix@,\$${prefix}," \
+	    -e "s,@libdir@,\$${prefix}/lib," \
+	    -e "s,@includedir@,\$${prefix}/include/nss," \
+	    -e "s,@NSS_MAJOR_VERSION@,$(NSS_MAJOR_VERSION),g" \
+	    -e "s,@NSS_MINOR_VERSION@,$(NSS_MINOR_VERSION)," \
+	    -e "s,@NSS_PATCH_VERSION@,$(NSS_PATCH_VERSION)," \
+	    nss.pc.in > nss.pc
+	chmod 0644 nss.pc
+	ln -sf ../../../../nss/config/nss.pc $(DIST)/lib/pkgconfig
+
+	# Create the nss-config script
+	mkdir -p $(DIST)/bin
+	sed -e "s,@prefix@,$(PREFIX)," \
+	    -e "s,@NSS_MAJOR_VERSION@,$(NSS_MAJOR_VERSION)," \
+	    -e "s,@NSS_MINOR_VERSION@,$(NSS_MINOR_VERSION)," \
+	    -e "s,@NSS_PATCH_VERSION@,$(NSS_PATCH_VERSION)," \
+	    nss-config.in > nss-config
+	chmod 0755 nss-config
+	ln -sf ../../../nss/config/nss-config $(DIST)/bin
+
+libs:
+
+dummy: all export libs
+
diff -Naurp nss-3.28-orig/nss/config/nss-config.in nss-3.28/nss/config/nss-config.in
--- nss-3.28-orig/nss/config/nss-config.in	1969-12-31 18:00:00.000000000 -0600
+++ nss-3.28/nss/config/nss-config.in	2016-12-26 22:20:40.008205774 -0600
@@ -0,0 +1,153 @@
+#!/bin/sh
+
+prefix=@prefix@
+
+major_version=@NSS_MAJOR_VERSION@
+minor_version=@NSS_MINOR_VERSION@
+patch_version=@NSS_PATCH_VERSION@
+
+usage()
+{
+	cat <<EOF
+Usage: nss-config [OPTIONS] [LIBRARIES]
+Options:
+	[--prefix[=DIR]]
+	[--exec-prefix[=DIR]]
+	[--includedir[=DIR]]
+	[--libdir[=DIR]]
+	[--version]
+	[--libs]
+	[--cflags]
+Dynamic Libraries:
+	nss
+	nssutil
+	smime
+	ssl
+	softokn
+EOF
+	exit $1
+}
+
+if test $# -eq 0; then
+	usage 1 1>&2
+fi
+
+lib_nss=yes
+lib_nssutil=yes
+lib_smime=yes
+lib_ssl=yes
+lib_softokn=yes
+
+while test $# -gt 0; do
+  case "$1" in
+  -*=*) optarg=`echo "$1" | sed 's/[-_a-zA-Z0-9]*=//'` ;;
+  *) optarg= ;;
+  esac
+
+  case $1 in
+    --prefix=*)
+      prefix=$optarg
+      ;;
+    --prefix)
+      echo_prefix=yes
+      ;;
+    --exec-prefix=*)
+      exec_prefix=$optarg
+      ;;
+    --exec-prefix)
+      echo_exec_prefix=yes
+      ;;
+    --includedir=*)
+      includedir=$optarg
+      ;;
+    --includedir)
+      echo_includedir=yes
+      ;;
+    --libdir=*)
+      libdir=$optarg
+      ;;
+    --libdir)
+      echo_libdir=yes
+      ;;
+    --version)
+      echo ${major_version}.${minor_version}.${patch_version}
+      ;;
+    --cflags)
+      echo_cflags=yes
+      ;;
+    --libs)
+      echo_libs=yes
+      ;;
+    nss)
+      lib_nss=yes
+      ;;
+    nssutil)
+      lib_nssutil=yes
+      ;;
+    smime)
+      lib_smime=yes
+      ;;
+    ssl)
+      lib_ssl=yes
+      ;;
+    softokn)
+      lib_softokn=yes
+      ;;
+    *)
+      usage 1 1>&2
+      ;;
+  esac
+  shift
+done
+
+# Set variables that may be dependent upon other variables
+if test -z "$exec_prefix"; then
+    exec_prefix=`pkg-config --variable=exec_prefix nss`
+fi
+if test -z "$includedir"; then
+    includedir=`pkg-config --variable=includedir nss`
+fi
+if test -z "$libdir"; then
+    libdir=`pkg-config --variable=libdir nss`
+fi
+
+if test "$echo_prefix" = "yes"; then
+    echo $prefix
+fi
+
+if test "$echo_exec_prefix" = "yes"; then
+    echo $exec_prefix
+fi
+
+if test "$echo_includedir" = "yes"; then
+    echo $includedir
+fi
+
+if test "$echo_libdir" = "yes"; then
+    echo $libdir
+fi
+
+if test "$echo_cflags" = "yes"; then
+    echo -I$includedir
+fi
+
+if test "$echo_libs" = "yes"; then
+      libdirs="-L$libdir"
+      if test -n "$lib_nss"; then
+	libdirs="$libdirs -lnss${major_version}"
+      fi
+      if test -n "$lib_nssutil"; then
+        libdirs="$libdirs -lnssutil${major_version}"
+      fi
+      if test -n "$lib_smime"; then
+	libdirs="$libdirs -lsmime${major_version}"
+      fi
+      if test -n "$lib_ssl"; then
+	libdirs="$libdirs -lssl${major_version}"
+      fi
+      if test -n "$lib_softokn"; then
+        libdirs="$libdirs -lsoftokn${major_version}"
+      fi
+      echo $libdirs
+fi
+
diff -Naurp nss-3.28-orig/nss/config/nss.pc.in nss-3.28/nss/config/nss.pc.in
--- nss-3.28-orig/nss/config/nss.pc.in	1969-12-31 18:00:00.000000000 -0600
+++ nss-3.28/nss/config/nss.pc.in	2016-12-26 22:22:53.300694346 -0600
@@ -0,0 +1,12 @@
+prefix=@prefix@
+exec_prefix=@exec_prefix@
+libdir=@libdir@
+includedir=@includedir@
+
+Name: NSS
+Description: Network Security Services
+Version: @NSS_MAJOR_VERSION@.@NSS_MINOR_VERSION@.@NSS_PATCH_VERSION@
+Requires: nspr >= 4.18
+Libs: -L@libdir@ -lnss@NSS_MAJOR_VERSION@ -lnssutil@NSS_MAJOR_VERSION@ -lsmime@NSS_MAJOR_VERSION@ -lssl@NSS_MAJOR_VERSION@ -lsoftokn@NSS_MAJOR_VERSION@
+Cflags: -I${includedir}
+
diff -Naurp nss-3.28-orig/nss/manifest.mn nss-3.28/nss/manifest.mn
--- nss-3.28-orig/nss/manifest.mn	2016-12-21 05:56:27.000000000 -0600
+++ nss-3.28/nss/manifest.mn	2016-12-26 22:24:12.278991843 -0600
@@ -10,4 +10,4 @@ IMPORTS =	nspr20/v4.8 \

 RELEASE = nss

-DIRS = coreconf lib cmd cpputil gtests
+DIRS = coreconf lib cmd cpputil gtests config
'''

        self.apply_patch(self.directory, text)
        self.directory = os.path.join(self.directory, 'nss')

#        filename = os.path.join(
#            self.directory,
#            'lib/libpkix/pkix_pl_nss/pki/pkix_pl_ocsprequest.c')
#        src = r'''*pHashcode = (((((extensionHash << 8) || certHash) << 8) ||'''
#        dst = r'''*pHashcode = (((((extensionHash << 8) != 0 || certHash) << 8) != 0 ||'''
#        patch(filename, src, dst)

#        src = r'''dateHash) << 8) || signerHash;'''
#        dst = r'''dateHash) << 8) != 0 || signerHash;'''
#        patch(filename, src, dst)
