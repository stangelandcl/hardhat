from .base import GnuRecipe


class LibmngRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibmngRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4a462fdd48d4bc82c1d7a21106c8a18b' \
                      '62f8cc0042454323058e6da0dbb57dd3'

        self.name = 'libmng'
        self.version = '2.0.3'
        self.depends = ['libjpeg-turbo', 'lcms']
        self.url = 'http://downloads.sourceforge.net/libmng/' \
                   'libmng-$version.tar.xz'

    def need_configure(self):
        return True
