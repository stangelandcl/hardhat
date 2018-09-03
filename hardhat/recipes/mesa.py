from .base import GnuRecipe


class MesaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MesaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0c3c240bcd1352d179e65993214f9d55' \
                      'a399beac852c3ab4433e8df9b6c51c83'
        self.name = 'mesa'
        self.version = '18.1.7'
        self.version_regex = '(?P<version>\d+\.\d+\.\d+)/'
        self.version_url = 'https://mesa.freedesktop.org/archive/'
        self.depends = ['elfutils', 'eudev', 'libdrm', 'llvm', 'nettle',
                        'wayland-protocols', 'xorg-libs']
        self.url = 'https://mesa.freedesktop.org/archive/mesa-$version.tar.gz'
        self.configure_args += [
            '--enable-egl',
            '--with-platforms=drm,x11,wayland,surfaceless',
            '--enable-gles1',
            '--enable-gles2',
            '--enable-shared-glapi',
            '--enable-gbm',
            '--enable-dri3',
            '--enable-texture-float',
            '--enable-glx-tls',
            '--enable-osmesa',
            '--enable-opengl',
            '--with-gallium-drivers=i915,r600,nouveau,radeonsi,svga,swrast,swr',
            '--enable-llvm'
            ]
