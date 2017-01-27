import os
from string import Template
from .base import GnuRecipe


class PaleMoonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PaleMoonRecipe, self).__init__(*args, **kwargs)
        self.name = 'palemoon'
        self.version = '27.1.0b2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+(\w+\d+)?)'
        self.version_url = 'https://github.com/MoonchildProductions/' \
                           'Pale-Moon/releases'
        self.depends = ['atk', 'autoconf', 'dbus', 'dbus-glib',
                        'cairo',
                        'gdk-pixbuf',
                        'glib', 'gobject-introspection',
                        'gtk2', 'mesa', 'pango', 'python2', 'xorg-libs']
        self.url = 'https://github.com/MoonchildProductions/Pale-Moon/' \
                   'archive/$version.tar.gz'

    def patch(self):
        self.log_dir('patch', self.directory, 'creating .mozconfig')
        text = Template(r'''
ac_add_options --enable-official-branding
export MOZILLA_OFFICIAL=1

mk_add_options MOZ_CO_PROJECT=browser
ac_add_options --enable-application=browser

mk_add_options MOZ_OBJDIR=${directory}/obj

ac_add_options --enable-optimize="${cflags} -msse2 -mfpmath=sse -ffast-math"
ac_add_options --with-pthreads

ac_add_options --disable-installer
ac_add_options --disable-updater

ac_add_options --enable-release
ac_add_options --enable-devtools
ac_add_options --enable-jemalloc
ac_add_options --enable-shared-js

ac_add_options --enable-strip

ac_add_options --x-libraries=${prefix}/lib

''').substitute(prefix=self.prefix_dir,
                directory=self.directory,
                cflags=self.environment['CFLAGS'])

        filename = os.path.join(self.directory, '.mozconfig')
        with open(filename, 'wt') as f:
            f.write(text)
