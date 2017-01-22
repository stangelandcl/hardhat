from .base import GnuRecipe
from ..urls import Urls


class PidginRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PidginRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f72613440586da3bdba6d58e718dce1b' \
                      '2c310adf8946de66d8077823e57b3333'

        self.name = 'pidgin'
        self.version = '2.11.0'
        self.url = 'https://downloads.sourceforge.net/project/pidgin/Pidgin/' \
                   '$version/pidgin-$version.tar.bz2'
        self.depends = ['gnutls', 'gtk2', 'libxml2', 'ncurses', 'perl']
        self.configure_args += [
            '--disable-gtkspell',
            '--disable-vv',
            '--disable-meanwhile',
            '--disable-avahi',
            '--disable-dbus',
            '--with-ncurses-headers=%s/include' % self.prefix_dir,
            '--disable-tcl']
        self.environment['LIBS'] += ' -ltinfow'
