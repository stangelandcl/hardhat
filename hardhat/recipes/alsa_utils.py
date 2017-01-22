from .base import GnuRecipe


class AlsaUtilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AlsaUtilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '89757c9abaf420831b088fce354d492a' \
                      'cc170bd02bb50eb7392c175f594b8041'

        self.name = 'alsa-utils'
        self.version = '1.1.1'
        self.depends = ['alsa-lib']
        self.url = 'ftp://ftp.alsa-project.org/pub/utils/' \
                   'alsa-utils-$version.tar.bz2'

        self.environment['NCURSESW_LIBS'] = '-lncursesw -ltinfow'
