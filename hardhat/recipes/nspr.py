import os
from .base import GnuRecipe


class NsprRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NsprRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5e4c1751339a76e7c772c0c04747488d' \
                      '7f8c98980b434dc846977e43117833ab'
        self.name = 'nspr'
        self.version = '4.13.1'
        self.version_regex = r'v(?P<version>\d+\.\d+(\.\d+)*)'
        self.version_url = 'https://ftp.mozilla.org/pub/mozilla.org/nspr/' \
                           'releases/'
        self.url = 'https://ftp.mozilla.org/pub/mozilla.org/nspr/releases/' \
                   'v$version/src/nspr-$version.tar.gz'

        self.configure_args += ['--with-mozilla',
                                '--with-pthreads',
                                '--enable-64bit']
        self.directory = os.path.join(self.directory, 'nspr')

    def patch(self):
        self.log_dir('patch', self.directory,
                     'disable installing unneeded scripts')
        # disable installing two unneeded scripts. from BLFS
        args = ['sed',
                '-ri',
                r"""'s#^(RELEASE_BINS =).*#\1#'""",
                'pr/src/misc/Makefile.in']
        self.run_exe(args, self.directory, self.environment)

        args = ['sed',
                '-i',
                r"""'s#$(LIBRARY) ##'""",
                'config/rules.mk']
        self.run_exe(args, self.directory, self.environment)
