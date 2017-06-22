from .base import GnuRecipe


class PkgConfRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PkgConfRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e74886879f3fbadce3798c0c4621d761' \
                      '68404009c0e79ad35616529d6977eae5'

        self.name = 'pkgconf'
        self.version = '1.3.7'
        self.url = 'https://distfiles.dereferenced.org/pkgconf/' \
                   'pkgconf-$version.tar.gz'
        self.configure_args = self.shell_args + [
            './configure',
            '--prefix=%s' % (self.prefix_dir),
            '--build=%s' % (self.build_triplet),
            '--target=%s' % (self.target_triplet),
            '--disable-host-tool',
            '--disable-maintainer-mode',
#                                '--with-libiconv=gnu'
            '--with-pkg-config-dir=%s/lib/pkgconfig:%s/lib64/pkgconfig:'
            '%s/share/pkgconfig' % (
                self.prefix_dir, self.prefix_dir, self.prefix_dir)
            ]

    def install(self):
        super(PkgConfRecipe, self).install()

        # If replacing pkg-config
        # ln -sf /usr/bin/pkgconf /usr/bin/pkg-config
