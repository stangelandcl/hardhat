from .base import GnuRecipe


class LibCsvRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibCsvRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd9c0431cb803ceb9896ce74f683e6e5a' \
                      '0954e96ae1d9e4028d6e0f967bebd7e4'

        self.name = 'libcsv'
        self.version = '3.0.3'
        self.url = 'http://downloads.sourceforge.net/project/$name/$name/' \
                   '$name-$version/$name-$version.tar.gz'


#https://sourceforge.net/projects/libcsv/files/latest/download
#http://downloads.sourceforge.net/project/libcsv/libcsv/libcsv-3.0.3/libcsv-3.0.3.tar.gz?r=https%3A%2F%2Fsourceforge.net%2Fprojects%2Flibcsv%2F&ts=1471893694&use_mirror=pilotfiber
