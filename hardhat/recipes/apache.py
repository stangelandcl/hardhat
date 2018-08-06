from .base import GnuRecipe


class ApacheRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ApacheRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fa53c95631febb08a9de41fd2864cfff' \
                      '815cf62d9306723ab0d4b8d7aa1638f0'

        self.name = 'apache'
        self.version = '2.4.34'
        self.url = 'https://archive.apache.org/dist/httpd/' \
                   'httpd-$version.tar.bz2'
        self.version_url = r'''http://apache.cs.utah.edu/httpd/'''
        self.version_regex = r'''httpd\-(?P<version>\d+\.\d+\.\d+)\.tar\.gz'''
        self.configure_strip_cross_compile()
        self.configure_args += ['--build=%s' % self.target_triplet,
                                '--host=%s' % self.target_triplet]
