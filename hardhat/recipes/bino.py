from .base import GnuRecipe


class BinoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(BinoRecipe, self).__init__(*args, **kwargs)
#        self.sha256 = '3254316d3ae81cc69643dcd823caaac1' \
#                      '233704d91289272d0011ced5e5cdffe2'
        self.sha256 = '96a63ed76629879917af2bd7fa73b896' \
                      '721705c7b15d450928501c5ce69539c6'

        self.name = 'bino'
        self.version = '1.6.5'
        self.depends = ['ffmpeg',
                        'glew',
                        'openal-soft',
                        'pkgconfig',
                        ]
#        self.url = 'http://download.savannah.nongnu.org/releases/bino/' \
#                   'bino-$version.tar.xz'

        self.url = 'http://git.savannah.gnu.org/cgit/bino.git/snapshot/' \
                   'bino-7098cd6afb7ed805de085ed72a5a3ff56e529277.tar.gz'

    def configure(self):
        self.configure_args = ['autoreconf', '-i']
        super(BinoRecipe, self).configure()

        self.configure_args = self.shell_args + [
            'configure',
            '--prefix=%s' % self.prefix_dir]
        super(BinoRecipe, self).configure()
