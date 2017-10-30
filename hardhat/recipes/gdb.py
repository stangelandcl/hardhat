from .base import GnuRecipe


class GdbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GdbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3dbd5f93e36ba2815ad0efab030dcd0c' \
                      '7b211d7b353a40a53f4c02d7d56295e3'

        self.name = 'gdb'
        self.version = '8.0.1'
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
