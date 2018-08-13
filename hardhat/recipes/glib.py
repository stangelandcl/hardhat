from .base import GnuRecipe


class GLibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GLibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9b0edc4ff5d3de6cf78491c1f83b41ca' \
                      'd6b319adad2a195886cdc60709183f99'
        self.name = 'glib'
        self.version = '2.57.2'
        self.version_regex = '(?P<version>\d+\.\d+(\.\d+)?)\.tar\.gz'
        self.depends = ['gtk-doc', 'libffi', 'pcre', 'python3', 'util-linux']
        self.version_url = 'https://github.com/GNOME/glib/releases/'
        self.url = 'https://github.com/GNOME/glib/archive/$version.tar.gz'
        self.configure_args = [self.shell_args + ['./autogen.sh'],
                               self.configure_args + ['glib_cv_stack_grows=no',
                                                      'glib_cv_uscore=false',
                                                      '--with-pcre=system',
                                                      '--enable-gtk-doc']]
