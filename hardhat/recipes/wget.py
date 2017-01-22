from .base import GnuRecipe
from ..urls import Urls


class WGetRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(WGetRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a00a65fab84cc46e24c53ce88c456046' \
                      '68a7a479276e037dc2f558e34717fb2d'

        self.name = 'wget'
        self.version = '1.18'
        self.url = Urls.gnu_template(self.name, self.version)
