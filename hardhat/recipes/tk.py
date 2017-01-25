import os
from .base import GnuRecipe
from ..version import extension_regex


class TkRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TkRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fbbd93541b4cd467841208643b4014c4' \
                      '543a54c3597586727f0ab128220d7946'

        self.name = 'tk'
        self.rebuilds = ['graphviz']
        self.depends = ['tcl', 'xorg-libs']
        self.version = '8.6.5'
        self.version_regex = self.name + r'(?P<version>\d+d.\d+\.\d+)-src' \
            + extension_regex
        self.version_url = 'https://tcl.tk/software/tcltk/download.html'
        self.url = 'http://downloads.sourceforge.net/tcl/' \
                   '$name$version-src.tar.gz'

        self.configure_strip_cross_compile()
        self.environment['LIBS'] += ' -lm'

    @property
    def directory(self):
        d = super(TkRecipe, self).directory
        return os.path.join(d, 'unix')

    def compile(self):
        try:
            super(TkRecipe, self).compile()
        except Exception as e:
            print('ignoring compile error: %s' % e)
