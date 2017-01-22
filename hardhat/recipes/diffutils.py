from .base import GnuRecipe
from ..urls import Urls


class DiffUtilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DiffUtilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'dad398ccd5b9faca6b0ab219a036453f' \
                      '62a602a56203ac659b43e889bec35533'

        self.description = 'patch and diff'

        self.name = 'diffutils'
        self.version = '3.5'
        self.url = Urls.gnu_template(name=self.name,
                                     version=self.version,
                                     extension='tar.xz')
