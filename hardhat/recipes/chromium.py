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
        self.sha256 = '4135968cac6623c1d2b224494600cd27' \
                      '4098cce41c298f8c3908b354a34c281b'

        self.name = 'chromium'
        self.version = '61.0.3163.100'
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
            'nodejs',
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
            'chrome', 'chrome_sandbox', 'chromedriver', 'widevinecdmadapter',
            '-j%s' % self.cpu_count
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
        self.widevine.sha256 = '5b8b9655db8dcce4b276db7860ae1c8c' \
                               'e1079a33f161a716c17fda24b8d5a9b2'
        self.extra_downloads.append(self.widevine)

    def patch(self):
        self.log_dir('patch', self.directory, 'fix gcc 7 build')
        text = r'''
Submitted By:            DJ Lucas <dj_AT_linuxfromscratch_DOT_org>
Date:                    2017-10-13
Initial Package Version: 61.0.3163.100
Upstream Status:         Pending
Origin:                  upstream
Description:             Allows building with GCC-7.2.0.


diff -Naurp chromium-61.0.3163.100-orig/base/numerics/safe_math_shared_impl.h chromium-61.0.3163.100/base/numerics/safe_math_shared_impl.h
--- chromium-61.0.3163.100-orig/base/numerics/safe_math_shared_impl.h	2017-09-21 17:04:50.000000000 -0500
+++ chromium-61.0.3163.100/base/numerics/safe_math_shared_impl.h	2017-10-11 23:30:39.809656293 -0500
@@ -21,8 +21,7 @@
 #if !defined(__native_client__) &&                         \
     ((defined(__clang__) &&                                \
       ((__clang_major__ > 3) ||                            \
-       (__clang_major__ == 3 && __clang_minor__ >= 4))) || \
-     (defined(__GNUC__) && __GNUC__ >= 5))
+       (__clang_major__ == 3 && __clang_minor__ >= 4))))
 #include "base/numerics/safe_math_clang_gcc_impl.h"
 #define BASE_HAS_OPTIMIZED_SAFE_MATH (1)
 #else
diff -Naurp chromium-61.0.3163.100-orig/third_party/WebKit/Source/platform/graphics/gpu/SharedGpuContext.h chromium-61.0.3163.100/third_party/WebKit/Source/platform/graphics/gpu/SharedGpuContext.h
--- chromium-61.0.3163.100-orig/third_party/WebKit/Source/platform/graphics/gpu/SharedGpuContext.h	2017-09-21 17:05:18.000000000 -0500
+++ chromium-61.0.3163.100/third_party/WebKit/Source/platform/graphics/gpu/SharedGpuContext.h	2017-10-11 23:30:39.806323020 -0500
@@ -8,6 +8,7 @@
 #include "platform/PlatformExport.h"
 #include "platform/wtf/ThreadSpecific.h"

+#include <functional>
 #include <memory>

 namespace gpu {
diff -Naurp chromium-61.0.3163.100-orig/third_party/WebKit/Source/platform/wtf/LinkedHashSet.h chromium-61.0.3163.100/third_party/WebKit/Source/platform/wtf/LinkedHashSet.h
--- chromium-61.0.3163.100-orig/third_party/WebKit/Source/platform/wtf/LinkedHashSet.h	2017-09-21 17:05:18.000000000 -0500
+++ chromium-61.0.3163.100/third_party/WebKit/Source/platform/wtf/LinkedHashSet.h	2017-10-11 23:30:39.806323020 -0500
@@ -685,6 +685,31 @@ inline LinkedHashSet<T, U, V, W>& Linked
   return *this;
 }

+inline void SwapAnchor(LinkedHashSetNodeBase& a, LinkedHashSetNodeBase& b) {
+  DCHECK(a.prev_);
+  DCHECK(a.next_);
+  DCHECK(b.prev_);
+  DCHECK(b.next_);
+  swap(a.prev_, b.prev_);
+  swap(a.next_, b.next_);
+  if (b.next_ == &a) {
+    DCHECK_EQ(b.prev_, &a);
+    b.next_ = &b;
+    b.prev_ = &b;
+  } else {
+    b.next_->prev_ = &b;
+    b.prev_->next_ = &b;
+  }
+  if (a.next_ == &b) {
+    DCHECK_EQ(a.prev_, &b);
+    a.next_ = &a;
+    a.prev_ = &a;
+  } else {
+    a.next_->prev_ = &a;
+    a.prev_->next_ = &a;
+  }
+}
+
 template <typename T, typename U, typename V, typename W>
 inline void LinkedHashSet<T, U, V, W>::Swap(LinkedHashSet& other) {
   impl_.swap(other.impl_);
@@ -877,31 +902,6 @@ inline void LinkedHashSet<T, U, V, W>::e
   erase(find(value));
 }

-inline void SwapAnchor(LinkedHashSetNodeBase& a, LinkedHashSetNodeBase& b) {
-  DCHECK(a.prev_);
-  DCHECK(a.next_);
-  DCHECK(b.prev_);
-  DCHECK(b.next_);
-  swap(a.prev_, b.prev_);
-  swap(a.next_, b.next_);
-  if (b.next_ == &a) {
-    DCHECK_EQ(b.prev_, &a);
-    b.next_ = &b;
-    b.prev_ = &b;
-  } else {
-    b.next_->prev_ = &b;
-    b.prev_->next_ = &b;
-  }
-  if (a.next_ == &b) {
-    DCHECK_EQ(a.prev_, &b);
-    a.next_ = &a;
-    a.prev_ = &a;
-  } else {
-    a.next_->prev_ = &a;
-    a.prev_->next_ = &a;
-  }
-}
-
 inline void swap(LinkedHashSetNodeBase& a, LinkedHashSetNodeBase& b) {
   DCHECK_NE(a.next_, &a);
   DCHECK_NE(b.next_, &b);
diff -Naurp chromium-61.0.3163.100-orig/chrome/browser/devtools/devtools_file_system_indexer.cc chromium-61.0.3163.100/chrome/browser/devtools/devtools_file_system_indexer.cc
--- chromium-61.0.3163.100-orig/chrome/browser/devtools/devtools_file_system_indexer.cc
+++ chromium-61.0.3163.100/chrome/browser/devtools/devtools_file_system_indexer.cc
@@ -34,12 +34,13 @@
 using base::TimeTicks;
 using content::BrowserThread;
 using std::map;
-using std::set;
 using std::string;
 using std::vector;

 namespace {

+using std::set;
+
 base::SequencedTaskRunner* impl_task_runner() {
   constexpr base::TaskTraits kBlockingTraits = {base::MayBlock(),
                                                 base::TaskPriority::BACKGROUND};
diff -Naurp chromium-61.0.3163.100-orig/ui/views/examples/box_layout_example.h chromium-61.0.3163.100/ui/views/examples/box_layout_example.h
--- chromium-61.0.3163.100-orig/ui/views/examples/box_layout_example.h
+++ chromium-61.0.3163.100/ui/views/examples/box_layout_example.h
@@ -38,7 +38,7 @@
   void CreateExampleView(View* container) override;

  private:
-  friend class ChildPanel;
+  friend class views::examples::ChildPanel;
   // ButtonListener
   void ButtonPressed(Button* sender, const ui::Event& event) override;
'''

        self.apply_patch(self.directory, text)

        text = r'''
Submitted By:            DJ Lucas <dj_AT_linuxfromscratch_DOT_org>
Date:                    2017-10-12
Initial Package Version: 61.0.3163.100
Upstream Status:         Committed
Origin:                  https://hg.mozilla.org/integration/autoland/rev/d3970338a22b
Description:             Allows building with GlibC-2.26.


diff -Naurp chromium-61.0.3163.100-orig/breakpad/src/client/linux/dump_writer_common/ucontext_reader.cc chromium-61.0.3163.100/breakpad/src/client/linux/dump_writer_common/ucontext_reader.cc
--- chromium-61.0.3163.100-orig/breakpad/src/client/linux/dump_writer_common/ucontext_reader.cc	2017-09-21 17:07:24.000000000 -0500
+++ chromium-61.0.3163.100/breakpad/src/client/linux/dump_writer_common/ucontext_reader.cc	2017-10-11 23:25:53.978959111 -0500
@@ -40,11 +40,11 @@ namespace google_breakpad {

 #if defined(__i386__)

-uintptr_t UContextReader::GetStackPointer(const struct ucontext* uc) {
+uintptr_t UContextReader::GetStackPointer(const ucontext_t* uc) {
   return uc->uc_mcontext.gregs[REG_ESP];
 }

-uintptr_t UContextReader::GetInstructionPointer(const struct ucontext* uc) {
+uintptr_t UContextReader::GetInstructionPointer(const ucontext_t* uc) {
   return uc->uc_mcontext.gregs[REG_EIP];
 }

@@ -88,15 +88,15 @@ void UContextReader::FillCPUContext(RawC

 #elif defined(__x86_64)

-uintptr_t UContextReader::GetStackPointer(const struct ucontext* uc) {
+uintptr_t UContextReader::GetStackPointer(const ucontext_t* uc) {
   return uc->uc_mcontext.gregs[REG_RSP];
 }

-uintptr_t UContextReader::GetInstructionPointer(const struct ucontext* uc) {
+uintptr_t UContextReader::GetInstructionPointer(const ucontext_t* uc) {
   return uc->uc_mcontext.gregs[REG_RIP];
 }

-void UContextReader::FillCPUContext(RawContextCPU *out, const ucontext *uc,
+void UContextReader::FillCPUContext(RawContextCPU *out, const ucontext_t *uc,
                                     const struct _libc_fpstate* fpregs) {
   const greg_t* regs = uc->uc_mcontext.gregs;

@@ -145,11 +145,11 @@ void UContextReader::FillCPUContext(RawC

 #elif defined(__ARM_EABI__)

-uintptr_t UContextReader::GetStackPointer(const struct ucontext* uc) {
+uintptr_t UContextReader::GetStackPointer(const ucontext_t* uc) {
   return uc->uc_mcontext.arm_sp;
 }

-uintptr_t UContextReader::GetInstructionPointer(const struct ucontext* uc) {
+uintptr_t UContextReader::GetInstructionPointer(const ucontext_t* uc) {
   return uc->uc_mcontext.arm_pc;
 }

@@ -184,11 +184,11 @@ void UContextReader::FillCPUContext(RawC

 #elif defined(__aarch64__)

-uintptr_t UContextReader::GetStackPointer(const struct ucontext* uc) {
+uintptr_t UContextReader::GetStackPointer(const ucontext_t* uc) {
   return uc->uc_mcontext.sp;
 }

-uintptr_t UContextReader::GetInstructionPointer(const struct ucontext* uc) {
+uintptr_t UContextReader::GetInstructionPointer(const ucontext_t* uc) {
   return uc->uc_mcontext.pc;
 }

@@ -210,11 +210,11 @@ void UContextReader::FillCPUContext(RawC

 #elif defined(__mips__)

-uintptr_t UContextReader::GetStackPointer(const struct ucontext* uc) {
+uintptr_t UContextReader::GetStackPointer(const ucontext_t* uc) {
   return uc->uc_mcontext.gregs[MD_CONTEXT_MIPS_REG_SP];
 }

-uintptr_t UContextReader::GetInstructionPointer(const struct ucontext* uc) {
+uintptr_t UContextReader::GetInstructionPointer(const ucontext_t* uc) {
   return uc->uc_mcontext.pc;
 }

diff -Naurp chromium-61.0.3163.100-orig/breakpad/src/client/linux/dump_writer_common/ucontext_reader.h chromium-61.0.3163.100/breakpad/src/client/linux/dump_writer_common/ucontext_reader.h
--- chromium-61.0.3163.100-orig/breakpad/src/client/linux/dump_writer_common/ucontext_reader.h	2017-09-21 17:07:24.000000000 -0500
+++ chromium-61.0.3163.100/breakpad/src/client/linux/dump_writer_common/ucontext_reader.h	2017-10-11 23:25:53.978959111 -0500
@@ -41,21 +41,21 @@ namespace google_breakpad {

 // Wraps platform-dependent implementations of accessors to ucontext structs.
 struct UContextReader {
-  static uintptr_t GetStackPointer(const struct ucontext* uc);
+  static uintptr_t GetStackPointer(const ucontext_t* uc);

-  static uintptr_t GetInstructionPointer(const struct ucontext* uc);
+  static uintptr_t GetInstructionPointer(const ucontext_t* uc);

   // Juggle a arch-specific ucontext into a minidump format
   //   out: the minidump structure
   //   info: the collection of register structures.
 #if defined(__i386__) || defined(__x86_64)
-  static void FillCPUContext(RawContextCPU *out, const ucontext *uc,
+  static void FillCPUContext(RawContextCPU *out, const ucontext_t *uc,
                              const struct _libc_fpstate* fp);
 #elif defined(__aarch64__)
-  static void FillCPUContext(RawContextCPU *out, const ucontext *uc,
+  static void FillCPUContext(RawContextCPU *out, const ucontext_t *uc,
                              const struct fpsimd_context* fpregs);
 #else
-  static void FillCPUContext(RawContextCPU *out, const ucontext *uc);
+  static void FillCPUContext(RawContextCPU *out, const ucontext_t *uc);
 #endif
 };

diff -Naurp chromium-61.0.3163.100-orig/breakpad/src/client/linux/handler/exception_handler.cc chromium-61.0.3163.100/breakpad/src/client/linux/handler/exception_handler.cc
--- chromium-61.0.3163.100-orig/breakpad/src/client/linux/handler/exception_handler.cc	2017-09-21 17:07:24.000000000 -0500
+++ chromium-61.0.3163.100/breakpad/src/client/linux/handler/exception_handler.cc	2017-10-11 23:25:53.978959111 -0500
@@ -457,9 +457,9 @@ bool ExceptionHandler::HandleSignal(int
   // Fill in all the holes in the struct to make Valgrind happy.
   memset(&g_crash_context_, 0, sizeof(g_crash_context_));
   memcpy(&g_crash_context_.siginfo, info, sizeof(siginfo_t));
-  memcpy(&g_crash_context_.context, uc, sizeof(struct ucontext));
+  memcpy(&g_crash_context_.context, uc, sizeof(ucontext_t));
 #if defined(__aarch64__)
-  struct ucontext* uc_ptr = (struct ucontext*)uc;
+  ucontext_t* uc_ptr = (ucontext_t*)uc;
   struct fpsimd_context* fp_ptr =
       (struct fpsimd_context*)&uc_ptr->uc_mcontext.__reserved;
   if (fp_ptr->head.magic == FPSIMD_MAGIC) {
@@ -468,9 +468,9 @@ bool ExceptionHandler::HandleSignal(int
   }
 #elif !defined(__ARM_EABI__) && !defined(__mips__)
   // FP state is not part of user ABI on ARM Linux.
-  // In case of MIPS Linux FP state is already part of struct ucontext
+  // In case of MIPS Linux FP state is already part of ucontext_t
   // and 'float_state' is not a member of CrashContext.
-  struct ucontext* uc_ptr = (struct ucontext*)uc;
+  ucontext_t* uc_ptr = (ucontext_t*)uc;
   if (uc_ptr->uc_mcontext.fpregs) {
     memcpy(&g_crash_context_.float_state, uc_ptr->uc_mcontext.fpregs,
            sizeof(g_crash_context_.float_state));
@@ -494,7 +494,7 @@ bool ExceptionHandler::SimulateSignalDel
   // ExceptionHandler::HandleSignal().
   siginfo.si_code = SI_USER;
   siginfo.si_pid = getpid();
-  struct ucontext context;
+  ucontext_t context;
   getcontext(&context);
   return HandleSignal(sig, &siginfo, &context);
 }
diff -Naurp chromium-61.0.3163.100-orig/breakpad/src/client/linux/handler/exception_handler.h chromium-61.0.3163.100/breakpad/src/client/linux/handler/exception_handler.h
--- chromium-61.0.3163.100-orig/breakpad/src/client/linux/handler/exception_handler.h	2017-09-21 17:07:24.000000000 -0500
+++ chromium-61.0.3163.100/breakpad/src/client/linux/handler/exception_handler.h	2017-10-11 23:25:53.978959111 -0500
@@ -191,7 +191,7 @@ class ExceptionHandler {
   struct CrashContext {
     siginfo_t siginfo;
     pid_t tid;  // the crashing thread.
-    struct ucontext context;
+    ucontext_t context;
 #if !defined(__ARM_EABI__) && !defined(__mips__)
     // #ifdef this out because FP state is not part of user ABI for Linux ARM.
     // In case of MIPS Linux FP state is already part of struct
diff -Naurp chromium-61.0.3163.100-orig/breakpad/src/client/linux/microdump_writer/microdump_writer.cc chromium-61.0.3163.100/breakpad/src/client/linux/microdump_writer/microdump_writer.cc
--- chromium-61.0.3163.100-orig/breakpad/src/client/linux/microdump_writer/microdump_writer.cc	2017-09-21 17:07:24.000000000 -0500
+++ chromium-61.0.3163.100/breakpad/src/client/linux/microdump_writer/microdump_writer.cc	2017-10-11 23:25:53.978959111 -0500
@@ -593,7 +593,7 @@ class MicrodumpWriter {

   void* Alloc(unsigned bytes) { return dumper_->allocator()->Alloc(bytes); }

-  const struct ucontext* const ucontext_;
+  const ucontext_t* const ucontext_;
 #if !defined(__ARM_EABI__) && !defined(__mips__)
   const google_breakpad::fpstate_t* const float_state_;
 #endif
diff -Naurp chromium-61.0.3163.100-orig/breakpad/src/client/linux/minidump_writer/minidump_writer.cc chromium-61.0.3163.100/breakpad/src/client/linux/minidump_writer/minidump_writer.cc
--- chromium-61.0.3163.100-orig/breakpad/src/client/linux/minidump_writer/minidump_writer.cc	2017-09-21 17:07:24.000000000 -0500
+++ chromium-61.0.3163.100/breakpad/src/client/linux/minidump_writer/minidump_writer.cc	2017-10-11 23:25:53.978959111 -0500
@@ -1323,7 +1323,7 @@ class MinidumpWriter {
   const int fd_;  // File descriptor where the minidum should be written.
   const char* path_;  // Path to the file where the minidum should be written.

-  const struct ucontext* const ucontext_;  // also from the signal handler
+  const ucontext_t* const ucontext_;  // also from the signal handler
 #if !defined(__ARM_EABI__) && !defined(__mips__)
   const google_breakpad::fpstate_t* const float_state_;  // ditto
 #endif
diff -Naurp chromium-61.0.3163.100-orig/buildtools/third_party/libc++/trunk/include/__locale chromium-61.0.3163.100/buildtools/third_party/libc++/trunk/include/__locale
--- chromium-61.0.3163.100-orig/buildtools/third_party/libc++/trunk/include/__locale	2017-09-21 17:07:34.000000000 -0500
+++ chromium-61.0.3163.100/buildtools/third_party/libc++/trunk/include/__locale	2017-10-11 23:27:04.847682982 -0500
@@ -34,9 +34,6 @@
 # include <support/solaris/xlocale.h>
 #elif defined(_NEWLIB_VERSION)
 # include <support/newlib/xlocale.h>
-#elif (defined(__GLIBC__) || defined(__APPLE__)      || defined(__FreeBSD__) \
-    || defined(__EMSCRIPTEN__) || defined(__IBMCPP__))
-# include <xlocale.h>
 #elif defined(__Fuchsia__)
 # include <support/fuchsia/xlocale.h>
 #elif defined(_LIBCPP_HAS_MUSL_LIBC)
'''

        self.apply_patch(self.directory, text)

        # if False:
        #     self.log_dir('patch', self.directory, 'fix gcc 6 build')
        #     args = [
        #         'sed',
        #         r"""'s/^config("compiler") {/&\ncflags_cc = """
        #         r"""[ "-fno-delete-null-pointer-checks" ]/'""",
        #         '-i',
        #         'build/config/linux/BUILD.gn']
        #     self.run_exe(args, self.directory, self.environment)

        self.log_dir('patch', self.directory, 'enable widevine')
        src = '#define WIDEVINE_CDM_AVAILABLE'
        dst = '#define WIDEVINE_CDM_AVAILABLE\n#define WIDEVINE_CDM_VERSION_STRING "Pinkie Pie"\n'
        filename = os.path.join(self.directory, 'third_party/widevine/cdm/stub/widevine_cdm_version.h')
        patch(filename, src, dst)

        # self.log_dir('patch', self.directory, 'libaddressinput update')
        # args = ['python',
        #         'third_party/libaddressinput/chromium/tools/update-strings.py']
        # self.run_exe(args, self.directory, self.environment)

        # self.log_dir('patch', self.directory, 'patch gn')
        # src = "'base/callback_internal.cc',"
        # dst = src + "\n      'base/callback_helpers.cc',"
        # filename = os.path.join(self.directory,
        #                         'tools/gn/bootstrap/bootstrap.py')
        # patch(filename, src, dst)

        args = ['sed', '-e',
                r'''"/histogram_samples.cc/a\      'base/metrics/histogram_snapshot_manager.cc',"''',
                '-e', r'''"/heap_profiler_event_writer.cc/s/event_/heap_dump_/"''',
                '-i', "tools/gn/bootstrap/bootstrap.py"]
        self.run_exe(args, self.directory, self.environment)

        args = ['sed',
                r"""'/atk_state_set_add_state/s@atk_state_set,@state_set,@'""",
                '-i',
                r"""content/browser/accessibility/browser_accessibility_auralinux.cc"""
                ]
        self.run_exe(args, self.directory, self.environment)

        script = r'''for LIB in ffmpeg flac harfbuzz-ng libjpeg \
           libjpeg_turbo libpng libwebp libxslt yasm; do
    find -type f -path "*third_party/$LIB/*"     \
        \! -path "*third_party/$LIB/chromium/*"  \
        \! -path "*third_party/$LIB/google/*"    \
        \! -path "*base/third_party/icu/*"       \
        \! -path "*base/third_party/libevent/*"  \
        \! -regex '.*\.\(gn\|gni\|isolate\|py\)' \
        -delete
done &&

python build/linux/unbundle/replace_gn_files.py \
    --system-libraries ffmpeg flac harfbuzz-ng libjpeg \
                       libpng libwebp libxslt yasm &&
python third_party/libaddressinput/chromium/tools/update-strings.py'''
        filename = os.path.join(self.directory, 'patch.sh')
        with open(filename, 'wt') as f:
            f.write(script)
        args = self.shell_args + [filename]
        self.run_exe(args, self.directory, self.environment)

    def configure(self):
        self.log_dir('configure', self.directory, 'generating build files')

        script = r'''#!/bin/bash
python tools/gn/bootstrap/bootstrap.py --gn-gen-args '
    google_api_key="AIzaSyDxKL42zsPjbke5O8_rPVpVrLrJ8aeE9rQ"
    google_default_client_id="595013732528-llk8trb03f0ldpqq6nprjp1s79596646.apps.googleusercontent.com"
    google_default_client_secret="5ntt6GbbkjnTVXx-MSxbmx5e"
    enable_hangout_services_extension=false
    clang_use_chrome_plugins=false
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
    is_debug=false
    treat_warnings_as_errors=false
    enable_hangout_services_extension=true
    enable_nacl=false
    enable_nacl_nonsfi=false
    use_allocator="none"
    use_cups=false
    use_gconf=false
    use_gnome_keyring=false
    use_gold=false
    use_gtk3=true
    use_kerberos=true
    use_pulseaudio=false
    link_pulseaudio=false
    fatal_linker_warnings=false
    is_debug=false
    linux_use_bundled_binutils=false
    proprietary_codecs=true
    enable_widevine=true
    fieldtrial_testing_like_official_build=true
    remove_webcore_debug_symbols=true    enable_hangout_services_extension=false
    clang_use_chrome_plugins=false
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

        dst = os.path.join(self.directory, 'third_party', 'node', 'linux',
                           'node-linux-x64', 'bin')
        os.makedirs(dst)
        src = os.path.join(self.prefix_dir, 'bin', 'node')
        os.link(src, dst + '/node')

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
            f.write(text)
        self.run_exe(['bash', 'install.sh'],
                     self.directory,
                     self.environment)
