import os
from .base import GnuRecipe
from ..util import patch


class SqshRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(SqshRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd6641f365ace60225fc0fa48f82b9dbe' \
                      'd77a4e506a0e497eb6889e096b8320f2'
        self.name = 'sqsh'
        self.version = '2.5.16.1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['freetds']
        self.url = 'http://downloads.sourceforge.net/sqsh/' \
                   'sqsh-$version.tgz'
        self.environment['SYBASE'] = self.prefix_dir
        self.configure_strip_cross_compile()

    def patch(self):
        self.log_dir('patch', self.directory, 'downgrade TDS version')
        filename = os.path.join(self.directory, 'src', 'cmd_connect.c')
        src = 'CS_TDS_80'
        dst = 'CS_TDS_73'
        patch(filename, src, dst)
