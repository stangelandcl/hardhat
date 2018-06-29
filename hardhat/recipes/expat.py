from .base import GnuRecipe


class ExpatRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ExpatRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd9dc32efba7e74f788fcc4f212a43216' \
                      'fc37cf5f23f4c2339664d473353aedf6'
        self.name = 'expat'  # includes liblzma
        self.version = '2.2.5'
        self.version_url = 'https://github.com/libexpat/libexpat/releases'
        self.version_regex = 'expat-(?P<version>\d+\.\d+\.\d+)\.tar\.bz2'
        self.url = 'https://downloads.sourceforge.net/project/expat/expat/' \
                   '$version/expat-$version.tar.bz2'
