import os
from .base import GnuRecipe
from ..util import get_groups


class SthttpdRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SthttpdRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '81e686d048b51752f3ef541d020d9033' \
                      '35b9210d561c0c565006ef4ac1d52f80'

        self.name = 'sthttpd'
        self.depends = ['autotools']
        self.version = 'aa3f36c0bf2aef1ffb17f5188ccf5e8afc13d3dc'
        self.url = 'https://github.com/blueness/$name/archive/' \
                   '$version.tar.gz'
        # Fix rpl_malloc undefined when cross-compiling.
        # See http://rickfoosusa.blogspot.com/2011/11/
        # howto-fix-undefined-reference-to.html
        self.configure_strip_cross_compile()        
        self.install_args = ['WEBGROUP=%s' % get_groups()[0]]

    def patch(self):
        self.log_dir('pre-configure', self.directory, 'autogen configure')
        args = self.shell_args + ['./autogen.sh']
        self.run_exe(args, self.directory, self.environment)
