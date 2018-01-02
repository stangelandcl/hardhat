from .base import GnuRecipe


class GnomeCommonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GnomeCommonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8407fd8786a44c9ce47987de0906d926' \
                      '6492195df9251a089afaa06cc65c72d8'

        self.name = 'gnome-common'
        self.version = '3.18.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools']
        self.url = 'https://github.com/GNOME/gnome-common/archive/' \
                   '$version.tar.gz'
        self.configure_args = [self.shell_args + ['./autogen.sh'],
                               self.configure_args]
