import os
from .base import GnuRecipe


class LibFFIRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibFFIRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd06ebb8e1d9a22d19e38d63fdb839542' \
                      '53f39bedc5d46232a05645685722ca37'

        self.name = 'libffi'
        self.version = '3.2.1'
        self.url = 'ftp://sourceware.org/pub/$name/$name-$version.tar.gz'

        self.configure_strip_cross_compile()
        self.configure_args += ['--host=%s' % (self.host_triplet),
                                '--target=%s' % (self.target_triplet)
                                ]

    def patch(self):
        replace = 'includesdir = $(libdir)/@PACKAGE_NAME@-@PACKAGE_VERSION@' \
                  '/include'
        filename = os.path.join(self.directory, 'include', 'Makefile.in')
        with open(filename, 'rt') as f:
            text = f.read()
        text = text.replace(replace, 'includesdir = $(includedir)')
        with open(filename, 'wt') as f:
            f.write(text)

        replace = 'includedir=${libdir}/@PACKAGE_NAME@-@PACKAGE_VERSION@' \
                  '/include'
        filename = os.path.join(self.directory, 'libffi.pc.in')
        with open(filename, 'rt') as f:
            text = f.read()
        text = text.replace(replace, 'includedir=@includedir@')
        with open(filename, 'wt') as f:
            f.write(text)
