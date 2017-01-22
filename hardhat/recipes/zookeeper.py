import os
from .base import GnuRecipe


class ZookeeperRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ZookeeperRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e7f340412a61c7934b5143faef8d1352' \
                      '9b29242ebfba2eba48169f4a8392f535'

        self.name = 'zookeeper'
        self.version = '3.4.9'
        self.url = 'http://www-us.apache.org/dist/zookeeper/stable/' \
                   'zookeeper-$version.tar.gz'
        self.configure_strip_cross_compile()
        self.environment['CFLAGS'] += ' -Wno-unused-but-set-variable'

    def patch(self):
        self.directory = os.path.join(self.directory, 'src', 'c')
