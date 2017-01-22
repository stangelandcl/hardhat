from .base import GnuRecipe
from hardhat.urls import Urls


class Dos2UnixRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Dos2UnixRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5c910aea2eae96663c67e87627998c4f' \
                      'e3cded403be5819b4c190e56c82ff0fb'

        self.name = 'dos2unix'
        self.version = '7.3.3'
        self.url = Urls.sourceforge(
            self.name,
            '$name/$version/$name-$version.tar.gz')

        self.compile_args += ['prefix=%s' % self.prefix_dir]
        self.install_args += ['prefix=%s' % self.prefix_dir]
