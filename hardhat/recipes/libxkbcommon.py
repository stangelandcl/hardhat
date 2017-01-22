from .base import GnuRecipe
from ..version import extension_regex


class LibXkbCommonRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibXkbCommonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '09351592312d67b438655f54da5b6785' \
                      '3026662c4a57e6be4d225f04a9989798'

        self.name = 'libxkbcommon'
        self.version = '0.7.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)' + extension_regex
        self.depends = ['xkeyboard-config', 'libxcb']
        self.url = 'http://xkbcommon.org/download/libxkbcommon-$version.tar.xz'
