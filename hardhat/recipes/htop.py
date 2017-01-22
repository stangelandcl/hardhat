from .base import GnuRecipe


class HtopRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(HtopRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '179be9dccb80cee0c5e1a1f58c8f72ce' \
                      '7b2328ede30fb71dcdf336539be2f487'
        self.name = 'htop'
        self.version = '2.0.2'
        self.version_regex = r'(?P<version>\d+\.\d+(\.\d+)?)'
        self.version_url = 'http://hisham.hm/htop/releases/'
        self.url = 'http://hisham.hm/htop/releases/$version/' \
                   'htop-$version.tar.gz'
        self.configure_args += ['--enable-unicode',
                                '--enable-proc']
        self.environment['LIBS'] += ' -ltinfow'
