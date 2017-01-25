import os
import shutil
import sys
from string import Template
from hardhat.util import patch
from .base import GnuRecipe


class RRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(RRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd294ad21e9f574fb4828ebb3a94b8cb3' \
                      '4f4f304a41687a994be00dd41a4e514c'

        self.name = 'r'
        self.version = '3.3.2'
        self.version_prefix = 'R'

        self.url = 'http://cran.mtu.edu/src/base/R-3/R-$version.tar.gz'
        # libssh2 required by some R libraries
        # the MASS package installed in the R build requires libtinfo.so.5
        # (ncurses 5)
        self.depends = ['bash', 'bzip2', 'curl', 'libpng', 'libtiff',
                        'libssh2',
                        'ncurses5', 'openblas',
                        'pcre', 'posix', 'readline', 'texlive', 'xz', 'zlib']
        self.environment['LD_RUN_PATH'] = Template('$prefix/lib:$prefix/lib64:'
                                                   '$prefix/$target/lib:'
                                                   '$prefix/$target/lib64:'
                                                   '$prefix/lib64/R/lib') \
            .substitute(prefix=self.prefix_dir, target=self.target_triplet)
        self.configure_strip_cross_compile()
#        self.environment_strip_lto()
        self.configure_args += ['--enable-R-shlib',
                                '--enable-R-static-lib',
                                '--enable-BLAS-shlib',
                                '--enable-lto',
                                '--with-blas',
                                '--with-lapack',
                                '--with-x=no',
                                '--with-system-pcre',
                                '--without-recommended-packages',
                                ]

    def compile(self):
        try:
            super(RRecipe, self).compile()
        except:
            pass  # run once to build libR.so


        # install libR.so so the next build can reference it
        dir = os.path.join(self.directory, 'lib')
        for file in os.listdir(dir):
            filename = os.path.join(dir, file)
            dst = os.path.join(self.prefix_dir, 'lib64', 'R', 'lib')
            if not os.path.exists(dst):
                os.makedirs(dst)
            dst = os.path.join(dst, file)
            shutil.copy2(filename, dst)


        super(RRecipe, self).compile()

        # run ldconfig so R can find libR.so
        super(RRecipe, self).post_install()

        # Compile again. R will use the installed libR.so not the
        # just compiled version
        super(RRecipe, self).compile()


    def patch(self):
#        src = r'''(eval "$ac_compile") 2>conftest.err'''
#        dst = r'''
#env
#(eval "$ac_compile") 2>conftest.err'''

        filename = os.path.join(self.directory, 'configure')
 #       patch(filename, src, dst)

        src = 'shlibpath_var=LD_LIBRARY_PATH'
        dst = 'shlibpath_var=LD_RUN_PATH'
        patch(filename, src, dst)

        src = r'  exit(strncmp(ZLIB_VERSION, "1.2.5", 5) < 0);'
        dst = r'  exit(0); /* Always >= 1.2.5 */'
        patch(filename, src, dst)

        # Strip all the LD_LIBRARY_PATH garbage
        filename = os.path.join(self.directory, 'etc', 'ldpaths.in')
        with open(filename, 'rt') as f:
            text = '\n'.join(f.readlines()[:2])
        with open(filename, 'wt') as f:
            f.write(text)

#    def install(self):
#        filename = os.path.join(self.directory, 'etc', 'Makeconf')
#        src = '-O3'
#        dst = '-O2'
#        patch(filename, src, dst)

#        super(RRecipe, self).install()
