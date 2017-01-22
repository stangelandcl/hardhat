import os
import shutil
from string import Template
from hardhat.recipes.base import TarballRecipe


class GccPrereqRecipe(TarballRecipe):
    def __init__(self, *args, **kwargs):
        super(GccPrereqRecipe, self).__init__(*args, **kwargs)
        self.sha256 = None
        self.gcc_directory = None
        self.extension = 'tar.bz2'


    @property
    def simple_name(self):
        return self.name.replace('cross-', '')

    @property
    def url(self):
        return Template('ftp://gcc.gnu.org/pub/gcc/infrastructure/'
                        '$name-$version.%s' % (self.extension)).substitute(
                            name=self.simple_name, version=self.version)

    def install(self):
        link = os.path.join(self.gcc_directory, self.simple_name)
        self.log_dir('install', self.directory, 'link to ' + link)
        if os.path.exists(link):
            os.remove(link)
        os.symlink(self.directory, link)
        copy = os.path.join(self.gcc_directory,
                            self.simple_name + '-' + str(self.version))
        self.log_dir('install', self.directory, 'copy to ' + copy)
#        if os.path.exists(copy):
#            os.remove(copy)
#            shutil.rmtree(copy)
        shutil.copytree(self.directory, copy)

    def run(self):
        gcc_name = 'cross-gcc_%s' % (self.simple_name)
        reinstall = hasattr(self, 'reinstall') and self.reinstall
        if gcc_name not in self.install_file.installed or reinstall:
            self.download()
            self.extract()
            self.install()
            self.install_file.installed.add(gcc_name)
            self.install_file.save()
