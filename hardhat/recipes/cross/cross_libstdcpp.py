import os
from hardhat.util import patch
from .base import CrossGnuRecipe
from .cross_gcc import CrossGcc1Recipe


class CrossLibStdCppRecipe(CrossGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossLibStdCppRecipe, self).__init__(*args, **kwargs)
        self.name = 'cross-libstdc++'
        gcc = CrossGcc1Recipe(settings=self)
        self.version = gcc.version
        self.directory = self.directory + '-build'
        if not os.path.exists(self.directory):
            os.makedirs(self.directory)

        self.configure_args = self.shell_args + [
            '%s/libstdc++-v3/configure' % gcc.extract_dir,
            '--host=%s' % self.target_triplet,
            '--prefix=%s/%s' % (self.cross_prefix_dir,
                                self.target_triplet),
            '--disable-multilib',
            '--disable-nls',
            '--disable-libstdcxx-threads',
            '--disable-libstdcxx-pch',
 #           '--libdir=%s/%s/lib' % (self.cross_prefix_dir,
 #                                   self.target_triplet),
 #           '--libexecdir=%s/%s/lib' % (self.cross_prefix_dir,
 #                                       self.target_triplet),
            '--with-gxx-include-dir=%s/%s/include/c++/%s' % (
                self.cross_prefix_dir,
                self.target_triplet,
                gcc.version
            )]

#        self.environment['CC'] = self.target_triplet + '-gcc'
#        self.environment['CXX'] = self.target_triplet + '-g++'
#        self.environment['AR'] = self.target_triplet + '-ar'
#        self.environment['RANLIB'] = self.target_triplet + '-ranlib'

#    def configure(self):
#        super(CrossLibStdCppRecipe, self).configure()
#        file = os.path.join(self.directory, 'Makefile')
#        self.log_dir('configure', self.directory,
#                     'patching Makefile to remove lib64')
#        patch(file,
#              'glibcxx_toolexeclibdir = ${libdir}/../lib64',
#              'glibcxx_toolexeclibdir = ${libdir}')

    def version_check(self):
        pass

    def download(self):
        pass

    def extract(self):
        pass

    def post_install(self):
        # skip ldconfig
        pass
