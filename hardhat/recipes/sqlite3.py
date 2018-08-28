from .base import GnuRecipe
from ..version import Versions


class Sqlite3Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Sqlite3Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd9d14e88c6fb6d68de9ca0d1f9797477' \
                      'd82fc3aed613558f87ffbdbbc5ceb74a'
        self.name = 'sqlite3'
        self.version = '3.24.0'
        # Doesn't work because version is not in href
        long_version = self.version.replace('.', '') + '000'

        self.url = 'https://www.sqlite.org/2018/sqlite-autoconf-%s.tar.gz' % \
            long_version
        self.version_url = 'https://sqlite.org/changes.html'
        self.version_regex = '\d\d\d\d-\d\d-\d\d [(](?P<version>\d+.\d+.\d+)[)]'

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

        # firefox and QT requires this
        self.environment['CFLAGS'] += \
            ' -DSQLITE_SECURE_DELETE=1' \
            ' -DSQLITE_ENABLE_UNLOCK_NOTIFY=1' \
            ' -DSQLITE_ENABLE_DBSTAT_VTAB=1' \
            ' -DSQLITE_ENABLE_COLUMN_METADATA=1'

#    def version_transform(self, v):
#        return v[:1] + '.' + v[1:3] + '.' + v[4:]

    def get_version_always(self):
        return Versions.get_non_link_versions(
            self.version_url, self.version_regex)
