import os
import shutil
from .base import GnuRecipe
from ..urls import Urls
from ..util import patch


class NCurses5Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NCurses5Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'aa057eeeb4a14d470101eff4597d5833' \
                      'dcef5965331be3528c08d99cebaa0d17'
        self.name = 'ncurses5'
        self.version = '6.1'
        self.url = Urls.gnu_template('ncurses', self.version)

        self.configure_args += ['--without-libtool',
                                '--with-shared',
                                '--with-cxx-shared',
                                '--without-normal',
                                '--without-debug',
                                '--enable-widec',
                                '--enable-pc-files',
                                '--enable-termcap',
                                '--enable-getcap',
                                '--enable-tcap-names',
                                '--with-termlib',
                                '--enable-ext-colors',
                                '--with-abi-version=5',
                                '--without-tests'
                                ]
        self.compile_args += ['sources', 'libs']

    def patch(self):
        filename = os.path.join(self.directory, 'ncurses', 'base', 'new_pair.c')
        src = 'if (_nc_reserve_pairs(sp, pair) == 0) {'
        dst = 'if (_nc_reserve_pairs(SP_PARM, pair) == 0) {'
        patch(filename, src, dst)

    def install(self):
        src = os.path.join(self.directory, 'lib')
        for file in os.listdir(src):
            filename = os.path.join(src, file)
            if file.startswith('lib') and '.so.5' in filename:
                dst = os.path.join(self.prefix_dir, 'lib', file)
                self.log_dir('install', self.directory, 'copying ' + filename)
                shutil.copy2(filename, dst)

        lib_dir = os.path.join(self.prefix_dir, 'lib')

        def find_files(dir):
            filenames = next(os.walk(dir))[2]
            return [os.path.join(dir, f) for f in filenames]

        files = find_files(lib_dir)
        for file in files:
            filename = os.path.basename(file)
            is_lib = filename.startswith('libncursesw')
            is_lib = is_lib and '.so.5' in filename
            is_lib = is_lib or filename.startswith('libtinfow')
            is_lib = is_lib or filename.startswith('libtpanelw')
            is_lib = is_lib or filename.startswith('libformw')
            is_lib = is_lib or filename.startswith('libmenuw')

            if is_lib:
                name, ext = os.path.splitext(filename)
                i = name.find('w')
                if i < 0:
                    continue
                name = name[:i] + name[i+1:]
                dest = os.path.join(lib_dir, name + ext)
                if os.path.exists(dest):
                    os.remove(dest)
                self.log_dir('install', self.directory,
                             'symlink %s to %s' % (file, dest))
                os.symlink(file, dest)
