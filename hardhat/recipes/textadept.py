import os
import shutil
from .base import GnuRecipe


class TextAdeptRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TextAdeptRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '47f352e86a73e91537e24e40da02dec8' \
                      'a9488581cfe1cf77bc55321fba340c58'
        self.name = 'textadept'
        self.version = '10.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://foicica.com/textadept/download/'
        self.url = 'https://foicica.com/textadept/download/' \
                   'textadept_$version.x86_64.tgz'
                   
    def configure(self):
        pass

    def compile(self):
        pass
        
    def install(self):
        self.log_dir('install', self.directory, 'install')
        dir = os.path.join(self.prefix_dir, 'textadept')
        if os.path.exists(dir):
            shutil.rmtree(dir)
        shutil.copytree(self.directory, dir)
        dst = os.path.join(self.prefix_dir, 'bin', 'textadept')
        if os.path.exists(dst):
            os.remove(dst)    
        os.symlink(os.path.join(dir, 'textadept'), dst)
        dst = os.path.join(self.prefix_dir, 'bin', 'textadept-curses')
        if os.path.exists(dst):
            os.remove(dst)        
        os.symlink(os.path.join(dir, 'textadept-curses'), dst)