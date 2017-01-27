from .base import GnuRecipe


class GdbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GdbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '834ff3c5948b30718343ea57b11cbc32' \
                      '35d7995c6a4f3a5cecec8c8114164f94'

        self.name = 'gdb'
        self.version = '7.12'
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
