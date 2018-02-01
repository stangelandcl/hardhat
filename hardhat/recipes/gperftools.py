from .base import GnuRecipe


class GperfToolsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GperfToolsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '314b2ff6ed95cc0763704efb4fb72d01' \
                      '39e1c381069b9e17a619006bee8eee9f'
        self.name = 'gperftools'
        self.depends = ['libunwind']
        self.version = '2.6.3'
        self.url = 'https://github.com/gperftools/gperftools/releases/' \
                   'download/gperftools-$version/gperftools-$version.tar.gz'

        self.configure_args += ['--enable-cpu-profiler',
                                '--enable-heap-profiler',
                                '--enable-heap-checker']
