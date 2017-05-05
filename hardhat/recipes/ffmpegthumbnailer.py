from .base import GnuRecipe


class FfmpegThumbnailerRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FfmpegThumbnailerRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e5c31299d064968198cd378f7488e52c' \
                      'd5e738fac998eea780bc77d7f32238c2'

        self.name = 'ffmpegthumbnailer'
        self.version = '2.2.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.url = 'https://github.com/dirkvdb/ffmpegthumbnailer/releases/' \
                   'download/$version/ffmpegthumbnailer-$version.tar.bz2'
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            '-DENABLE_GIO=ON',
            '-DENABLE_THUMBNAILER=ON'
            ]
