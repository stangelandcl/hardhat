import os
from .base import GnuRecipe


class X265Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(X265Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b872552535e41fbffa03ba7cbcd3479c' \
                      '42c4053868309292e78e147b7773ac4b'

        self.name = 'x265'
        self.version = '2.2'
        self.depends = ['cmake', 'yasm']
        self.url = 'https://bitbucket.org/multicoreware/x265/downloads/' \
                   'x265_$version.tar.gz'
        self.configure_args = [
            'cmake',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '../source'
            ]
        self.configure_strip_cross_compile()
        self.environment['AS'] = 'yasm'

    def patch(self):
        self.directory = os.path.join(self.directory, 'bld')
        os.makedirs(self.directory)
