from .base import GnuRecipe


class LibTheoraRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibTheoraRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f36da409947aa2b3dcc6af0a8c2e3144' \
                      'bc19db2ed547d64e9171c59c66561c61'

        self.name = 'libtheora'
        self.version = '1.1.1'
        self.depends = ['libogg', 'libvorbis']
        self.url = 'http://downloads.xiph.org/releases/theora/' \
                   'libtheora-$version.tar.xz'

    def patch(self):
        args = ['sed',
                '-i',
                r"'s/png_\(sizeof\)/\1/g'",
                'examples/png2theora.c'
                ]

        self.run_exe(args, self.directory, self.environment)
