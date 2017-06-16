import os
import stat
from .base import GnuRecipe
from ..util import patch


class Extra:
    def __init__(self, name):
        self.name = name
        self.sha256 = None


class ChromiumRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ChromiumRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f24cef3dd2acf9dd5ccdeeca47fea42d' \
                      '1c1ddff32b7375dc9e0cd35a4e8d78ff'

        self.name = 'chromium'
        self.version = '58.0.3029.110'
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
            'p11-kit',
            'python2',
            'snappy',
            'usbutils',
            'xorg-libs',
            'yasm',
        ]
        self.url = 'https://commondatastorage.googleapis.com/' \
                   'chromium-browser-official/chromium-$version.tar.xz'

        self.compile_args = [
            'ninja', '-C', 'out/Release',
            'chrome', 'chrome_sandbox', 'chromedriver', 'widevinecdmadapter'
            ]
        self.environment['CPPFLAGS'] += ' -I%s/include/nss' % self.prefix_dir
        self.environment['CXXFLAGS'] += ' -I%s/include/nss' % self.prefix_dir
        self.environment['CFLAGS'] += ' -I%s/include/nss' % self.prefix_dir

        self.widevine = Extra('widevine')
        self.widevine.url = 'http://dl.google.com/linux/chrome/deb/pool/main' \
                            '/g/google-chrome-stable/' \
                            'google-chrome-stable_%s-1_amd64.deb' \
                            % self.version
        self.widevine.version = self.version
        self.widevine.sha256 = '2d1eed9be2687c0b393699381d1a93bf' \
                               '8913a50eaf8df6b4596e3bfc4b15dd6d'
        self.extra_downloads.append(self.widevine)


    def patch(self):
        self.log_dir('patch', self.directory, 'fix gcc 7 build')
        text = r'''
Submitted By:            DJ Lucas <dj_AT_linuxfromscratch_DOT_org>
Date:                    2017-05-26
Initial Package Version: 58.0.3029.110
Upstream Status:         Committed
Origin:                  Upstream
Description:             Allows building with GCC-7.1.0.

diff -Naurp chromium-58.0.3029.110-orig/v8/src/objects-body-descriptors.h chromium-58.0.3029.110/v8/src/objects-body-descriptors.h
--- chromium-58.0.3029.110-orig/v8/src/objects-body-descriptors.h	2017-05-25 01:00:35.919340167 -0500
+++ chromium-58.0.3029.110/v8/src/objects-body-descriptors.h	2017-05-25 01:02:02.896748350 -0500
@@ -99,7 +99,7 @@ class FixedBodyDescriptor final : public

   template <typename StaticVisitor>
   static inline void IterateBody(HeapObject* obj, int object_size) {
-    IterateBody(obj);
+    IterateBody<StaticVisitor>(obj);
   }
 };

diff -Naurp chromium-58.0.3029.110-orig/v8/src/objects-inl.h chromium-58.0.3029.110/v8/src/objects-inl.h
--- chromium-58.0.3029.110-orig/v8/src/objects-inl.h	2017-05-25 01:00:35.926006896 -0500
+++ chromium-58.0.3029.110/v8/src/objects-inl.h	2017-05-25 01:05:22.191293156 -0500
@@ -43,6 +43,25 @@
 namespace v8 {
 namespace internal {

+template <typename Derived, typename Shape, typename Key>
+uint32_t HashTable<Derived, Shape, Key>::Hash(Key key) {
+  if (Shape::UsesSeed) {
+    return Shape::SeededHash(key, GetHeap()->HashSeed());
+  } else {
+    return Shape::Hash(key);
+  }
+}
+
+template <typename Derived, typename Shape, typename Key>
+uint32_t HashTable<Derived, Shape, Key>::HashForObject(Key key,
+                                                       Object* object) {
+  if (Shape::UsesSeed) {
+    return Shape::SeededHashForObject(key, GetHeap()->HashSeed(), object);
+  } else {
+    return Shape::HashForObject(key, object);
+  }
+}
+
 PropertyDetails::PropertyDetails(Smi* smi) {
   value_ = smi->value();
 }
diff -Naurp chromium-58.0.3029.110-orig/v8/src/objects.h chromium-58.0.3029.110/v8/src/objects.h
--- chromium-58.0.3029.110-orig/v8/src/objects.h	2017-05-25 01:00:35.919340167 -0500
+++ chromium-58.0.3029.110/v8/src/objects.h	2017-05-25 01:04:20.824315766 -0500
@@ -3358,22 +3358,10 @@ class HashTable : public HashTableBase {
  public:
   typedef Shape ShapeT;

-  // Wrapper methods
-  inline uint32_t Hash(Key key) {
-    if (Shape::UsesSeed) {
-      return Shape::SeededHash(key, GetHeap()->HashSeed());
-    } else {
-      return Shape::Hash(key);
-    }
-  }
-
-  inline uint32_t HashForObject(Key key, Object* object) {
-    if (Shape::UsesSeed) {
-      return Shape::SeededHashForObject(key, GetHeap()->HashSeed(), object);
-    } else {
-      return Shape::HashForObject(key, object);
-    }
-  }
+  // Wrapper methods.  Defined in src/objects-inl.h
+  // to break a cycle with src/heap/heap.h.
+  inline uint32_t Hash(Key key);
+  inline uint32_t HashForObject(Key key, Object* object);

   // Returns a new HashTable object.
   MUST_USE_RESULT static Handle<Derived> New(
diff -Naurp chromium-58.0.3029.110-orig/third_party/WebKit/Source/wtf/LinkedHashSet.h chromium-58.0.3029.110/third_party/WebKit/Source/wtf/LinkedHashSet.h
--- chromium-58.0.3029.110-orig/third_party/WebKit/Source/wtf/LinkedHashSet.h	2017-05-25 01:00:47.959451969 -0500
+++ chromium-58.0.3029.110/third_party/WebKit/Source/wtf/LinkedHashSet.h	2017-05-25 01:11:08.915644292 -0500
@@ -687,6 +687,8 @@ inline LinkedHashSet<T, U, V, W>& Linked
   return *this;
 }

+inline void swapAnchor(LinkedHashSetNodeBase& a, LinkedHashSetNodeBase& b);
+
 template <typename T, typename U, typename V, typename W>
 inline void LinkedHashSet<T, U, V, W>::swap(LinkedHashSet& other) {
   m_impl.swap(other.m_impl);
diff -Naurp chromium-58.0.3029.110-orig/third_party/WebKit/Source/platform/graphics/gpu/SharedGpuContext.h chromium-58.0.3029.110/third_party/WebKit/Source/platform/graphics/gpu/SharedGpuContext.h
--- chromium-58.0.3029.110-orig/third_party/WebKit/Source/platform/graphics/gpu/SharedGpuContext.h	2017-05-25 01:00:47.909451510 -0500
+++ chromium-58.0.3029.110/third_party/WebKit/Source/platform/graphics/gpu/SharedGpuContext.h	2017-05-25 19:12:53.217370518 -0500
@@ -5,6 +5,7 @@
 #include "platform/PlatformExport.h"
 #include "wtf/ThreadSpecific.h"

+#include <functional>
 #include <memory>

 namespace gpu {
'''

        self.apply_patch(self.directory, text)

     ##    self.log_dir('patch', self.directory, 'use system ffmpeg')
