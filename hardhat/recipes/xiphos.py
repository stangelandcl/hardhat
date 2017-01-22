from .base import GnuRecipe


class XiphosRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XiphosRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c937146383a4135d5514b78acd85a4f6' \
                      'cf2afccf91645791372e7aa6e509b9be'

        self.name = 'xiphos'
        self.version = '3a8f5d6d6f1c1bee01ccb5eaf9403e6eb9a77a31'
        self.depends = ['gtk3', 'gtkhtml', 'libxml2', 'python2', 'sword']
        self.url = 'https://github.com/crosswire/xiphos/' \
                   'archive/$version.tar.gz'
        self.configure_args = ['python2',
                               'waf',
                               'configure',
                               '--prefix=%s' % self.prefix_dir,
                               '--debug-level=optimized'
                               ]
        self.compile_args = ['python2', 'waf', 'build']
        self.install_args = ['python2', 'waf', 'install']
