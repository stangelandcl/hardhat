import os
from .base import GnuRecipe
from ..util import patch


class FreeRdpRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FreeRdpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '99e108cfc2f7bc7339d0693e9c4c25f9' \
	              '0bad4c6bc38349206758c2cccd7cc4cc'
        self.name = 'freerdp'
        self.version = '71ce3378da9044d21575d0331dc4fb97bc4c995c'
        self.url = 'https://github.com/FreeRDP/FreeRDP/archive/' \
                   '$version.tar.gz'
        self.depends = ['alsa-lib',
                        'ffmpeg',
                        'libjpeg-turbo',
                        'libxkbcommon',
                        'openssl',
                        'wayland',
                        'x264',
                        'xorg-libs'
                        ]
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '-DWITH_X11=ON',
            '-DWITH_WAYLAND=ON',
            '-DWITH_DIRECTFB=OFF',
            '-DWITH_ALSA=ON',
            '-DWITH_PULSE=OFF',
            '-DWITH_FFMPEG=ON',
            '-DWITH_JPEG=ON',
            '-DWITH_X264=ON',
            '-DWITH_GSTREAMER_1_0=OFF',
            '-DWITH_GSTREAMER_0_10=OFF',
            ]
        self.key_mappings = [
            ('LFSH', 'RDP_SCANCODE_LSHIFT', 'RDP_SCANCODE_LCONTROL'),
            ('CAPS', 'RDP_SCANCODE_CAPSLOCK', 'RDP_SCANCODE_LSHIFT')
            ]

    def patch(self):
        self.log_dir('patch', self.directory, 'remapping keys')
        filename = os.path.join(self.directory, 'libfreerdp',
                                'locale', 'keyboard_xkbfile.c')

        for clientKey, old, new in self.key_mappings:

            src = '{ "%s", %s }' % (clientKey, old)
            dst = '{ "%s", %s }' % (clientKey, new)
            patch(filename, src, dst)
