import os
import shutil
from .base import GnuRecipe


class FuseRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FuseRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ec632de07b79ec72a591f9878a6d090c' \
                      '249bdafb4e2adf47fa46dc681737b205'

        self.name = 'fuse'
        self.version = '3.0.2'
        self.depends = ['autotools', 'pcre', 'pkgconfig', 'xz', 'zlib']
        self.url = 'https://github.com/libfuse/libfuse/releases/download/' \
                   'fuse-$version/fuse-$version.tar.gz'

        # TODO: install documentation and examples

    def install(self):
        super(FuseRecipe, self).install()

        self.log_dir('install', self.directory, 'install docs and examples')

        dst = os.path.join(self.prefix_dir, 'share', 'doc', 'fuse')
        if os.path.exists(dst):
            shutil.rmtree(dst)

        os.makedirs(dst)

        src = os.path.join(self.directory, 'example')
        shutil.copytree(src, os.path.join(dst, 'example'))

        src = os.path.join(self.directory, 'doc', 'html')
        shutil.copytree(src, os.path.join(dst, 'html'))
