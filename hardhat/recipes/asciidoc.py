from .base import GnuRecipe


class AsciiDocRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AsciiDocRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '78db9d0567c8ab6570a6eff7ffdf84ea' \
                      'dd91f2dfc0a92a2d0105d323cab4e1f0'

        self.name = 'asciidoc'
        self.version = '8.6.9'
        self.url = 'http://sourceforge.net/projects/asciidoc/files/asciidoc/' \
                   '$version/asciidoc-$version.tar.gz'
