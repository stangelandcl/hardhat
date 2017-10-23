import os
import shutil
from .base import GnuRecipe
from ..util import patch
from ..version import extension_regex


class LmdbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LmdbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '108532fb94c6f227558d45be3f3347b5' \
                      '2539f0f58290a7bb31ec06c462d05326'

        self.name = 'lmdb'
        self.version = '0.9.19'
        self.version_regex = 'LMDB_(?P<version>\d+\.\d+\.\d+)' \
            + extension_regex
        self.version_url = 'https://github.com/LMDB/lmdb/releases'
        self.url = 'https://github.com/LMDB/lmdb/archive/LMDB_$version.tar.gz'

        self.compile_args += [
            'XCFLAGS="-DMDB_MAXKEYSIZE=1800"',
            'OPT="%s"' % self.environment['OPT'],
            ]

        self.install_args += [
            'prefix=""',
            'DESTDIR=%s' % (self.prefix_dir)]

    def extract(self):
        super(LmdbRecipe, self).extract()
        self.directory = os.path.join(self.directory, 'libraries', 'liblmdb')

    def configure(self):
        pass


class Mingw64LmdbRecipe(LmdbRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64LmdbRecipe, self).__init__(*args, **kwargs)
        self.name = 'mingw64-lmdb'

    def install(self):
        super(LmdbRecipe, self).install()

        self.log_dir('install', self.directory,
                     'installing import lib')
        libdir = os.path.join(self.prefix_dir, 'lib')
        for file in ['liblmdb.dll.a']:
            src = os.path.join(self.directory, file)
            dst = os.path.join(libdir, file)
            shutil.copy2(src, dst)

    def patch(self):
        extra = []
        self.deffile = os.path.join(self.prefix_dir, 'lib', 'liblmdb.def')
        extra = ['CC=%s' % self.environment['CC'],
                 'AR=%s' % self.environment['AR'],
                 'SOEXT=.dll']
        self.compile_args += extra
        self.install_args += extra
        self.environment['SOLDFLAGS'] = self.environment['LDFLAGS'] + \
            ' %s -Wl,--out-implib,liblmdb.dll.a ' % self.deffile

        text = r'''EXPORTS
mdb_version
mdb_strerror
mdb_env_create
mdb_env_open
mdb_env_copy
mdb_env_copyfd
mdb_env_copy2
mdb_env_copyfd2
mdb_env_stat
mdb_env_info
mdb_env_sync
mdb_env_close
mdb_env_set_flags
mdb_env_get_flags
mdb_env_get_path
mdb_env_get_fd
mdb_env_set_mapsize
mdb_env_set_maxreaders
mdb_env_get_maxreaders
mdb_env_set_maxdbs
mdb_env_get_maxkeysize
mdb_env_set_userctx
mdb_env_get_userctx
mdb_env_set_assert
mdb_txn_begin
mdb_txn_env
mdb_txn_id
mdb_txn_commit
mdb_txn_abort
mdb_txn_reset
mdb_txn_renew
mdb_dbi_open
mdb_stat
mdb_dbi_flags
mdb_dbi_close
mdb_drop
mdb_set_compare
mdb_set_dupsort
mdb_set_relfunc
mdb_set_relctx
mdb_get
mdb_put
mdb_del
mdb_cursor_open
mdb_cursor_close
mdb_cursor_renew
mdb_cursor_txn
mdb_cursor_dbi
mdb_cursor_get
mdb_cursor_put
mdb_cursor_del
mdb_cursor_count
mdb_cmp
mdb_dcmp
mdb_reader_list
mdb_reader_check
'''
        with open(self.deffile, 'wt') as f:
            f.write(text)

        src = '$(LDFLAGS) -pthread'
        dst = '$(SOLDFLAGS) -pthread'
        filename = os.path.join(self.directory, 'Makefile')
        patch(filename, src, dst)
