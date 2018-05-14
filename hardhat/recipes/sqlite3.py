from .base import GnuRecipe


class Sqlite3Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Sqlite3Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '3757612463976e7d08c5e9f0af302161' \
                      '3fc24bbcfe1c51197d6776b9ece9ac5c'
        self.name = 'sqlite3'
        self.version = '3.23.1'
        # Doesn't work because version is not in href
        self.version_url = 'https://sqlite.org/download.html'
        self.version_regex = 'sqlite\-autoconf\-(?P<version>\d+)\.tar\.gz'
        self.url = 'https://www.sqlite.org/2017/sqlite-autoconf-3180000.tar.gz'
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
