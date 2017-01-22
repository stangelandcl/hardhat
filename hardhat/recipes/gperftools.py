from .base import GnuRecipe


class GperfToolsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GperfToolsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6fa2748f1acdf44d750253e160cf6e2e' \
                      '72571329b42e563b455bde09e9e85173'

        self.name = 'gperftools'
        self.depends = ['libunwind']
        self.version = '2.5'
        self.url = 'https://github.com/gperftools/gperftools/releases/' \
                   'download/gperftools-$version/gperftools-$version.tar.gz'

        self.configure_args += ['--enable-cpu-profiler',
                                '--enable-heap-profiler',
                                '--enable-heap-checker']
