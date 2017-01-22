from .base import GnuRecipe


class LibVpxRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibVpxRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd0afbb5eb1ecae68f8d578abace160a9' \
                      '7e2e8a230e3028cf4db115d59a695aad'

        self.name = 'libvpx'
        self.version = '1.6.0'
        self.depends = ['doxygen', 'which', 'yasm']
        self.url = 'http://storage.googleapis.com/downloads.webmproject.org/' \
                   'releases/webm/libvpx-$version.tar.bz2'
        self.configure_strip_cross_compile()
        self.configure_args += ['--enable-shared']
        self.environment['AS'] = 'yasm'
