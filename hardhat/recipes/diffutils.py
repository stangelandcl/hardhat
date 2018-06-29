import os
from .base import GnuRecipe
from ..urls import Urls


class DiffUtilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DiffUtilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd621e8bdd4b573918c8145f7ae61817d' \
                      '1be9deb4c8d2328a65cea8e11d783bd6'
        self.description = 'patch and diff'
        self.name = 'diffutils'
        self.version = '3.6'
        self.url = Urls.gnu_template(name=self.name,
                                     version=self.version,
                                     extension='tar.xz')
        self.configure_args +=['gl_cv_func_getopt_gnu=yes']
