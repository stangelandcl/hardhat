import os
import shutil
from .base import GnuRecipe
from ..urls import Urls


class IconNamingUtilsThemeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(IconNamingUtilsThemeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b1378679df4485b4459f609a3304238b' \
                      '3e92d91e43744c47b70abbe690d883d5'
        self.name = 'icon-naming-utils'
        self.version = '0.8.90'
        self.url = 'http://tango.freedesktop.org/releases/icon-naming-utils-$version.tar.bz2'
        self.depends = ['perl5-xml-simple']
