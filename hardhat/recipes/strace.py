from .base import GnuRecipe


class StraceRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(StraceRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e86a5f6cd8f941f67f3e4b28f4e60f3d' \
                      '9185c951cf266404533210a2e5cd8152'

        self.name = 'strace'
        self.version = '4.11'
        self.url = 'https://downloads.sourceforge.net/project/strace/strace/' \
                   '$version/strace-$version.tar.xz'
