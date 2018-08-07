import os
from .base import GnuRecipe
from ..util import patch
from ..urls import Urls


class ManDBRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ManDBRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '103c185f9d8269b9ee3b8a4cb27912b3' \
                      'aa393e952731ef96fedc880723472bc3'
        self.name = 'man-db'
        self.version = '2.8.4'
        self.depends = ['groff', 'libpipeline']
        self.url = Urls.savannah(self.name, self.version, 'tar.xz')
        self.configure_args += [
            '--disable-setuid',
            '--oldincludedir=%s/include' % self.prefix_dir,
            '--with-systemdtmpfilesdir=%s/tmp' % self.prefix_dir,
#            '--with-sysroot=%s' % self.prefix_dir
            ]

    def patch(self):
        self.log_dir('patch', self.directory, 'appending to man path (man -w)')
        filename = '%s/src/man_db.conf.in' % self.directory
        src = 'MANDATORY_MANPATH\t\t\t/usr/man'
        dst = '''
MANDATORY_MANPATH\t\t\t%s/man
MANDATORY_MANPATH\t\t\t%s/share/man
MANDATORY_MANPATH\t\t\t%s/java/man
MANDATORY_MANPATH\t\t\t/usr/man
''' % (self.prefix_dir, self.prefix_dir, self.prefix_dir)
        patch(filename, src, dst)

    def install(self):
        man_conf = os.path.join(self.prefix_dir, 'etc', 'man_db.conf')
        if os.path.exists(man_conf):
            os.remove(man_conf)

        super(ManDBRecipe, self).install()
