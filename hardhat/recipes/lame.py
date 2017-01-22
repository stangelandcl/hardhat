from .base import GnuRecipe


class LameRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LameRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '24346b4158e4af3bd9f2e194bb23eb47' \
                      '3c75fb7377011523353196b19b9a23ff'

        self.name = 'lame'
        self.version = '3.99.5'
        self.depends = ['yasm']
        self.url = 'http://downloads.sourceforge.net/project/$name/$name/%s/' \
                   '$name-$version.tar.gz' % self.short_version

        self.environment['LIBS'] = ' -ltinfow'
        self.configure_args += ['--enable-nasm',
                                '--enable-mp3rtp']
