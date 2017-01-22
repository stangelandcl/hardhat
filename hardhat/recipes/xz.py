from .base import GnuRecipe


class XZRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XZRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6ff5f57a4b9167155e35e6da8b529de6' \
                      '9270efb2b4cf3fbabf41a4ee793840b5'

        self.name = 'xz'  # includes liblzma
        self.version = '5.2.2'
        self.url = 'http://tukaani.org/xz/xz-$version.tar.bz2'
