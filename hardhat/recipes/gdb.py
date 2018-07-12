from .base import GnuRecipe


class GdbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GdbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'af61a0263858e69c5dce51eab26662ff' \
                      '3d2ad9aa68da9583e8143b5426be4b34'

        self.name = 'gdb'
        self.version = '8.1'
        self.url = 'http://ftp.gnu.org/gnu/gdb/gdb-$version.tar.xz'
        self.depends = ['readline', 'zlib']
        autoload = '$p/$t/lib:$p/$t/lib64:$p/lib:$p/lib64'.replace(
            '$p', self.prefix_dir).replace('$t', self.target_triplet)
        self.configure_args += [
            '--with-system-readline',
            '--with-system-zlib',
            # Add path to load pthread db from for thread
            # debugging
            '--with-auto-load-dir=%s' % autoload,
            '--with-auto-load-safe-path=%s' % autoload
            ]
