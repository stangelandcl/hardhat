from .base import GnuRecipe


class NsprRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NsprRecipe, self).__init__(*args, **kwargs)
        self.name = 'nspr'
        self.version = '4.13.1'
        self.version_regex = r'v(?P<version>\d+\.\d+(\.\d+)*)'
        self.version_url = 'https://ftp.mozilla.org/pub/mozilla.org/nspr/' \
                           'releases/'
        self.url = 'https://ftp.mozilla.org/pub/mozilla.org/nspr/releases/' \
                   'v$version/src/nspr-$version.tar.gz'

    def patch(self):
        self.log_dir('patch', self.directory,
                     'disable installing unneeded scripts')
        # disable installing two unneeded scripts. from BLFS
        args = ['sed',
                'ri',
                r"""'s#^(RELEASE_BINS =).*#\1#'""",
                'pr/src/misc/Makefile.in']
        self.run_exe(args, self.directory, self.environment)
