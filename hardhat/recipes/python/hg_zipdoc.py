import os
import shutil
from ..base import Downloader, Extractor, Recipe


class HgZipDocRecipe(Downloader, Extractor, Recipe):
    def __init__(self, *args, **kwargs):
        super(HgZipDocRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '0de7075c9be80856f3a1c8968f42cfa0' \
                      '9c44d09068b49c6c67dbf641b55ba8b9'

        self.pythons = ['python2']
        self.name = 'hg-zipdoc'
        self.version = '57b36658dbdf'
        self.url = 'https://bitbucket.org/cstangeland/hg-zipdoc/get/' \
                   '$version.tar.gz'

    def install(self):
        src = os.path.join(self.directory, 'zipdoc.py')
        dst = os.path.join(self.prefix_dir, 'etc', 'mercurial', 'zipdoc.py')
        dir = os.path.dirname(dst)
        if not os.path.exists(dir):
            os.makedirs(dir)
        shutil.copy2(src, dst)
