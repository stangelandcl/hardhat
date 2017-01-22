from .base import GnuRecipe
from ..urls import Urls


class GdbmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(GdbmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd97b2166ee867fd6ca5c022efee80702' \
                      'd6f30dd66af0e03ed092285c3af9bcea'

        self.name = 'gdbm'
        self.version = '1.12'
        self.url = Urls.gnu_template(self.name, self.version)
