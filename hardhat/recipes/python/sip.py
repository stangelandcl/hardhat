from .base import PythonBaseRecipe
from ..base import GnuRecipe


class SipRecipe(PythonBaseRecipe, GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SipRecipe, self).__init__(*args, **kwargs)

        self.name = 'sip'
        self.depends = ['bison', 'flex', 'mercurial']
        self.version = '4.18'
        self.sha256 = 'f1dc5c81c07a9ad97edcd4a0af964a41' \
                      'e420024ba7ca165afd2b351efd249cb6'

        self.url = 'http://sourceforge.net/projects/pyqt/files/sip/' \
                   'sip-$version/sip-$version.tar.gz'

    def configure(self):
        self.configure_args = [self.python,
                               'configure.py',
                               '--sysroot=%s' % self.prefix_dir
                               ]
        super(SipRecipe, self).configure()
