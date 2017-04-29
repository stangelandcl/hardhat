from .base import GnuRecipe


class ChromiumRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ChromiumRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '70011770a7e522c92826a3af48d3fd28' \
                      'a46bf8042897d072d20c748cbf828cf7'


        self.name = 'chromium'
        self.version = '57.0.2987.133'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+\.\d+)'
        self.depends = [
            'alsa-lib',
            'cups',
            'desktop-file-utils',
            'dbus',
            'flac',
            'ffmpeg',
            'gconf',
            'gtk2',
            'hicolor-icon-theme',
            'icu',
            'libevent',
            'libexif',
            'libjpeg-turbo',
            'libpng',
            'libsecret',
            'libvpx',
            'libwebp',
            'libxml2',
            'mit-kerberos',
            'mesa',
            'ninja',
            'nss',
            'pciutils',
            'perl5-file-basedir',
            'python2',
            'snappy',
            'usbutils',
            'xorg-libs',
            'yasm',
        ]
        self.url = 'https://commondatastorage.googleapis.com/' \
                   'chromium-browser-official/chromium-$version.tar.xz'

        self.compile_args = [
            'ninja', '-C', '-out/Release',
            'chrome', 'chrome_sandbox', 'chromedriver', 'widevinecdmadapter'
            ]

    def patch(self):
        text = r'''
Submitted By:            DJ Lucas <dj_AT_linuxfromscratch_DOT_org>
Date:                    2017-03-18
Initial Package Version: 57.0.2987.110
Upstream Status:         Not submitted
Origin:                  Gentoo: https://gitweb.gentoo.org/repo/gentoo.git/plain/www-client/chromium/files/chromium-system-ffmpeg-r4.patch
Description:             Allows building with system provided ffmpeg.


--- a/media/ffmpeg/ffmpeg_common.h.orig	2016-09-09 13:16:07.757294768 +0000
+++ b/media/ffmpeg/ffmpeg_common.h	2016-09-09 13:16:41.705989273 +0000
@@ -22,10 +22,6 @@

 // Include FFmpeg header files.
 extern "C" {
-// Disable deprecated features which result in spammy compile warnings.  This
-// list of defines must mirror those in the 'defines' section of FFmpeg's
-// BUILD.gn file or the headers below will generate different structures!
-#define FF_API_CONVERGENCE_DURATION 0
 // Upstream libavcodec/utils.c still uses the deprecated
 // av_dup_packet(), causing deprecation warnings.
 // The normal fix for such things is to disable the feature as below,
@@ -35,7 +35,6 @@
 MSVC_PUSH_DISABLE_WARNING(4244);
 #include <libavcodec/avcodec.h>
 #include <libavformat/avformat.h>
-#include <libavformat/internal.h>
 #include <libavformat/avio.h>
 #include <libavutil/avutil.h>
 #include <libavutil/imgutils.h>
--- a/media/filters/ffmpeg_demuxer.cc.orig	2016-09-09 14:21:40.185828912 +0000
+++ b/media/filters/ffmpeg_demuxer.cc	2016-09-09 14:21:52.894089352 +0000
@@ -1185,24 +1185,6 @@
   // If no estimate is found, the stream entry will be kInfiniteDuration.
   std::vector<base::TimeDelta> start_time_estimates(format_context->nb_streams,
                                                     kInfiniteDuration);
-  const AVFormatInternal* internal = format_context->internal;
-  if (internal && internal->packet_buffer &&
-      format_context->start_time != static_cast<int64_t>(AV_NOPTS_VALUE)) {
-    struct AVPacketList* packet_buffer = internal->packet_buffer;
-    while (packet_buffer != internal->packet_buffer_end) {
-      DCHECK_LT(static_cast<size_t>(packet_buffer->pkt.stream_index),
-                start_time_estimates.size());
-      const AVStream* stream =
-          format_context->streams[packet_buffer->pkt.stream_index];
-      if (packet_buffer->pkt.pts != static_cast<int64_t>(AV_NOPTS_VALUE)) {
-        const base::TimeDelta packet_pts =
-            ConvertFromTimeBase(stream->time_base, packet_buffer->pkt.pts);
-        if (packet_pts < start_time_estimates[stream->index])
-          start_time_estimates[stream->index] = packet_pts;
-      }
-      packet_buffer = packet_buffer->next;
-    }
-  }

   std::unique_ptr<MediaTracks> media_tracks(new MediaTracks());
'''
        self.apply_patch(self.directory, text)

        self.log_dir('patch', self.directory, 'fix gcc 6 build')
        args = [
                'sed',
                r"""'s/^config("compiler") {/&\ncflags_cc = """
                r"""[ "-fno-delete-null-pointer-checks" ]/'""",
                '-i',
                'build/config/linux/BUILD.gn']
        self.run_exe(args, self.directory, self.environment)

        self.log_dir('patch', self.directory, 'enable widevine')
        args = [
            'sed',
            's/WIDEVINE_CDM_AVAILABLE/&\n\n#define '
            'WIDEVINE_CDM_VERSION_STRING "Pinkie Pie"/',
            '-i', 'third_party/widevine/cdm/stub/widevine_cdm_version.h'
            ]
        self.run_exe(args, self.directory, self.environment)

    def configure(self):
        self.log_dir('configure', self.directory, 'generating build files')
        text = r'''
GN_CONFIG=('google_api_key="AIzaSyDxKL42zsPjbke5O8_rPVpVrLrJ8aeE9rQ"'
'google_default_client_id="595013732528-llk8trb03f0ldpqq6nprjp1s79596646.apps.googleusercontent.com"'
'google_default_client_secret="5ntt6GbbkjnTVXx-MSxbmx5e"'
'clang_use_chrome_plugins=false'
'enable_hangout_services_extension=true'
'enable_nacl=false'
'enable_nacl_nonsfi=false'
'enable_widevine=true'
'fatal_linker_warnings=false'
'ffmpeg_branding="Chrome"'
'fieldtrial_testing_like_official_build=true'
'is_debug=false'
'is_clang=false'
'link_pulseaudio=true'
'linux_use_bundled_binutils=false'
'proprietary_codecs=true'
'remove_webcore_debug_symbols=true'
'symbol_level=0'
'treat_warnings_as_errors=false'
'use_allocator="none"'
'use_cups=true'
'use_gconf=false'
'use_gnome_keyring=false'
'use_gold=false'
'use_gtk3=false'
'use_kerberos=true'
'use_pulseaudio=true'
'use_sysroot=false') \
\
python tools/gn/bootstrap/bootstrap.py --gn-gen-Args "${GN_CONFIG[*]}" && \
out/Release/gn gen out/Release --args="${GN_CONFIG[*]}"
'''

        args = self.shell_args + [text]
        self.run_exe(args, self.directory, self.environment)

    def install(self):
        text = r'''
install -vDm755  out/Release/chrome \
                 $prefix/lib/chromium/chromium                   &&
install -vDm4755 out/Release/chrome_sandbox \
                 $prefix/lib/chromium/chrome-sandbox             &&
install -vDm755  out/Release/chromedriver \
                 $prefix/lib/chromium/chromedriver               &&
ln -svf $prefix/lib/chromium/chromium /usr/bin                   &&
ln -svf $prefix/lib/chromium/chromedriver /usr/bin/              &&

install -vDm644 out/Release/gen/content/content_resources.pak \
                $prefix/lib/chromium/                            &&
install -vm644 out/Release/{*.pak,*.bin} \
               $prefix/lib/chromium/                             &&

cp -av out/Release/locales $prefix/lib/chromium/ &&

install -vDm644 out/Release/chrome.1 \
                $prefix/share/man/man1/chromium.1
'''
        text = text.replace('$prefix', self.prefix_dir)
        self.run_exe(self.shell_args + [text],
                     self.directory,
                     self.environment)
