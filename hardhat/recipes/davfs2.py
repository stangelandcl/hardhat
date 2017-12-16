import os
from .base import GnuRecipe


class DavFS2Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DavFS2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c9c4e0f0912a782386216b2147eb9c36' \
                      'c47f193b8fcf3d637719e0b9fe7c96e0'
        self.name = 'davfs2'
        self.version = '1.5.4'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'http://download.savannah.nongnu.org/releases/davfs2/'
        self.depends = ['neon']
        self.url = 'http://download.savannah.nongnu.org/releases/davfs2/' \
                   'davfs2-$version.tar.gz'
        # Fix rpl_malloc undefined when cross-compiling.
        # See http://rickfoosusa.blogspot.com/2011/11/
        # howto-fix-undefined-reference-to.html
        self.configure_strip_cross_compile()
        self.sudo = True
        self.configure_args += ['dav_user=%s' % os.environ['USER']]
        self.configure_args += ['dav_group=%s' % os.environ['USER']]

    def install(self):
        self.log_dir('install', self.directory, 'installing')
        args = self.install_args
        self.run_sudo(args, self.directory, self.environment)
#        self.run_sudo(['groupadd', 'davfs2'], self.directory, self.environment)
#        self.run_sudo(['usermod', '-a', '-G', 'davfs2', os.environ['USER']], self.directory, self.environment)
