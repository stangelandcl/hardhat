import os
import shutil
from .base import GnuRecipe


class CheckRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CheckRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f5f50766aa6f8fe5a2df752666ca01a9' \
                      '50add45079aa06416b83765b1cf71052'

        self.description = 'Unit testing framework for C'
        self.name = 'check'
        self.version = '0.10.0'
        self.url = 'http://downloads.sourceforge.net/check/' \
                   'check-$version.tar.gz'

    def extract(self):
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)
        os.makedirs(self.directory)
        self.extract_into(self.filename, self.directory)
        self.directory = os.path.join(self.directory,
                                      self.name + '-' + self.version)
