import os
import shutil
from .base import GnuRecipe


class MuPdfRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MuPdfRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '209474a80c56a035ce3f4958a63373a9' \
                      '6fad75c927c7b1acdc553fc85855f00a'

        self.name = 'mupdf'
        self.version = '1.11'
        self.depends = ['harfbuzz', 'libjpeg-turbo', 'openjpeg', 'curl',
                        'xorg-libs']
        self.url = 'http://www.mupdf.com/downloads/archive/' \
                   'mupdf-$version-source.tar.gz'
        self.install_args = [
            ['make',
             'prefix=%s' % self.prefix_dir,
             'build=release',
             'docdir=%s/share/doc/mupdf' % self.prefix_dir,
             'install'],
            ['ln', '-sfv', 'mupdf-x11-curl', '%s/mupdf' % self.prefix_dir]]



    def configure(self):
        pass

    def compile(self):
        pass

    def patch(self):
        self.log_dir('patch', self.directory, 'shared libs')
        text = r'''
Submitted By: Pierre Labastie <pierre dot labastie at neuf dot fr>
Date: 2016-11-27
Initial Package Version: 1.10
Upstream Status: N/A
Origin: Armin K and Gentoo
Description: Generate shared libraries for mupdf, instead of static ones. This
             allows to have the font information (around 35 MB) at one place
             only, instead of in all the executables.
Update: Bruce Dubbs 2017/07/15.  Changes to include new threads library.

diff -Naur mupdf-1.11-source.orig/Makefile mupdf-1.11-source/Makefile
--- mupdf-1.11-source.orig/Makefile	2017-04-05 06:02:21.000000000 -0500
+++ mupdf-1.11-source/Makefile	2017-04-15 18:26:46.286239623 -0500
@@ -14,7 +14,7 @@
 # Do not specify CFLAGS or LIBS on the make invocation line - specify
 # XCFLAGS or XLIBS instead. Make ignores any lines in the makefile that
 # set a variable that was set on the command line.
-CFLAGS += $(XCFLAGS) -Iinclude -Igenerated
+CFLAGS += $(XCFLAGS) -Iinclude -Igenerated -fPIC
 LIBS += $(XLIBS) -lm

 LIBS += $(FREETYPE_LIBS)
@@ -300,19 +300,22 @@

 # --- Library ---

-MUPDF_LIB = $(OUT)/libmupdf.a
-THIRD_LIB = $(OUT)/libmupdfthird.a
-THREAD_LIB = $(OUT)/libmuthreads.a
+MUPDF_LIB = $(OUT)/libmupdf.so
+THIRD_LIB = $(OUT)/libmupdfthird.so
+THREAD_LIB = $(OUT)/libmuthreads.so

 MUPDF_OBJ := $(FITZ_OBJ) $(FONT_OBJ) $(PDF_OBJ) $(XPS_OBJ) $(SVG_OBJ) $(CBZ_OBJ) $(HTML_OBJ) $(GPRF_OBJ)
 THIRD_OBJ := $(FREETYPE_OBJ) $(HARFBUZZ_OBJ) $(JBIG2DEC_OBJ) $(LIBJPEG_OBJ) $(JPEGXR_OBJ) $(LURATECH_OBJ) $(MUJS_OBJ) $(OPENJPEG_OBJ) $(ZLIB_OBJ)
 THREAD_OBJ := $(THREAD_OBJ)

-$(MUPDF_LIB) : $(MUPDF_OBJ)
+$(MUPDF_LIB) : $(MUPDF_OBJ) $(THIRD_LIB) $(THREAD_LIB)
+	$(LINK_CMD) -shared -Wl,-soname -Wl,libmupdf.so -Wl,--no-undefined
 $(THIRD_LIB) : $(THIRD_OBJ)
+	$(LINK_CMD) -shared -Wl,-soname -Wl,libmupdfthird.so -Wl,--no-undefined
 $(THREAD_LIB) : $(THREAD_OBJ)
+	$(LINK_CMD) -shared -Wl,-soname -Wl,libmuthreads.so -Wl,--no-undefined -lpthread

-INSTALL_LIBS := $(MUPDF_LIB) $(THIRD_LIB)
+INSTALL_LIBS := $(MUPDF_LIB) $(THIRD_LIB) $(THREAD_LIB)

 # --- Tools and Apps ---

'''
        self.apply_patch(self.directory, text)

        self.log_dir('patch', self.directory, 'openjpeg')
        text = r'''
Submitted By: Bruce Dubbs <bdubbs at linuxfromscratch dot org>
Date: 2016-11-27
Initial Package Version: 1.11
Upstream Status: Not submitted
Origin: Arch Linux
Description: Fixes for openjpeg-2.1

diff --git a/source/fitz/load-jpx.c b/source/fitz/load-jpx.c
index d01de58..6ca3838 100644
--- a/source/fitz/load-jpx.c
+++ b/source/fitz/load-jpx.c
@@ -444,14 +444,18 @@ fz_load_jpx_info(fz_context *ctx, unsigned char *data, size_t size, int *wp, int

 #else /* HAVE_LURATECH */

+#ifdef __cplusplus
+extern "C"
+{
 #define OPJ_STATIC
 #define OPJ_HAVE_INTTYPES_H
 #if !defined(_WIN32) && !defined(_WIN64)
 #define OPJ_HAVE_STDINT_H
 #endif
+#endif
 #define USE_JPIP

-#include <openjpeg.h>
+#include <openjpeg-2.1/openjpeg.h>

 struct fz_jpxd_s
 {
@@ -919,6 +923,10 @@ fz_load_jpx_info(fz_context *ctx, unsigned char *data, size_t size, int *wp, int
 	*yresp = state.yres;
 }

+#ifdef __cplusplus
+}
+#endif
+
 #endif /* HAVE_LURATECH */

 #else /* FZ_ENABLE_JPX */
'''
        self.apply_patch(self.directory, text)

        self.log_dir('patch', self.directory, 'remove 3rd party')
        for dir in ['curl', 'freetype', 'harfbuzz',
                    'libjpeg', 'openjpeg', 'zlib']:
            shutil.rmtree(os.path.join(self.directory, 'thirdparty', dir))
