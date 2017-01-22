from .base import GnuRecipe


class HaskellPlatformRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(HaskellPlatformRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd747aaa51eb20a7c8b4de93fa2a0d07c' \
                      '3b54fc5f36bf50fcede1a332812656f7'
        self.name = 'haskell-platform'
        self.version = '8.0.1'
        self.depends = ['pcre', 'pkgconfig', 'xz', 'zlib']
        self.url = 'https://haskell.org/platform/download/$version/' \
                   'haskell-platform-$version-unknown-posix--full-x86_64.tar.gz'
