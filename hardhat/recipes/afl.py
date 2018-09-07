from .base import GnuRecipe


class AflRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(AflRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '43614b4b91c014d39ef086c5cc84ff5f' \
                      '068010c264c2c05bf199df60898ce045'
        self.description = 'American fuzzy lop - fuzzer'
        self.name = 'afl'
        self.version = '2.52b'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['autotools']
        self.url = 'http://lcamtuf.coredump.cx/afl/releases/afl-$version.tgz'
