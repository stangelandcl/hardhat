from .base import GnuRecipe


class LibaioRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibaioRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e019028e631725729376250e32b47301' \
                      '2f7cb68e1f7275bfc1bbcdd0f8745f7e'
        self.name = 'libaio'
        self.version = '0.3.110'
        self.url = 'https://launchpad.net/ubuntu/+archive/primary/' \
                   '+files/libaio_$version.orig.tar.gz'
        self.compile_args += ['prefix=%s' % self.prefix_dir]
        self.install_args += ['prefix=%s' % self.prefix_dir]
