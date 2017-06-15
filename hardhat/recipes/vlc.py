import os
from .base import GnuRecipe
from ..util import patch


class VlcRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(VlcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c403d3accd9a400eb2181c958f3e7bc5' \
                      '524fe5738425f4253d42883b425a42a8'

        self.name = 'vlc'
        self.version = '2.2.6'
        self.depends = [
            'alsa-lib',
            'dbus',
            'ffmpeg',
            'flac',
            'fontconfig',
            'fribidi',
            'freetype',
            'liba52',
            'libass',
            'libdvdcss',
            'libgcrypt',
            'libmad',
            'libnotify',
            'libogg',
            'librsvg',
            'libtheora',
            'libvorbis',
            'libxml2',
            'pulseaudio',
            'qt5',
            'xorg-libs'
            ]
        self.url = 'http://get.videolan.org/vlc/$version/vlc-$version.tar.xz'
        self.compile_args += ['V=1']  # verbose
        self.environment['CFLAGS'] += ' -DLUA_COMPAT_5_1'
        self.configure_args += [
            '--disable-atmo',
            '--disable-silent-rules',
            '--enable-opencv=no',
            '--with-kde-solid=%s/share/kde4/apps/solid/actions']
        self.configure_strip_cross_compile()

    def configure(self):
        super(VlcRecipe, self).configure()
        self.log_dir('configure', self.directory, 'add vlccore linking')

        src = 'vlc_LDADD = ../lib/libvlc.la'
        dst = 'vlc_LDADD = ../lib/libvlc.la ../src/libvlccore.la'
        filename = os.path.join(self.directory, 'bin', 'Makefile')
        patch(filename, src, dst)

        src = '	../lib/libvlc.la'
        dst = '	../lib/libvlc.la ../src/libvlccore.la'
        patch(filename, src, dst)

    def patch(self):
        text = r'''
Submitted By:            Armin K <krejzi au email do com>
Date:                    2016-05-06
Initial Package Version: 2.2.3
Upstream Status:         Committed
Origin:                  Upstream
Description:             Fixes building against ffmpeg3
                         Rediffed for version 2.2.3 by Bruce Dubbs

diff -Naur vlc-2.2.3.orig/configure vlc-2.2.3/configure
--- vlc-2.2.3.orig/configure	2016-04-04 19:45:51.000000000 -0500
+++ vlc-2.2.3/configure	2016-05-06 22:39:24.859030920 -0500
@@ -36549,7 +36549,7 @@

     if test -n "$PKG_CONFIG" && \
     { { $as_echo "$as_me:${as_lineno-$LINENO}: \$PKG_CONFIG --exists --print-errors \"libavutil < 55\""; } >&5
-  ($PKG_CONFIG --exists --print-errors "libavutil < 55") 2>&5
+  ($PKG_CONFIG --exists --print-errors "libavutil > 55") 2>&5
   ac_status=$?
   $as_echo "$as_me:${as_lineno-$LINENO}: \$? = $ac_status" >&5
   test $ac_status = 0; }; then
@@ -36843,7 +36843,7 @@
     ffmpeg)
       if test -n "$PKG_CONFIG" && \
     { { $as_echo "$as_me:${as_lineno-$LINENO}: \$PKG_CONFIG --exists --print-errors \"libavcodec >= 57.10.100\""; } >&5
-  ($PKG_CONFIG --exists --print-errors "libavcodec >= 57.10.100") 2>&5
+  ($PKG_CONFIG --exists --print-errors "libavcodec >= 60.10.100") 2>&5
   ac_status=$?
   $as_echo "$as_me:${as_lineno-$LINENO}: \$? = $ac_status" >&5
   test $ac_status = 0; }; then
@@ -36927,7 +36927,7 @@
       ffmpeg)
         if test -n "$PKG_CONFIG" && \
     { { $as_echo "$as_me:${as_lineno-$LINENO}: \$PKG_CONFIG --exists --print-errors \"libavcodec >= 57.10.100\""; } >&5
-  ($PKG_CONFIG --exists --print-errors "libavcodec >= 57.10.100") 2>&5
+  ($PKG_CONFIG --exists --print-errors "libavcodec >= 60.10.100") 2>&5
   ac_status=$?
   $as_echo "$as_me:${as_lineno-$LINENO}: \$? = $ac_status" >&5
   test $ac_status = 0; }; then
@@ -45119,7 +45119,7 @@
     ffmpeg) av_vdpau_ver="55.42.100"
       if test -n "$PKG_CONFIG" && \
     { { $as_echo "$as_me:${as_lineno-$LINENO}: \$PKG_CONFIG --exists --print-errors \"libavcodec >= 57.10.100\""; } >&5
-  ($PKG_CONFIG --exists --print-errors "libavcodec >= 57.10.100") 2>&5
+  ($PKG_CONFIG --exists --print-errors "libavcodec >= 60.10.100") 2>&5
   ac_status=$?
   $as_echo "$as_me:${as_lineno-$LINENO}: \$? = $ac_status" >&5
   test $ac_status = 0; }; then
diff -Naur vlc-2.2.3.orig/modules/codec/avcodec/audio.c vlc-2.2.3/modules/codec/avcodec/audio.c
--- vlc-2.2.3.orig/modules/codec/avcodec/audio.c	2015-12-08 10:18:56.000000000 -0600
+++ vlc-2.2.3/modules/codec/avcodec/audio.c	2016-05-06 22:39:24.859030920 -0500
@@ -36,12 +36,11 @@
 #include <vlc_codec.h>
 #include <vlc_avcodec.h>

+#include "avcodec.h"
+
 #include <libavcodec/avcodec.h>
 #include <libavutil/mem.h>

-#include <libavutil/audioconvert.h>
-
-#include "avcodec.h"

 /*****************************************************************************
  * decoder_sys_t : decoder descriptor
diff -Naur vlc-2.2.3.orig/modules/codec/avcodec/avcommon_compat.h vlc-2.2.3/modules/codec/avcodec/avcommon_compat.h
--- vlc-2.2.3.orig/modules/codec/avcodec/avcommon_compat.h	2015-03-01 08:07:35.000000000 -0600
+++ vlc-2.2.3/modules/codec/avcodec/avcommon_compat.h	2016-05-06 22:39:24.859030920 -0500
@@ -506,6 +506,15 @@

 #endif /* HAVE_LIBAVUTIL_AVUTIL_H */

+#if LIBAVUTIL_VERSION_MAJOR >= 55
+# define FF_API_AUDIOCONVERT 1
+#endif
+
+/* libavutil/pixfmt.h */
+#ifndef PixelFormat
+# define PixelFormat AVPixelFormat
+#endif
+
 #ifdef HAVE_LIBAVFORMAT_AVFORMAT_H
 # include <libavformat/avformat.h>

diff -Naur vlc-2.2.3.orig/modules/codec/avcodec/encoder.c vlc-2.2.3/modules/codec/avcodec/encoder.c
--- vlc-2.2.3.orig/modules/codec/avcodec/encoder.c	2015-10-21 11:36:45.000000000 -0500
+++ vlc-2.2.3/modules/codec/avcodec/encoder.c	2016-05-06 22:39:24.860030887 -0500
@@ -41,7 +41,6 @@
 #include <vlc_cpu.h>

 #include <libavcodec/avcodec.h>
-#include <libavutil/audioconvert.h>

 #include "avcodec.h"
 #include "avcommon.h"
@@ -311,7 +310,7 @@
     else if( !GetFfmpegCodec( p_enc->fmt_out.i_codec, &i_cat, &i_codec_id,
                              &psz_namecodec ) )
     {
-        if( FindFfmpegChroma( p_enc->fmt_out.i_codec ) == PIX_FMT_NONE )
+        if( FindFfmpegChroma( p_enc->fmt_out.i_codec ) == AV_PIX_FMT_NONE )
             return VLC_EGENERIC; /* handed chroma output */

         i_cat      = VIDEO_ES;
@@ -1017,7 +1016,7 @@
         }
     }

-    p_sys->frame = avcodec_alloc_frame();
+    p_sys->frame = av_frame_alloc();
     if( !p_sys->frame )
     {
         goto error;
@@ -1088,7 +1087,8 @@
     AVFrame *frame = NULL;
     if( likely(p_pict) ) {
         frame = p_sys->frame;
-        avcodec_get_frame_defaults( frame );
+        av_frame_unref( frame );
+
         for( i_plane = 0; i_plane < p_pict->i_planes; i_plane++ )
         {
             p_sys->frame->data[i_plane] = p_pict->p[i_plane].p_pixels;
@@ -1329,7 +1329,7 @@
     //How much we need to copy from new packet
     const int leftover = leftover_samples * p_sys->p_context->channels * p_sys->i_sample_bytes;

-    avcodec_get_frame_defaults( p_sys->frame );
+    av_frame_unref( p_sys->frame );
     p_sys->frame->format     = p_sys->p_context->sample_fmt;
     p_sys->frame->nb_samples = leftover_samples + p_sys->i_samples_delay;

@@ -1451,7 +1451,8 @@
     while( ( p_aout_buf->i_nb_samples >= p_sys->i_frame_size ) ||
            ( p_sys->b_variable && p_aout_buf->i_nb_samples ) )
     {
-        avcodec_get_frame_defaults( p_sys->frame );
+        av_frame_unref( p_sys->frame );
+
         if( p_sys->b_variable )
             p_sys->frame->nb_samples = p_aout_buf->i_nb_samples;
         else
diff -Naur vlc-2.2.3.orig/modules/codec/avcodec/vaapi.c vlc-2.2.3/modules/codec/avcodec/vaapi.c
--- vlc-2.2.3.orig/modules/codec/avcodec/vaapi.c	2014-11-16 12:57:58.000000000 -0600
+++ vlc-2.2.3/modules/codec/avcodec/vaapi.c	2016-05-06 22:39:24.860030887 -0500
@@ -595,7 +595,7 @@
         return err;

     /* Only VLD supported */
-    p_va->pix_fmt = PIX_FMT_VAAPI_VLD;
+    p_va->pix_fmt = AV_PIX_FMT_VAAPI_VLD;
     p_va->setup = Setup;
     p_va->get = Get;
     p_va->release = Release;
diff -Naur vlc-2.2.3.orig/modules/codec/avcodec/video.c vlc-2.2.3/modules/codec/avcodec/video.c
--- vlc-2.2.3.orig/modules/codec/avcodec/video.c	2016-04-04 19:45:24.000000000 -0500
+++ vlc-2.2.3/modules/codec/avcodec/video.c	2016-05-06 22:39:24.860030887 -0500
@@ -234,7 +234,7 @@
     p_sys->p_codec = p_codec;
     p_sys->i_codec_id = i_codec_id;
     p_sys->psz_namecodec = psz_namecodec;
-    p_sys->p_ff_pic = avcodec_alloc_frame();
+    p_sys->p_ff_pic = av_frame_alloc();
     p_sys->b_delayed_open = true;
     p_sys->p_va = NULL;
     vlc_sem_init( &p_sys->sem_mt, 0 );
@@ -446,7 +446,7 @@
     if( ffmpeg_OpenCodec( p_dec ) < 0 )
     {
         msg_Err( p_dec, "cannot open codec (%s)", p_sys->psz_namecodec );
-        avcodec_free_frame( &p_sys->p_ff_pic );
+        av_frame_free( &p_sys->p_ff_pic );
         vlc_sem_destroy( &p_sys->sem_mt );
         free( p_sys );
         return VLC_EGENERIC;
@@ -826,7 +826,7 @@
     wait_mt( p_sys );

     if( p_sys->p_ff_pic )
-        avcodec_free_frame( &p_sys->p_ff_pic );
+        av_frame_free( &p_sys->p_ff_pic );

     if( p_sys->p_va )
         vlc_va_Delete( p_sys->p_va );
'''

        self.apply_patch(self.directory, text)

        self.log_dir('patch', self.directory, 'remove implicit function error')
        script = r"""sed -i 's/error-implicit-function-declaration//' configure"""
        filename = os.path.join(self.directory, 'init.sh')
        with open(filename, 'wt') as f:
            f.write(script)

        self.run_exe(self.shell_args + [filename],
                     self.directory, self.environment)
