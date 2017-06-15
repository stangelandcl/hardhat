from .base import GnuRecipe
import os


class LibMadRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibMadRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'bbfac3ed6bfbc2823d3775ebb9310873' \
                      '71e142bb0e9bb1bee51a76a6e0078690'

        self.name = 'libmad'
        self.version = '0.15.1b'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools']
        self.url = 'http://downloads.sourceforge.net/mad/' \
                   'libmad-$version.tar.gz'

    def patch(self):
        text = r'''
Submitted By:            Igor Å½ivkoviÄ‡ <contact at igor hyphen zivkovic dot from dot hr>
Date:                    2013-07-04
Initial Package Version: 0.15.1b
Upstream Status:         Reported
Origin:                  Arch Linux packages repository
Description:             Fixes compilation on x86-64 and optimization issues.

diff -Naur libmad-0.15.1b.orig/configure.ac libmad-0.15.1b/configure.ac
--- libmad-0.15.1b.orig/configure.ac	2004-01-23 10:41:32.000000000 +0100
+++ libmad-0.15.1b/configure.ac	2013-07-04 15:55:09.323764417 +0200
@@ -124,71 +124,7 @@

 if test "$GCC" = yes
 then
-    if test -z "$arch"
-    then
-	case "$host" in
-	    i386-*)           ;;
-	    i?86-*)           arch="-march=i486" ;;
-	    arm*-empeg-*)     arch="-march=armv4 -mtune=strongarm1100" ;;
-	    armv4*-*)         arch="-march=armv4 -mtune=strongarm" ;;
-	    powerpc-*)        ;;
-	    mips*-agenda-*)   arch="-mcpu=vr4100" ;;
-	    mips*-luxsonor-*) arch="-mips1 -mcpu=r3000 -Wa,-m4010" ;;
-	esac
-    fi
-
-    case "$optimize" in
-	-O|"-O "*)
-	    optimize="-O"
-	    optimize="$optimize -fforce-mem"
-	    optimize="$optimize -fforce-addr"
-	    : #x optimize="$optimize -finline-functions"
-	    : #- optimize="$optimize -fstrength-reduce"
-	    optimize="$optimize -fthread-jumps"
-	    optimize="$optimize -fcse-follow-jumps"
-	    optimize="$optimize -fcse-skip-blocks"
-	    : #x optimize="$optimize -frerun-cse-after-loop"
-	    : #x optimize="$optimize -frerun-loop-opt"
-	    : #x optimize="$optimize -fgcse"
-	    optimize="$optimize -fexpensive-optimizations"
-	    optimize="$optimize -fregmove"
-	    : #* optimize="$optimize -fdelayed-branch"
-	    : #x optimize="$optimize -fschedule-insns"
-	    optimize="$optimize -fschedule-insns2"
-	    : #? optimize="$optimize -ffunction-sections"
-	    : #? optimize="$optimize -fcaller-saves"
-	    : #> optimize="$optimize -funroll-loops"
-	    : #> optimize="$optimize -funroll-all-loops"
-	    : #x optimize="$optimize -fmove-all-movables"
-	    : #x optimize="$optimize -freduce-all-givs"
-	    : #? optimize="$optimize -fstrict-aliasing"
-	    : #* optimize="$optimize -fstructure-noalias"
-
-	    case "$host" in
-		arm*-*)
-		    optimize="$optimize -fstrength-reduce"
-		    ;;
-		mips*-*)
-		    optimize="$optimize -fstrength-reduce"
-		    optimize="$optimize -finline-functions"
-		    ;;
-		i?86-*)
-		    optimize="$optimize -fstrength-reduce"
-		    ;;
-		powerpc-apple-*)
-		    # this triggers an internal compiler error with gcc2
-		    : #optimize="$optimize -fstrength-reduce"
-
-		    # this is really only beneficial with gcc3
-		    : #optimize="$optimize -finline-functions"
-		    ;;
-		*)
-		    # this sometimes provokes bugs in gcc 2.95.2
-		    : #optimize="$optimize -fstrength-reduce"
-		    ;;
-	    esac
-	    ;;
-    esac
+    optimize="-O2"
 fi

 case "$host" in
@@ -297,6 +233,7 @@
 then
     case "$host" in
 	i?86-*)     FPM="INTEL"  ;;
+	x86_64*)    FPM="64BIT"  ;;
 	arm*-*)     FPM="ARM"    ;;
 	mips*-*)    FPM="MIPS"   ;;
 	sparc*-*)   FPM="SPARC"  ;;
'''

        self.apply_patch(self.directory, text)

        self.log_dir('patch', self.directory, 'run autoreconf')
        script = r'''
sed "s@AM_CONFIG_HEADER@AC_CONFIG_HEADERS@g" -i configure.ac
touch NEWS AUTHORS ChangeLog
autoreconf -fi
'''
        file = os.path.join(self.directory, 'init.sh')
        with open(file, 'wt') as f:
            f.write(script)
        self.run_exe(self.shell_args + [file],
                     self.directory,
                     self.environment)

    def install(self):
        super(LibMadRecipe, self).install()

        text = r'''
prefix=%s
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include

Name: mad
Description: MPEG audio decoder
Requires:
Version: 0.15.1b
Libs: -L${libdir} -lmad
Cflags: -I${includedir}
EOF
''' % self.prefix_dir

        filename = os.path.join(self.prefix_dir, 'lib', 'pkgconfig', 'mad.pc')
        self.log_dir('install', filename, 'write pkgconfig')
        with open(filename, 'wt') as f:
            f.write(text)
