from .base import GnuRecipe


class LibTiRpcRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibTiRpcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5156974f31be7ccbc8ab1de37c4739af' \
                      '6d9d42c87b1d5caf4835dda75fcbb89e'

        self.name = 'libtirpc'
        self.version = '1.0.1'
        self.url = 'http://downloads.sourceforge.net/project/libtirpc/' \
                   'libtirpc/$version/libtirpc-$version.tar.bz2'
        self.depends = ['mit-kerberos']
