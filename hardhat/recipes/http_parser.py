import os
from .base import GnuRecipe
from hardhat.util import patch


class HttpParserRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(HttpParserRecipe, self).__init__(*args, **kwargs)
        self.description = 'C http-parser library'

        self.sha256 = 'b0c5bf03fe9a57c4e63760d19d5a51d3' \
                      '063e0502cae54b3a8f2f6c6eb6911167'

        self.name = 'http-parser'
        self.version = '2.7.0'
        self.url = 'https://github.com/nodejs/http-parser/archive/' \
                   'v$version.tar.gz'

        prefix = ['PREFIX=%s' % self.prefix_dir]
        self.compile_args += prefix
        self.install_args += prefix

    def patch(self):
        self.log_dir('patch', self.directory, 'disable warnings as errors')
        filename = os.path.join(self.directory, 'Makefile')
        src = '-Werror'
        dst = ''
        patch(filename, src, dst)
