import os
from .base import GnuRecipe
from ..util import patch


class FreeRdpRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FreeRdpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e8b23bf7d22d933e7d2a64f84cc09c83' \
                      '29016a0b31eaff02b9f4eff5c53a2789'
        self.name = 'freerdp'
        # 8cba20 04-26-2018
        self.version = '8cba2019997587ea83e2949eb39f789671fc6bcd'
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
            '-DWITH_X264=OFF',
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
