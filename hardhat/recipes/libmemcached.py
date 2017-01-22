from .base import GnuRecipe


class LibMemcachedRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibMemcachedRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e22c0bb032fde08f53de9ffbc5a12823' \
                      '3041d9f33b5de022c0978a2149885f82'

        self.name = 'libmemcached'
        self.depends = ['wget']
        self.version = '1.0.18'
        self.url = 'https://launchpad.net/libmemcached/%s/$version/' \
                   '+download/libmemcached-$version.tar.gz' \
                   % self.short_version
        self.configure_args += ['LIBUUID_LIB=-luuid']

    def install(self):
        super(LibMemcachedRecipe, self).install()
        docdir = '%s/doc/docs.libmemcached.org' % self.prefix_dir
        args = [
            ['wget', '--recursive', '--page-requisites',
             '--html-extension', '--convert-links', '--domains',
             'libmemcached.org',
             '--no-parent', 'http://docs.libmemcached.org/'],
            ['rm', '-rf', docdir],
            ['cp', '-R', 'docs.libmemcached.org', docdir]]

        for arg_list in args:
            self.log_dir('install', self.directory, ' '.join(arg_list))
            try:
                self.run_exe(arg_list, self.directory, self.environment)
            except Exception:
                if arg_list[0] != 'wget':
                    raise
