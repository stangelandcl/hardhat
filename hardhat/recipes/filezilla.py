
from .base import GnuRecipe


class FileZillaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(FileZillaRecipe, self).__init__(*args, **kwargs)

        self.name = 'filezilla'
        self.version = '3.18.0'
        self.url = 'http://sourceforge.net/project/filezilla/FileZilla_Client/' \
                   '$version/FileZilla_$version_src.tar.bz2'
#http://heanet.dl.sourceforge.net/project/filezilla/FileZilla_Client/3.18.0/FileZilla_3.18.0_src.tar.bz2
