from .base import GnuRecipe


class CdDiscIDRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CdDiscIDRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ffd68cd406309e764be6af4d5cbcc309' \
                      'e132c13f3597c6a4570a1f218edd2c63'

        self.name = 'cd-discid'
        self.version = '1.4'
        self.url = 'http://linukz.org/download/cd-discid-$version.tar.gz'
