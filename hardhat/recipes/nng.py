from .base import GnuRecipe, SourceMixin


class NngRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NngRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '31dd7f2e7b8e5554a73837f1f2d1be10' \
                      'fc4c0cc75d70a5f491f756c107d81d9f'

        self.name = 'nng'
        self.version = '1.0.0-beta.1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['cmake']
        self.url = 'https://github.com/nanomsg/nng/archive/v$version.tar.gz'
        self.configure_args = self.cmake_args


class NngSourceRecipe(SourceMixin, NngRecipe):
    def __init__(self, *args, **kwargs):
        super(NngSourceRecipe, self).__init__(*args, **kwargs)
