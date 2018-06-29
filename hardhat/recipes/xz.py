from .base import GnuRecipe


class XZRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XZRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3313fd2a95f43d88e44264e6b015e7d0' \
                      '3053e681860b0d5d3f9baca79c57b7bf'
        self.name = 'xz'  # includes liblzma
        self.version = '5.2.4'
        self.url = 'http://tukaani.org/xz/xz-$version.tar.bz2'
        self.compile_args = ['make', '-j1']
