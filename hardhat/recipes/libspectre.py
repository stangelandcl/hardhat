from .base import GnuRecipe


class LibSpectreRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibSpectreRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '65256af389823bbc4ee4d25bfd1cc190' \
                      '23ffc29ae9f9677f2d200fa6e98bc7a8'
                
        self.name = 'libspectre'
        self.depends = ['ghostscript']
        self.version = '0.2.8'
        self.url = 'http://libspectre.freedesktop.org/releases/' \
                   'libspectre-$version.tar.gz'
