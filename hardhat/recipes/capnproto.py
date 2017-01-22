from .base import GnuRecipe
import os


class CapnProtoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CapnProtoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '13c66dc1ce2a038562cddeaf48f71f0b' \
                      'b0e15a1d1a1775efa80dff3cdebeea6c'

        self.name = 'capnproto'
        self.version = '0.5.3'
        self.url = 'https://github.com/sandstorm-io/$name/archive/' \
                   'v$version.tar.gz'

        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]

    def patch(self):
        self.directory = os.path.join(self.directory, 'c++')
