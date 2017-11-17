import os
from .base import GnuRecipe


class NoIpClientRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NoIpClientRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '82b9bafab96a0c53b21aaef688bf70b3' \
                      '572e26217b5e2072bdb09da3c4a6f593'

        self.name = 'noip-client'
        self.version = '2.1.9-1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.url = 'https://www.noip.com/client/linux/noip-duc-linux.tar.gz'
        self.install_args += ['PREFIX=%s' % self.prefix_dir]

    def configure(self):
        self.directory = os.path.join(self.directory, 'noip-%s' % self.version)

    def compile(self):
        pass
