import os
from .base import GnuRecipe
from ..util import patch


class LuaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LuaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5113c06884f7de453ce57702abaac1d6' \
                      '18307f33f6789fa870e87a59d772aca2'

        self.name = 'lua'
        self.version = '5.3.3'
        self.url = 'http://www.lua.org/ftp/lua-$version.tar.gz'
        self.rebuilds = ['graphviz']
        self.compile_args = ['make',
                             'MYCFLAGS="-DLUA_COMPAT_5_2 -DLUA_COMPAT_5_1"',
                             'linux']
        self.install_args = [
            ['make',
             'INSTALL_TOP=%s' % self.prefix_dir,
             'TO_LIB="liblua.so liblua.so.5.3 liblua.so.5.3.3"',
             'INSTALL_DATA="cp -d"',
             'INSTALL_MAN=%s/share/man/man1' % self.prefix_dir,
             'install'],
            ['mkdir', '-pv', '%s/share/doc/lua-%s' %
             (self.prefix_dir, self.version)],
            ['cp', '-v', 'doc/*.{html,css,gif,png}', '%s/share/doc/lua-%s' %
             (self.prefix_dir, self.version)],
            ['install', '-v', '-m644', '-D', 'lua.pc',
             '%s/lib/pkgconfig/lua.pc' % self.prefix_dir]
            ]

    def install(self):
        text = r'''
V=5.3
R=5.3.3

prefix=%s
INSTALL_BIN=${prefix}/bin
INSTALL_INC=${prefix}/include
INSTALL_LIB=${prefix}/lib
INSTALL_MAN=${prefix}/share/man/man1
INSTALL_LMOD=${prefix}/share/lua/${V}
INSTALL_CMOD=${prefix}/lib/lua/${V}
exec_prefix=${prefix}
libdir=${exec_prefix}/lib
includedir=${prefix}/include

Name: Lua
Description: An Extensible Extension Language
Version: ${R}
Requires:
Libs: -L${libdir} -llua -lm -ldl
Cflags: -I${includedir}
EOF
''' % self.prefix_dir

        filename = os.path.join(self.directory, 'lua.pc')
        with open(filename, 'wt') as f:
            f.write(text)

        super(LuaRecipe, self).install()



    def patch(self):
        src = r'#define LUA_ROOT	"/usr/local/"'
        dst = r'#define LUA_ROOT	"%s"' % self.prefix_dir
        filename = os.path.join(self.directory, 'src', 'luaconf.h')
        patch(filename, src, dst)


        text = r'''
Submitted By:            Igor Živković <contact@igor-zivkovic.from.hr>
Date:                    2013-06-19
Initial Package Version: 5.2.2
Upstream Status:         Rejected
Origin:                  Arch Linux packages repository
Description:             Adds the compilation of a shared library.

diff -Naur lua-5.3.0.orig/Makefile lua-5.3.0/Makefile
--- lua-5.3.0.orig/Makefile	2014-10-30 00:14:41.000000000 +0100
+++ lua-5.3.0/Makefile	2015-01-19 22:14:09.822290828 +0100
@@ -52,7 +52,7 @@
 all:	$(PLAT)

 $(PLATS) clean:
-	cd src && $(MAKE) $@
+	cd src && $(MAKE) $@ V=$(V) R=$(R)

 test:	dummy
 	src/lua -v
diff -Naur lua-5.3.0.orig/src/Makefile lua-5.3.0/src/Makefile
--- lua-5.3.0.orig/src/Makefile	2015-01-05 17:04:52.000000000 +0100
+++ lua-5.3.0/src/Makefile	2015-01-19 22:14:52.559378543 +0100
@@ -7,7 +7,7 @@
 PLAT= none

 CC= gcc -std=gnu99
-CFLAGS= -O2 -Wall -Wextra -DLUA_COMPAT_5_2 $(SYSCFLAGS) $(MYCFLAGS)
+CFLAGS= -fPIC -O2 -Wall -Wextra -DLUA_COMPAT_5_2 $(SYSCFLAGS) $(MYCFLAGS)
 LDFLAGS= $(SYSLDFLAGS) $(MYLDFLAGS)
 LIBS= -lm $(SYSLIBS) $(MYLIBS)

@@ -29,6 +29,7 @@
 PLATS= aix bsd c89 freebsd generic linux macosx mingw posix solaris

 LUA_A=	liblua.a
+LUA_SO= liblua.so
 CORE_O=	lapi.o lcode.o lctype.o ldebug.o ldo.o ldump.o lfunc.o lgc.o llex.o \
 	lmem.o lobject.o lopcodes.o lparser.o lstate.o lstring.o ltable.o \
 	ltm.o lundump.o lvm.o lzio.o
@@ -43,7 +44,7 @@
 LUAC_O=	luac.o

 ALL_O= $(BASE_O) $(LUA_O) $(LUAC_O)
-ALL_T= $(LUA_A) $(LUA_T) $(LUAC_T)
+ALL_T= $(LUA_A) $(LUA_T) $(LUAC_T) $(LUA_SO)
 ALL_A= $(LUA_A)

 # Targets start here.
@@ -59,6 +60,12 @@
 	$(AR) $@ $(BASE_O)
 	$(RANLIB) $@

+$(LUA_SO): $(CORE_O) $(LIB_O)
+	$(CC) -shared -ldl -Wl,-soname,$(LUA_SO).$(V) -o $@.$(R) $? -lm $(MYLDFLAGS)
+	ln -sf $(LUA_SO).$(R) $(LUA_SO).$(V)
+	ln -sf $(LUA_SO).$(R) $(LUA_SO)
+
+
 $(LUA_T): $(LUA_O) $(LUA_A)
 	$(CC) -o $@ $(LDFLAGS) $(LUA_O) $(LUA_A) $(LIBS)

'''
        self.apply_patch(self.directory, text)
