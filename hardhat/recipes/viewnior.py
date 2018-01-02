from .base import GnuRecipe


class ViewniorRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ViewniorRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '89013f6d30c1c121d8cb6327d3ffc35a' \
                      '757fba1d777c24849d632afe244e60a0'
        self.name = 'viewnior'
        self.version = '1.6'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools',
                        'exiv2',
                        'gdk-pixbuf',
                        'glib',
                        'gnome-common',
                        'gnome-object-introspection',
                        'gtk2',
                        'shared-mime-info']
        self.url = 'https://github.com/hellosiyan/Viewnior/archive/' \
                   'viewnior-$version.tar.gz'

        self.configure_args = [self.shell_args + ['./autogen.sh'],
                               self.configure_args]
