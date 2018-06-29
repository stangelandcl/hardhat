from .base import GnuRecipe


class GLibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GLibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '73c10a1927c79d8c318bba9ad6f7bc96' \
                      'ff187013ee19377b3e82f684958b2c2c'
        self.name = 'glib'
        self.version = '2.57.1'
        self.version_regex = '(?P<version>\d+\.\d+(\.\d+)?)\.tar\.gz'
        self.depends = ['gtk-doc', 'libffi', 'pcre', 'python3', 'util-linux']
        self.version_url = 'https://github.com/GNOME/glib/releases/'
        self.url = 'https://github.com/GNOME/glib/archive/$version.tar.gz'
        self.configure_args = [self.shell_args + ['./autogen.sh'],
                               self.configure_args + ['glib_cv_stack_grows=no',
                                                      'glib_cv_uscore=false',
                                                      '--with-pcre=system',
                                                      '--enable-gtk-doc']]
