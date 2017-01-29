import os
from string import Template
from .base import GnuRecipe


class FirefoxRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FirefoxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '30ba00ba716ea1eeda526e2ccc8642f8' \
                      'd18a836793fde50e87a4fcb9d9fccca9'

        self.name = 'firefox'
        self.version = '51.0.1'
        self.version_regex = r'(?P<version>\d+\.\d+(\.\d+)*)'
        self.version_url = 'https://ftp.mozilla.org/pub/mozilla.org/firefox/' \
                           'releases/'
        self.depends = ['alsa-lib',
                        'autoconf',
                        'autoconf2.13',
                        'curl',
                        'dbus-glib',
                        'gconf',
                        'gtk3',
                        'icu',
                        'libevent',
                        'libjpeg-turbo',
                        'libpng',
                        'libproxy',
                        'libwebp',
                        'libvpx',
                        'nspr',
                        'nss',
                        'openssl',
                        'python2',
                        'sqlite3',
                        'startup-notification',
                        'unzip',
                        'yasm',
                        'zip',
                        'zlib'
                        ]
        self.url = 'https://ftp.mozilla.org/pub/mozilla.org/firefox/' \
                   'releases/$version/source/firefox-$version.source.tar.xz'

        self.compile_args = ['make', '-f', 'client.mk']
        self.install_args = [
            ['make', '-f', 'client.mk', 'install', 'INSTALL_SDK='],
            ['mkdir', '-pv', '%s/lib/mozilla/plugins' % self.prefix_dir],
            ['ln', '-sfv',
             '../../mozilla/plugins',
             '%s/lib/firefox-%s/browser' % (self.prefix_dir, self.version)]
            ]

    def configure(self):
        pass

    def extract(self):
        super(FirefoxRecipe, self).extract()
        self.directory = os.path.join(self.directory,
                                      '%s-%s' % (self.name, self.version))

    def patch(self):
        mozconfig = Template(r'''
# If you have a multicore machine, all cores will be used by default.
# If desired, you can reduce the number of cores used, e.g. to 1, by
# uncommenting the next line and setting a valid number of CPU cores.
mk_add_options MOZ_MAKE_FLAGS="-j${cpus}"
ac_add_options --target=${target}
ac_add_options --disable-gold

# If you have installed dbus-glib, comment out this line:
#ac_add_options --disable-dbus

# If you have installed dbus-glib, and you have installed (or will install)
# wireless-tools, and you wish to use geolocation web services, comment out
# this line
#ac_add_options --disable-necko-wifi

# Uncomment this option if you wish to build with gtk+-2
#ac_add_options --enable-default-toolkit=cairo-gtk2

# Uncomment these lines if you have installed optional dependencies:
#ac_add_options --enable-system-hunspell
ac_add_options --enable-startup-notification

# Comment out following option if you have PulseAudio installed
ac_add_options --disable-pulseaudio

# If you have installed GConf, comment out this line
#ac_add_options --disable-gconf

# Comment out following options if you have not installed
# recommended dependencies:
ac_add_options --enable-system-sqlite
ac_add_options --with-system-libevent
ac_add_options --with-system-libvpx
ac_add_options --with-system-nspr
ac_add_options --with-system-nss
ac_add_options --with-system-icu

# If you are going to apply the patch for system graphite
# and system harfbuzz, uncomment these lines:
#ac_add_options --with-system-graphite2
#ac_add_options --with-system-harfbuzz

# Stripping is now enabled by default.
# Uncomment these lines if you need to run a debugger:
#ac_add_options --disable-strip
#ac_add_options --disable-install-strip

# The BLFS editors recommend not changing anything below this line:
ac_add_options --prefix=${prefix}
ac_add_options --enable-application=browser

ac_add_options --disable-crashreporter
ac_add_options --disable-updater
ac_add_options --disable-tests

ac_add_options --enable-optimize

ac_add_options --enable-gio
ac_add_options --enable-official-branding
ac_add_options --enable-safe-browsing
ac_add_options --enable-url-classifier

# From firefox-40, using system cairo causes firefox to crash
# frequently when it is doing background rendering in a tab.
#ac_add_options --enable-system-cairo
ac_add_options --enable-system-ffi
ac_add_options --enable-system-pixman

ac_add_options --with-pthreads

ac_add_options --with-system-bz2
ac_add_options --with-system-jpeg
ac_add_options --with-system-png
ac_add_options --with-system-zlib

mk_add_options MOZ_OBJDIR=@TOPSRCDIR@/firefox-build-dir
''').substitute(cpus=self.cpu_count,
                prefix=self.prefix_dir,
                target=self.target_triplet)
        file = os.path.join(self.directory, 'mozconfig')
        with open(file, 'wt') as f:
            f.write(mozconfig)
