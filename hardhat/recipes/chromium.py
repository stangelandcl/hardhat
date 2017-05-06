import os
from .base import GnuRecipe
from ..util import patch


class ChromiumRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ChromiumRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5ab61b7025a5143fa1b21713479b316e' \
                      'c7a98e262e79e84f9c9a9656179217cb'

        self.name = 'chromium'
        self.version = '58.0.3029.81'
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


    def patch(self):
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