##         text = r'''
## Submitted By:            DJ Lucas <dj_AT_linuxfromscratch_DOT_org>
## Date:                    2017-03-18
## Initial Package Version: 57.0.2987.110
## Upstream Status:         Not submitted
## Origin:                  Gentoo: https://gitweb.gentoo.org/repo/gentoo.git/plain/www-client/chromium/files/chromium-system-ffmpeg-r4.patch
## Description:             Allows building with system provided ffmpeg.


## --- a/media/ffmpeg/ffmpeg_common.h.orig	2016-09-09 13:16:07.757294768 +0000
## +++ b/media/ffmpeg/ffmpeg_common.h	2016-09-09 13:16:41.705989273 +0000
## @@ -22,10 +22,6 @@

##  // Include FFmpeg header files.
##  extern "C" {
## -// Disable deprecated features which result in spammy compile warnings.  This
## -// list of defines must mirror those in the 'defines' section of FFmpeg's
## -// BUILD.gn file or the headers below will generate different structures!
## -#define FF_API_CONVERGENCE_DURATION 0
##  // Upstream libavcodec/utils.c still uses the deprecated
##  // av_dup_packet(), causing deprecation warnings.
##  // The normal fix for such things is to disable the feature as below,
## @@ -35,7 +35,6 @@
##  MSVC_PUSH_DISABLE_WARNING(4244);
##  #include <libavcodec/avcodec.h>
##  #include <libavformat/avformat.h>
## -#include <libavformat/internal.h>
##  #include <libavformat/avio.h>
##  #include <libavutil/avutil.h>
##  #include <libavutil/imgutils.h>
## --- a/media/filters/ffmpeg_demuxer.cc.orig	2016-09-09 14:21:40.185828912 +0000
## +++ b/media/filters/ffmpeg_demuxer.cc	2016-09-09 14:21:52.894089352 +0000
## @@ -1185,24 +1185,6 @@
##    // If no estimate is found, the stream entry will be kInfiniteDuration.
##    std::vector<base::TimeDelta> start_time_estimates(format_context->nb_streams,
##                                                      kInfiniteDuration);
## -  const AVFormatInternal* internal = format_context->internal;
## -  if (internal && internal->packet_buffer &&
## -      format_context->start_time != static_cast<int64_t>(AV_NOPTS_VALUE)) {
## -    struct AVPacketList* packet_buffer = internal->packet_buffer;
## -    while (packet_buffer != internal->packet_buffer_end) {
## -      DCHECK_LT(static_cast<size_t>(packet_buffer->pkt.stream_index),
## -                start_time_estimates.size());
## -      const AVStream* stream =
## -          format_context->streams[packet_buffer->pkt.stream_index];
## -      if (packet_buffer->pkt.pts != static_cast<int64_t>(AV_NOPTS_VALUE)) {
## -        const base::TimeDelta packet_pts =
## -            ConvertFromTimeBase(stream->time_base, packet_buffer->pkt.pts);
## -        if (packet_pts < start_time_estimates[stream->index])
## -          start_time_estimates[stream->index] = packet_pts;
## -      }
## -      packet_buffer = packet_buffer->next;
## -    }
## -  }

