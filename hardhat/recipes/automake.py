import os
from .base import GnuRecipe
from ..urls import Urls
from hardhat.util import patch


class AutoMakeRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AutoMakeRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '608a97523f97db32f1f5d5615c98ca69' \
                      '326ced2054c9f82e65bade7fc4c9dea8'
        self.name = 'automake'
        self.version = '1.16.1'
        self.depends = ['autoconf', 'help2man', 'perl5']
        self.url = Urls.gnu_template(self.name, self.version)
        self.configure_args += ['HELP2MAN=false']
        self.compile_args += ['HELP2MAN=true']

    def patch(self):
        return

    # This was needed for an old version
        src = r'''update_mans = \
  $(AM_V_GEN): \
    && $(MKDIR_P) doc \
    && $(extend_PATH) \
    && $(PERL) $(srcdir)/doc/help2man --output=$@
'''

        dst = 'update_mans = true'
        filename = os.path.join(self.directory, 'Makefile.in')
        patch(filename, src, dst)

        for dir in [os.path.join(self.directory, 'doc', 'aclocal-%s.1' % self.version),
                    os.path.join(self.directory, 'doc', 'automake-%s.1' % self.version)]:
            if not os.path.exists(dir):
                with open(dir, 'wt') as f:
                    f.write('')
