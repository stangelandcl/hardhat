import os
from .base import GnuRecipe, hash_file


class Bzip2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Bzip2Recipe, self).__init__(*args, **kwargs)
        self.url = 'http://www.bzip.org/1.0.6/bzip2-1.0.6.tar.gz'
        self.name = 'bzip2'
        self.sha256 = 'a2848f34fcd5d6cf47def00461fcb528' \
                      'a0484d8edef8208d6d2e2909dc61d9cd'
        self.version = '1.0.6'
        self.install_args += ['PREFIX=%s' % (self.prefix_dir)]

# shared is 20% slower on x86 according to docs
        self.build_shared = True
        self.lib_dir = os.path.join(self.prefix_dir, 'lib')

    def need_configure(self):
        return False

    def clean(self):
        super(Bzip2Recipe, self).clean()

        files = ['libbz2.so', 'libbz2.so.1.0', 'libbz2.so.%s' % (self.version)]
        for file in files:
            file = os.path.join(self.lib_dir, file)
            if os.path.exists(file):
                os.remove(file)

    def install(self):
        super(Bzip2Recipe, self).install()

        if self.build_shared:
            args = ['make', '-f', 'Makefile-libbz2_so', 'clean']
            self.log_dir('compile', self.directory, ' '.join(args))
            self.run_exe(args, self.directory, self.environment)

            args = ['make', '-f', 'Makefile-libbz2_so']
            self.log_dir('compile', self.directory, ' '.join(args))
            self.run_exe(args, self.directory, self.environment)

            args = ['cp',
                    'libbz2.so.%s' % (self.version),
                    self.lib_dir
                    ]
            self.log_dir('install', self.directory, ' '.join(args))
            self.run_exe(args, self.directory, self.environment)

            files = ['libbz2.so', 'libbz2.so.1.0']
            for file in files:
                file = os.path.join(self.lib_dir, file)
                os.symlink(os.path.join(self.lib_dir,
                                        'libbz2.so.%s' % (self.version)),
                           file)
