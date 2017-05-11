from .base import GnuRecipe


class CJsonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CJsonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6d1482c1b492893b25ab7e77ee6098fe' \
                      '3ef10585df660e5ffe67e632a8c5b9e4'

        self.name = 'cJSON'
        self.version = '1.5.2'
        self.url = 'https://github.com/DaveGamble/cJSON/archive/' \
                   'v$version.tar.gz'
        self.compile_args += ['all']
        self.install_args += ['PREFIX=""',
                              'DESTDIR=%s' % self.prefix_dir,
                              'LIBRARY_PATH=lib',
                              'INCLUDE_PATH=include/cjson']

    def configure(self):
        pass
