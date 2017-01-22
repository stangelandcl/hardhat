from .base import GnuRecipe


class LibAssRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibAssRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9387a2421b6e6a132c7d473de594b9f0' \
                      '367aa85af64aa103b66f0861431b1596'

        self.name = 'libass'
        self.version = '0.13.5'
        self.depends = ['fontconfig', 'freetype', 'fribidi', 'harfbuzz']
        self.url = 'https://github.com/libass/libass/releases/download/' \
                   '$version/libass-$version.tar.xz'
