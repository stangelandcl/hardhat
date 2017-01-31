import os
import shutil
from .base import GnuRecipe
from ..urls import Urls


class GnomeIconThemeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GnomeIconThemeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '359e720b9202d3aba8d477752c4cd11e' \
                      'ced368182281d51ffd64c8572b4e503a'

        self.name = 'gnome-icon-theme'
        self.version = '3.12.0'
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gnome-icon-theme/' \
                   '$short_version/gnome-icon-theme-$version.tar.xz'
        self.depends = ['gtk3', 'hicolor-icon-theme', 'icon-naming-utils']
