import os
from .base import JarBase


class AllowRecipe(JarBase):
    def __init__(self, *args, **kwargs):
        super(AllowRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b009873ede4a29e118af96a1fb7162c9' \
                      'f95a8cd189a7033e4ca6b26dda667703'

        self.name = 'alloy'
        self.version = '4.2'
        self.url = 'http://alloy.mit.edu/alloy/downloads/alloy$version.jar'
        self.installed_file = os.path.join(self.java_dir, 'bin', 'alloy.jar')
