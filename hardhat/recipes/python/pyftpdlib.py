from .base import SetupPyRecipe


class PyFtpdLibRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(PyFtpdLibRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '88c1dc3daa8de9ff5b25fd57ae8cc439' \
                      '0b5d034f87f2396ebd93eeb8f6879972'
        self.description = 'ftp server. Run from a directory. port is 2121.' \
                           ' login is anonymous'
        self.name = 'pyftpdlib'
        self.version = '1.5.0'
        self.url = 'https://github.com/giampaolo/pyftpdlib/archive/' \
                   'release-$version.tar.gz'
