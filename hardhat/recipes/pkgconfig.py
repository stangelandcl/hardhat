from .base import GnuRecipe


class PkgConfigRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PkgConfigRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'beb43c9e064555469bd4390dcfd8030b' \
                      '1536e0aa103f08d7abf7ae8cac0cb001'
        self.name = 'pkgconfig'
        self.version = '0.29.1'
        self.url = 'https://pkg-config.freedesktop.org/releases/' \
                   'pkg-config-$version.tar.gz'
        self.build_triplet = self.target_triplet
        self.configure_args = self.shell_args + [
                               './configure',
                               '--prefix=%s' % (self.prefix_dir),
                               '--build=%s' % (self.build_triplet),
                               '--target=%s' % (self.target_triplet),
                               '--with-internal-glib',
                               '--disable-host-tool',
                               '--disable-maintainer-mode'
    #                                '--with-libiconv=gnu'
                                ]
