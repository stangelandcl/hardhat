from .base import GnuRecipe


class Sqlite3Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Sqlite3Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '07b35063b9386865b78226cdaca9a299' \
                      'd938a87aaa8fdc4d73edb0cef30f3149'

        self.name = 'sqlite3'
        self.version = '3.15.2'
        # Doesn't work because version is not in href
        self.version_url = 'https://sqlite.org/download.html'
        self.version_regex = 'sqlite\-autoconf\-(?P<version>\d+)\.tar\.gz'
        self.url = 'https://www.sqlite.org/2016/sqlite-autoconf-3150200.tar.gz'
        self.depends = ['readline']
        self.configure_args += [
            '--enable-fts5',
            '--enable-json1',
            '--enable-readline',
            '--enable-threadsafe',
            '--enable-shared',
            '--enable-static',
            '--enable-dynamic-extensions'
            ]

        # firefox requires this
        self.environment['CFLAGS'] += ' -DSQLITE_SECURE_DELETE=1' \
            ' -DSQLITE_ENABLE_UNLOCK_NOTIFY=1' \
            ' -DSQLITE_ENABLE_DBSTAT_VTAB=1'

    def version_transform(self, v):
        return v[:1] + '.' + v[1:3] + '.' + v[4:]
