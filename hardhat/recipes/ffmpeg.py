from .base import GnuRecipe


class FfmpegRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FfmpegRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3f01bd1fe1a17a277f8c84869e5d9192' \
                      'b4b978cb660872aa2b54c3cc8a2fedfc'

        self.name = 'ffmpeg'
        self.version = '3.2.2'
        self.depends = ['alsa-lib',
                        'fdk-aac',
                        'freetype',
                        'lame',
                        'libass',
                        'libtheora',
                        'libva',
                        'libvdpau',
                        'libvorbis',
                        'libvpx',
                        'openssl',
                        'opus',
                        'sdl2',
                        'x264',
                        'x265',
                        'yasm']
        self.url = 'http://ffmpeg.org/releases/ffmpeg-$version.tar.xz'
        self.configure_args += [
            '--enable-gpl',
            '--enable-version3',
            '--enable-nonfree',
            '--enable-shared',
            '--enable-libass',
            '--enable-libfdk-aac',
            '--enable-libfreetype',
            '--enable-libmp3lame',
            '--enable-libopus',
            '--enable-libtheora',
            '--enable-libvorbis',
            '--enable-libvpx',
            '--enable-libx264',
            '--enable-libx265',
            '--enable-x11grab',
            '--disable-debug',
            '--enable-openssl',
            ]
        self.configure_strip_cross_compile()
        self.environment_strip_lto()

    def patch(self):
        self.log_dir('patch', self.directory, 'patching to use -lasound')
        args = ['sed',
                '-i',
                r"""'s/-lflite"/-lflite -lasound"/'""",
                'configure']
        self.run_exe(args, self.directory, self.environment)
