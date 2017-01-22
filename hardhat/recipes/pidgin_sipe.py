from .base import GnuRecipe
from ..urls import Urls


class PidginSipeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PidginSipeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '651af55d65cbdf5bdbee0366bd5151be' \
                      'c4152c910743aa432204d015893fe444'
        self.name = 'pidgin-sipe'
        self.version = '1.21.1'
        self.url = 'https://downloads.sourceforge.net/project/sipe/sipe/' \
                   '$name-$version/$name-$version.tar.xz'
        self.depends = ['pidgin']
