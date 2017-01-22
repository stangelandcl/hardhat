from .base import GnuRecipe


class VlcRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(VlcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '1632e91d2a0087e0ef4c3fb4c95c3c28' \
                      '90f7715a9d1d43ffd46329f428cf53be'

        self.name = 'vlc'
        self.version = '2.2.4'
        self.depends = [
            'alsa-lib',
            'dbus',
            'ffmpeg',
            'flac',
            'fontconfig',
            'fribidi',
            'freetype',
            'libass',
            'libdvdcss',
            'libgcrypt',
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
