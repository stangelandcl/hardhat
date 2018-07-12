from .base import GnuRecipe


class MesaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MesaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2a1e36280d01ad18ba6d5b3fbd653cea' \
                      'a109eaa031b78eb5dfaa4df452742b66'
        self.name = 'mesa'
        self.version = '18.1.3'
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
            '--enable-llvm'
            ]
