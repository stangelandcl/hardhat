from .base import GnuRecipe


class HtopRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(HtopRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd9d6826f10ce3887950d709b53ee1d8c' \
                      '1849a70fa38e91d5896ad8cbc6ba3c57'
        self.name = 'htop'
        self.version = '2.2.0'
        self.version_regex = r'(?P<version>\d+\.\d+(\.\d+)?)'
        self.version_url = 'http://hisham.hm/htop/releases/'
        self.url = 'http://hisham.hm/htop/releases/$version/' \
                   'htop-$version.tar.gz'
        self.configure_args += ['--enable-unicode',
                                '--enable-proc']
        self.environment['LIBS'] += ' -ltinfow'
