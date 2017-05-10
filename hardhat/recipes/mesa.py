from .base import GnuRecipe


class MesaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MesaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7510eee0d0077860b250d30d73305048' \
                      'c2df4ba09ea8fc04e4f3eec7beece301'

        self.name = 'mesa'
        self.version = '17.0.5'
        self.version_regex = '(?P<version>\d+\.\d+\.\d+)/'
        self.version_url = 'https://mesa.freedesktop.org/archive/'
        self.depends = ['elfutils', 'eudev', 'libdrm', 'llvm', 'nettle',
                        'wayland-protocols', 'xorg-libs']
        self.url = 'https://mesa.freedesktop.org/archive/mesa-$version.tar.gz'
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
