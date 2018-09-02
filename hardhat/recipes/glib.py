from .base import GnuRecipe


class GLibRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GLibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2f648d68bc825ddb95dcc52640a998af' \
                      '1cb8a523f630ac4846ba8fc65902a6a6'

        self.name = 'glib'
        self.version = '2.57.3'
        self.version_regex = '(?P<version>\d+\.\d+(\.\d+)?)\.tar\.gz'
        self.depends = ['gtk-doc', 'libffi', 'pcre', 'python3', 'util-linux']
        self.version_url = 'https://github.com/GNOME/glib/releases/'
        self.url = 'https://github.com/GNOME/glib/archive/$version.tar.gz'
        self.configure_args = [self.shell_args + ['./autogen.sh'],
                               self.configure_args + ['glib_cv_stack_grows=no',
                                                      'glib_cv_uscore=false',
                                                      '--with-pcre=system',
                                                      '--enable-gtk-doc']]
