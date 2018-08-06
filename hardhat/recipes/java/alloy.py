import os
from .base import JarBase


class AlloyRecipe(JarBase):
    def __init__(self, *args, **kwargs):
        super(AlloyRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '48ccd42563adf599374fada8b7aba4c8' \
                      'e2b47e73f5cd19af8cf9a6ce25da235d'

        self.name = 'alloy'
        self.version = '4.2_2015-02-22'
        self.url = 'http://alloytools.org/download/alloy$version.jar'
        self.version_url = 'http://alloytools.org/download.html'
        self.version_regex = 'alloy(?P<version>\d+\.\d+_\d\d\d\d\-\d\d\-\d\d)\.jar'
        self.installed_file = os.path.join(self.java_dir, 'bin', 'alloy.jar')
