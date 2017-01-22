from .base import GnuRecipe


class ApacheRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ApacheRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ac660b47aaa7887779a6430404dcb40c' \
                      '0b04f90ea69e7bd49a40552e9ff13743'

        self.name = 'apache'
        self.version = '2.4.16'
        self.url = 'https://archive.apache.org/dist/httpd/' \
                   'httpd-$version.tar.bz2'

        self.configure_strip_cross_compile()
        self.configure_args += ['--build=%s' % self.target_triplet,
                                '--host=%s' % self.target_triplet]
