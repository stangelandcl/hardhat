from .base import GnuRecipe


class XpdfRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XpdfRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ff3d92c42166e35b1ba6aec9b5f0adff' \
                      'b5fc05a3eb95dc49505b6e344e4216d6'

        self.name = 'xpdf'
        self.version = '4.00'
        self.depends = ['cmake', 'freetype', 'libpng', 'zlib']
        self.url = 'https://xpdfreader-dl.s3.amazonaws.com/xpdf-$version.tar.gz'
        self.configure_args = ['cmake', '-G', '"Unix Makefiles"',
                               '-DCMAKE_BUILD_TYPE=Release',
                               '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir]
