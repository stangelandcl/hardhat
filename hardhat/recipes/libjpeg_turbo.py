from .base import GnuRecipe


class LibJpegTurboRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibJpegTurboRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '41429d3d253017433f66e3d472b8c7d9' \
                      '98491d2f41caa7306b8d9a6f2a2c666c'

        self.name = 'libjpeg-turbo'
        self.version = '1.5.1'
        self.url = 'https://sourceforge.net/projects/$name/files/' \
                   '$name-$version.tar.gz'
