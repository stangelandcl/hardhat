from .base import GnuRecipe


class LibSpectreRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibSpectreRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e81b822a106beed14cf0fec70f1b890c' \
                      '690c2ffa150fa2eee41dc26518a6c3ec'
                
        self.name = 'libspectre'
        self.depends = ['ghostscript']
        self.version = '0.2.7'
        self.url = 'http://libspectre.freedesktop.org/releases/' \
                   'libspectre-$version.tar.gz'
