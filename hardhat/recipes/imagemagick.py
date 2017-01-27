import re
from .base import GnuRecipe
from ..version import extension_regex


class ImageMagickRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ImageMagickRecipe, self).__init__(*args, **kwargs)

        self.name = 'imagemagick'
        self.version_regex = r'ImageMagick\-(?P<version>\d+\.\d+\.\d+\-\d+)' \
            + extension_regex
        self.version_url = 'https://www.imagemagick.org/download/'
        # imagemagick only maintains one copy of their releases and
        # they change frequently. so just use whatever is there
        # TODO: set a mininmum version just in case
        self.version = self.get_version()[0]
        if self.version and self.version_compare('7.0.4-5') > 0:
            raise Exception("imagemagick version is lower than its old version")
        self.url = 'ftp://ftp.imagemagick.org/pub/ImageMagick/releases/' \
                   'ImageMagick-$version.tar.xz'

    def version_compare(self, new_version):
        regex = r'\d+'
        v1 = re.findall(regex, new_version)
        v2 = re.findall(regex, self.version)

        for i in range(4):
            x = int(v1[i])
            y = int(v2[i])

            if x > y:
                return 1
            if x < y:
                return -1
        return 0
