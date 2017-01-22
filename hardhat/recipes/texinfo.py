from .base import GnuRecipe
from ..urls import Urls


class TexInfoRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TexInfoRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '246cf3ffa54985118ec2eea2b8d0c71b' \
                      '92114efe6282c2ae90d65029db4cf93a'

        self.name = 'texinfo'
        self.version = '6.3'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')
