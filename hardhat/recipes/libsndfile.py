from .base import GnuRecipe


class LibSndFileRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibSndFileRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a391952f27f4a92ceb2b4c06493ac107' \
                      '896ed6c76be9a613a4731f076d30fac0'

        self.name = 'libsndfile'
        self.version = '1.0.27'
        self.url = 'http://www.mega-nerd.com/libsndfile/files/' \
                   'libsndfile-$version.tar.gz'
