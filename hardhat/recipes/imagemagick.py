import re
from .base import GnuRecipe
from ..version import extension_regex


class ImageMagickRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ImageMagickRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'bc09ea103a82d1c2c093889eda7e36dd' \
                      '0aa7aa98a06c55de4b73932838459fc4'

        self.name = 'imagemagick'
        self.version = '7.0.4-3'
        self.version_regex = r'ImageMagick\-(?P<version>\d+\.\d+\.\d+\-\d+)' \
            + extension_regex
        self.version_url = 'https://www.imagemagick.org/download/'
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
