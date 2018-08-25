import os
from ..util import patch
from .base import GnuRecipe


class MakeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MakeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd6e262bf3601b42d2b1e4ef8310029e1' \
                      'dcf20083c5446b4b7aa67081fdffc589'

        self.name = 'make'
        self.version = '4.2.1'
        self.url = 'http://ftp.gnu.org/gnu/make/make-$version.tar.bz2'
        self.configure_args += ['--without-guile']

    def patch(self):
        src = '#if !defined __alloca && !defined __GNU_LIBRARY__'
        dst = '#if 1'
        filename = os.path.join(self.directory, 'glob', 'glob.c')
        patch(filename, src, dst)

    def install(self):
        super(MakeRecipe, self).install()

        src = os.path.join(self.prefix_dir, 'bin', 'make')
        dst = os.path.join(self.prefix_dir, 'bin', 'gmake')
        if os.path.exists(dst):
            os.remove(dst)
        os.symlink(src, dst)


class MakeStaticRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MakeStaticRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd6e262bf3601b42d2b1e4ef8310029e1' \
                      'dcf20083c5446b4b7aa67081fdffc589'

        self.name = 'make-static'
        self.version = '4.2.1'
        self.url = 'http://ftp.gnu.org/gnu/make/make-$version.tar.bz2'
        self.configure_args += ['--without-guile',
                                '--without-dlmalloc',
                                'ac_cv_search_dlopen=no',
                                'ac_cv_have_decl_dlopen=no',
                                'ac_cv_search_getpwnam=no']
        self.compile_args += ['SHARED=0',
                              "CC='gcc -static' CFLAGS='-Os' LDFLAGS=''"]
        self.install_args = ['cp', 'make-static',
                             os.path.join(self.prefix_dir, 'bin', 'make-static')]

    def patch(self):
        src = '#if !defined __alloca && !defined __GNU_LIBRARY__'
        dst = '#if 1'
        filename = os.path.join(self.directory, 'glob', 'glob.c')
        patch(filename, src, dst)

        src = 'HAVE_GETPWNAM_R ||'
        dst = 'HAVE_GETPWNAM_R &&'
        patch(filename, src, dst)

        src = '!defined(_AMIGA) &&'
        dst = '!defined(_AMIGA) && 0 &&'
        filename = os.path.join(self.directory, 'read.c')
        patch(filename, src, dst)

    def compile(self):
        super(MakeStaticRecipe, self).compile()
        src = os.path.join(self.directory, 'make')
        dst = os.path.join(self.directory, 'make-static')
        os.rename(src, dst)
