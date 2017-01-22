from .base import GnuRecipe
from ..urls import Urls


class GetTextRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GetTextRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9c1781328238caa1685d7bc7a2e1dcf1' \
                      'c6c134e86b42ed554066734b621bd12f'

        self.name = 'gettext'
        self.version = '0.19.8'
        self.url = Urls.gnu_template(self.name, self.version, 'tar.xz')

        self.environment['LDFLAGS'] += ' -lm'
