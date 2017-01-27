import os
from .base import GnuRecipe


class GpmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GpmRecipe, self).__init__(*args, **kwargs)
        self.name = 'gpm'
        self.version = '1.20.7'
#./autogen.sh
        self.url = 'http://www.nico.schottelius.org/software/gpm/archives/' \
                   'gpm-$version.tar.bz2'