##    std::unique_ptr<MediaTracks> media_tracks(new MediaTracks());
## '''
##         self.apply_patch(self.directory, text)

        self.log_dir('patch', self.directory, 'fix gcc 6 build')
        args = [
                'sed',
                r"""'s/^config("compiler") {/&\ncflags_cc = """
                r"""[ "-fno-delete-null-pointer-checks" ]/'""",
                '-i',
                'build/config/linux/BUILD.gn']
        self.run_exe(args, self.directory, self.environment)

        self.log_dir('patch', self.directory, 'enable widevine')
        src = '#define WIDEVINE_CDM_AVAILABLE'
        dst = '#define WIDEVINE_CDM_AVAILABLE\n#define WIDEVINE_CDM_VERSION_STRING "Pinkie Pie"\n'
        filename = os.path.join(self.directory, 'third_party/widevine/cdm/stub/widevine_cdm_version.h')
        patch(filename, src, dst)

        self.log_dir('patch', self.directory, 'libaddressinput update')
        args = ['python',
                'third_party/libaddressinput/chromium/tools/update-strings.py']
        self.run_exe(args, self.directory, self.environment)

        self.log_dir('patch', self.directory, 'patch gn')
        src = "'base/callback_internal.cc',"
        dst = src + "\n      'base/callback_helpers.cc',"
        filename = os.path.join(self.directory,
                                'tools/gn/bootstrap/bootstrap.py')
        patch(filename, src, dst)

      ##   self.log_dir('patch', self.directory, 'setting which libraries are system')
##         script = r'''#!/bin/bash
## for LIB in ffmpeg flac harfbuzz-ng libevent libjpeg libjpeg_turbo libpng libwebp libxml libxslt yasm; do
##     find . -type f -path "*third_party/$LIB/*" ! -path "*third_party/$LIB/chromium/*" ! -path "*third_party/$LIB/google/*" ! -path "*base/third_party/libevent/*" ! -regex '.*\.(gn|gni|isolate|py)' -delete
## done

