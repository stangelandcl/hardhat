import os
from .base import GnuRecipe
from ..version import extension_regex


class PccRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PccRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '493a5b4fbec9e0eb54bb7f40666fdc3d' \
                      '4fbc7732268cc6bd0ab7d6457ae8a45e'
        self.description = 'broken Portable C compiler.' \
                           " It can't handle multiple include directories"
        self.name = 'pcc'
        self.version = '20170114'
        self.version_regex = r'pcc-(?P<version>\d+)' + extension_regex
        self.version_url = 'http://pcc.ludd.ltu.se/ftp/pub/pcc/'
        self.url = 'http://pcc.ludd.ltu.se/ftp/pub/pcc/pcc-$version.tgz'
        self.depends = ['bison']
        self.configure_args += [
            '--enable-tls',
            '--with-incdir=%s/include:%s/%s/include:%s/linux/include' %
            (self.prefix_dir,
             self.prefix_dir,
             self.target_triplet,
             self.prefix_dir),
            '--with-libdir=%s/lib' % self.prefix_dir
            ]


    def patch(self):
        pcc = os.path.join(self.prefix_dir, 'bin', 'pcc')
        if os.path.exists(pcc):
            os.remove(pcc)
