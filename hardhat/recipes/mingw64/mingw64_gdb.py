from .base import Mingw64BaseRecipe


class Mingw64GdbRecipe(Mingw64BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64GdbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3dbd5f93e36ba2815ad0efab030dcd0c' \
                      '7b211d7b353a40a53f4c02d7d56295e3'

        self.name = 'mingw64-gdb'
        self.version = '8.0.1'
        self.url = 'http://ftp.gnu.org/gnu/gdb/gdb-$version.tar.xz'
        self.mingw64depends = ['zlib']
        autoload = '$p/$t/lib:$p/$t/lib64:$p/lib:$p/lib64'.replace(
            '$p', self.prefix_dir).replace('$t', self.target_triplet)
        self.configure_args += [
            #'--with-system-readline',
            '--with-system-zlib',
            # Add path to load pthread db from for thread
            # debugging
            '--with-auto-load-dir=%s' % autoload,
            '--with-auto-load-safe-path=%s' % autoload,
            '--enable-gold=no',
            '--without-x',
            '--without-tcl',
            '--without-tk',
            '--without-lzma',
            '--without-python',
            '--enable-tui',
            '--enable-64-bit-bfd',
            '--disable-rpath'
            '--disable-win32-registry'
            ]
        self.compile_args = ['make', '-j1']
