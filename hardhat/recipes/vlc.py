import os
from .base import GnuRecipe
from ..util import patch


class VlcRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(VlcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2827fa94f4744fa4a080e72f6dc949ec' \
                      'ce6667944dd96b8b53a49bd74afa1a71'
#        self.sha256 = 'bf2813c517e586548587506f3e3e8fc4' \
#                      '289f4ece3f0012a1dadeab30cb0f00b3'
        self.name = 'vlc'
        # just above 3.0.3
#        self.version = '042b75e400bb259ba142f91464a214897476488a'
        self.version = '92c146a614aebe7412b19553e5b4bbb92a469b44'
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
 #       self.url = 'https://github.com/videolan/vlc-3.0/archive/$version.tar.gz'
        self.url = 'https://github.com/videolan/vlc/archive/$version.tar.gz'
        self.compile_args = ['make', '-j1', 'V=1']  # verbose
        self.environment['CFLAGS'] += ' -DLUA_COMPAT_5_1'
        self.configure_args += [
            '--disable-atmo',
            '--disable-silent-rules',
            '--enable-opencv=no',
            '--with-kde-solid=%s/share/kde4/apps/solid/actions' % self.prefix_dir]
        self.configure_strip_cross_compile()
        self.configure_args = [self.shell_args + ['./bootstrap'],
                               self.configure_args]

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
        self.log_dir('patch', self.directory, 'QButtonGroup')
        filename = os.path.join(self.directory, 'modules/gui/qt/components/simple_preferences.cpp')
        src = '#include <QDir>'
        dst = '#include <QDir>\n#include <QButtonGroup>'
        patch(filename, src, dst)

        filename = os.path.join(self.directory, 'src', 'Makefile.am')
        src = r'''	$(AM_V_at)rm -f -- revision.tmp
	$(AM_V_GEN)if ! git \
			--git-dir="$(top_srcdir)/.git/" describe \
			--tags --long --match '?.*.*' --always; then \
		cat $(srcdir)/revision.txt ; \
	fi > revision.tmp
	$(AM_V_at)if diff revision.tmp $(srcdir)/revision.txt >/dev/null 2>&1; then \
		rm -f -- revision.tmp; \
	else \
		mv -f -- revision.tmp $(srcdir)/revision.txt; \
	fi
'''
        dst = '\techo 1 > $(srcdir)/revision.txt'
        patch(filename, src, dst)
