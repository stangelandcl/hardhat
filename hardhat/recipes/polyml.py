from .base import GnuRecipe


class PolyMLRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PolyMLRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '19340d8e9cea15c3fd786dde27028cd2' \
                      '947608955a376d1317a20268c8a19279'
        
        self.name = 'polyml'
        self.version = '5.7'
        self.url = 'https://github.com/$name/$name/archive/v$version.tar.gz'