## python build/linux/unbundle/replace_gn_files.py --system-libraries ffmpeg flac harfbuzz-ng libevent libjpeg libpng libwebp libxml libxslt yasm

## python third_party/libaddressinput/chromium/tools/update-strings.py
## '''
##         filename = os.path.join(self.directory, 'set_libs.sh')
##         with open(filename, 'wt') as f:
##             f.write(script)

##         os.chmod(filename, stat.S_IRWXU)

##         self.run_exe(self.shell_args + [filename],
##                      self.directory, self.environment)

    def configure(self):
        self.log_dir('configure', self.directory, 'generating build files')

        script = r'''#!/bin/bash
python tools/gn/bootstrap/bootstrap.py --gn-gen-args '
    google_api_key="AIzaSyDxKL42zsPjbke5O8_rPVpVrLrJ8aeE9rQ"
    google_default_client_id="595013732528-llk8trb03f0ldpqq6nprjp1s79596646.apps.googleusercontent.com"
    google_default_client_secret="5ntt6GbbkjnTVXx-MSxbmx5e"
    use_sysroot=false
    use_gnome_keyring=false
    ffmpeg_branding="Chrome"
    is_clang=false
    treat_warnings_as_errors=false
    use_gold=false
    enable_hangout_services_extension=true
    enable_nacl=false
    enable_nacl_nonsfi=false
    use_cups=false
    use_gconf=false
    use_gtk3=false
    use_kerberos=true
    fatal_linker_warnings=false
    is_debug=false
    linux_use_bundled_binutils=false
    proprietary_codecs=true
    enable_widevine=true
    fieldtrial_testing_like_official_build=true
    remove_webcore_debug_symbols=true
    use_pulseaudio=false
'
out/Release/gn gen out/Release --args='
    google_api_key="AIzaSyDxKL42zsPjbke5O8_rPVpVrLrJ8aeE9rQ"
    google_default_client_id="595013732528-llk8trb03f0ldpqq6nprjp1s79596646.apps.googleusercontent.com"
    google_default_client_secret="5ntt6GbbkjnTVXx-MSxbmx5e"
    use_sysroot=false
    use_gnome_keyring=false
    ffmpeg_branding="Chrome"
    is_clang=false
    treat_warnings_as_errors=false
    use_gold=false
    enable_hangout_services_extension=true
    enable_nacl=false
    enable_nacl_nonsfi=false
    use_cups=false
    use_gconf=false
    use_gtk3=false
    use_kerberos=true
    fatal_linker_warnings=false
    is_debug=false
    linux_use_bundled_binutils=false
    proprietary_codecs=true
    enable_widevine=true
    fieldtrial_testing_like_official_build=true
    remove_webcore_debug_symbols=true
    use_pulseaudio=false
'
'''
        #clang_use_chrome_plugins=false

        exe = '/tmp/chromium_install.sh'
        with open(exe, 'wt') as f:
            f.write(script)

        args = ['/bin/bash', exe]
        self.log_dir('configure', self.directory, 'running configure')
        self.run_exe(args, self.directory, self.environment)

    def install(self):
        self.log_dir('install', self.directory, 'running install')
        text = r'''
prefix=%s
install -vDm755  out/Release/chrome \
                 $prefix/lib/chromium/chromium                   &&
install -vDm4755 out/Release/chrome_sandbox \
                 $prefix/lib/chromium/chrome-sandbox             &&
install -vDm755  out/Release/chromedriver \
                 $prefix/lib/chromium/chromedriver               &&
ln -svf $prefix/lib/chromium/chromium $prefix/bin                &&
ln -svf $prefix/lib/chromium/chromedriver $prefix/bin/           &&

install -vDm644 out/Release/gen/content/content_resources.pak \
                $prefix/lib/chromium/                            &&
install -vm644 out/Release/{*.pak,*.bin} \
               $prefix/lib/chromium/                             &&

cp -av out/Release/locales $prefix/lib/chromium/ &&

install -vDm644 out/Release/chrome.1 \
                $prefix/share/man/man1/chromium.1
''' % self.prefix_dir

        filename = os.path.join(self.directory, 'install.sh')
        with open(filename, 'wt') as f:
            f.write(filename)
        self.run_exe(['bash', 'install.sh'],
                     self.directory,
                     self.environment)
