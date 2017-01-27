from .base import GnuRecipe


class MesaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MesaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a6ed622645f4ed61da418bf65adde5bc' \
                      'c4bb79023c36ba7d6b45b389da4416d5'

        self.name = 'mesa'
        self.version = '13.0.2'
        self.version_regex = '(?P<version>\d+\.\d+\.\d+)/'
        self.version_url = 'https://mesa.freedesktop.org/archive/'
        self.depends = ['elfutils', 'eudev', 'libdrm', 'llvm', 'nettle',
                        'wayland-protocols', 'xorg-libs']
        self.url = 'ftp://ftp.freedesktop.org/pub/mesa/$version/' \
                   'mesa-$version.tar.xz'
        self.configure_args += [
            '--enable-egl',
            '--with-egl-platforms=x11,drm,wayland,surfaceless',
            '--enable-gles1',
            '--enable-gles2',
            '--enable-shared-glapi',
            '--enable-gbm',
            '--enable-dri3',
            '--enable-texture-float',
            '--enable-glx-tls',
            '--with-gallium-drivers=i915,r600,nouveau,radeonsi,svga,swrast,swr',
            '--enable-gallium-llvm'
            ]
