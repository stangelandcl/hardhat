import os
from .base import GnuRecipe


class PhpRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PhpRecipe, self).__init__(*args, **kwargs)
        self.name = 'php'
        self.version = '7.1.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools', 'bzip2',
                        'gdbm', 'gmp', 'libxml2', 'readline', 'zlib']
        self.url = 'http://www.php.net/distributions/php-$version.tar.xz'
        self.configure_args += [
            '--sysconfdir=%s/etc' % self.prefix_dir,
            '--localstatedir=%s/var' % self.prefix_dir,
            '--datadir=%s/share/php' % self.prefix_dir,
            '--mandir=%s/share/man' % self.prefix_dir,
            '--enable-fpm',
            '--with-fpm-user=%s' % os.environ['USER'],
            '--with-fpm-group=%s' % os.environ['USER'],
            '--with-config-file-path=%s/etc' % self.prefix_dir,
            '--with-zlib',
            '--enable-bcmath',
            '--with-bz2',
            '--enable-calendar',
            '--enable-dba=shared',
            '--with-gdbm',
            '--with-gmp',
            '--enable-ftp',
            '--with-gettext',
            '--enable-mbstring',
            '--with-readline']
