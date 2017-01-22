from .base import GnuRecipe


class GcRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '584e29e2f1be4a389ca30f78dcd2c991' \
                      '031e7d1e1eb3d7ce2a0f975218337c2f'

        self.name = 'gc'
        self.version = '7.2g'
        self.url = 'http://www.hboehm.info/gc/gc_source/gc-$version.tar.gz'

        self.configure_args += ['--enable-cplusplus',
                                '--disable-gcj'
                                ]
    def do_download(self, tmpfile):
        args = ['wget', self.url, '-O', tmpfile]
        self.run_exe(args, self.tarball_dir, self.environment)
