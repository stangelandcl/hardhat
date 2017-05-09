import os
from .base import GnuRecipe
from ..util import patch


class FontConfigRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FontConfigRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b449a3e10c47e1d1c7a6ec6e2016cca7' \
                      '3d3bd68fbbd4f0ae5cc6b573f7d6c7f3'

        self.depends = ['freetype']
        self.name = 'fontconfig'
        self.version = '2.12.1'
        self.url = 'http://www.freedesktop.org/software/fontconfig/release/' \
                   'fontconfig-$version.tar.bz2'
        self.configure_args += ['--sysconfdir=%s/etc' % self.prefix_dir,
                                '--localstatedir=%s/var' % self.prefix_dir,
                                '--disable-docs',
                                '--with-default-fonts=%s/share/fonts'
                                % self.prefix_dir
                                ]
    def patch(self):
        text = r'''
From 20cddc824c6501c2082cac41b162c34cd5fcc530 Mon Sep 17 00:00:00 2001
From: Khem Raj <raj.khem@gmail.com>
Date: Sun, 11 Dec 2016 14:32:00 -0800
Subject: [PATCH] Avoid conflicts with integer width macros from TS
 18661-1:2014

glibc 2.25+ has now defined these macros in <limits.h>
https://sourceware.org/git/?p=glibc.git;a=commit;h=5b17fd0da62bf923cb61d1bb7b08cf2e1f1f9c1a

Signed-off-by: Khem Raj <raj.khem@gmail.com>
---
Upstream-Status: Submitted

 fontconfig/fontconfig.h | 2 +-
 src/fcobjs.h            | 2 +-
 src/fcobjshash.gperf    | 2 +-
 src/fcobjshash.h        | 2 +-
 4 files changed, 4 insertions(+), 4 deletions(-)

Index: fontconfig-2.12.1/fontconfig/fontconfig.h
===================================================================
--- fontconfig-2.12.1.orig/fontconfig/fontconfig.h
+++ fontconfig-2.12.1/fontconfig/fontconfig.h
@@ -128,7 +128,8 @@ typedef int		FcBool;
 #define FC_USER_CACHE_FILE	    ".fonts.cache-" FC_CACHE_VERSION

 /* Adjust outline rasterizer */
-#define FC_CHAR_WIDTH	    "charwidth"	/* Int */
+#define FC_CHARWIDTH	    "charwidth"	/* Int */
+#define FC_CHAR_WIDTH	    FC_CHARWIDTH
 #define FC_CHAR_HEIGHT	    "charheight"/* Int */
 #define FC_MATRIX	    "matrix"    /* FcMatrix */

Index: fontconfig-2.12.1/src/fcobjs.h
===================================================================
--- fontconfig-2.12.1.orig/src/fcobjs.h
+++ fontconfig-2.12.1/src/fcobjs.h
@@ -51,7 +51,7 @@ FC_OBJECT (DPI,			FcTypeDouble,	NULL)
 FC_OBJECT (RGBA,		FcTypeInteger,	NULL)
 FC_OBJECT (SCALE,		FcTypeDouble,	NULL)
 FC_OBJECT (MINSPACE,		FcTypeBool,	NULL)
-FC_OBJECT (CHAR_WIDTH,		FcTypeInteger,	NULL)
+FC_OBJECT (CHARWIDTH,		FcTypeInteger,	NULL)
 FC_OBJECT (CHAR_HEIGHT,		FcTypeInteger,	NULL)
 FC_OBJECT (MATRIX,		FcTypeMatrix,	NULL)
 FC_OBJECT (CHARSET,		FcTypeCharSet,	FcCompareCharSet)
Index: fontconfig-2.12.1/src/fcobjshash.gperf
===================================================================
--- fontconfig-2.12.1.orig/src/fcobjshash.gperf
+++ fontconfig-2.12.1/src/fcobjshash.gperf
@@ -44,7 +44,7 @@ int id;
 "rgba",FC_RGBA_OBJECT
 "scale",FC_SCALE_OBJECT
 "minspace",FC_MINSPACE_OBJECT
-"charwidth",FC_CHAR_WIDTH_OBJECT
+"charwidth",FC_CHARWIDTH_OBJECT
 "charheight",FC_CHAR_HEIGHT_OBJECT
 "matrix",FC_MATRIX_OBJECT
 "charset",FC_CHARSET_OBJECT
Index: fontconfig-2.12.1/src/fcobjshash.h
===================================================================
--- fontconfig-2.12.1.orig/src/fcobjshash.h
+++ fontconfig-2.12.1/src/fcobjshash.h
@@ -284,7 +284,7 @@ FcObjectTypeLookup (register const char
       {(int)(long)&((struct FcObjectTypeNamePool_t *)0)->FcObjectTypeNamePool_str43,FC_CHARSET_OBJECT},
       {-1},
 #line 47 "fcobjshash.gperf"
-      {(int)(long)&((struct FcObjectTypeNamePool_t *)0)->FcObjectTypeNamePool_str45,FC_CHAR_WIDTH_OBJECT},
+      {(int)(long)&((struct FcObjectTypeNamePool_t *)0)->FcObjectTypeNamePool_str45,FC_CHARWIDTH_OBJECT},
 #line 48 "fcobjshash.gperf"
       {(int)(long)&((struct FcObjectTypeNamePool_t *)0)->FcObjectTypeNamePool_str46,FC_CHAR_HEIGHT_OBJECT},
 #line 55 "fcobjshash.gperf"
'''
        self.apply_patch(self.directory, text)
