from .base import GnuRecipe


class PoptRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PoptRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e728ed296fe9f069a0e005003c3d6b2d' \
                      'de3d9cad453422a10d6558616d304cc8'

        self.name = 'popt'
        self.version = '1.16'
        self.url = 'http://rpm5.org/files/popt/popt-$version.tar.gz'
        self.depends = ['doxygen']

        self.compile_args = [
            self.compile_args,
            ['doxygen']]

        doc = '%s/share/doc/popt-%s' % (self.prefix_dir, self.version)
        self.install_args = [
            self.install_args,
            ['install', '-v', '-m755', '-d', doc],
            ['install', '-v', '-m644', 'doxygen/html/*', doc]]
