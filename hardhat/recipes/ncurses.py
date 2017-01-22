import os
from .base import GnuRecipe
from ..urls import Urls


class NCursesRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NCursesRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f551c24b30ce8bfb6e96d9f59b42fbea' \
                      '30fa3a6123384172f9e7284bcf647260'

        self.name = 'ncurses'
        self.version = '6.0'
        self.url = Urls.gnu_template(self.name, self.version)

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
                                '--enable-ext-colors'
                                ]

    def post_install(self):
        lib_dir = os.path.join(self.prefix_dir, 'lib')

        def find_files(dir):
            filenames = next(os.walk(dir))[2]
            return [os.path.join(dir, f) for f in filenames]

        files = find_files(lib_dir)
        for file in files:
            filename = os.path.basename(file)
            is_lib = filename.startswith('libncursesw')
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
                if os.path.lexists(dest):
                    os.remove(dest)
                self.log_dir('install', self.directory,
                             'symlink %s to %s' % (file, dest))
                os.symlink(file, dest)

        include_dir = os.path.join(self.prefix_dir, 'include')
        ncurses_dir = os.path.join(include_dir, 'ncurses')
        ncursesw_dir = os.path.join(include_dir, 'ncursesw')
        if not os.path.exists(ncurses_dir):
            os.makedirs(ncurses_dir)

        ncursesw_files = find_files(ncursesw_dir)
        for file in ncursesw_files:
            filename = os.path.basename(file)
            include_file = os.path.join(include_dir, filename)
            ncurses_file = os.path.join(ncurses_dir, filename)

            if os.path.exists(include_file):
                os.remove(include_file)
            os.symlink(file, include_file)
            if os.path.exists(ncurses_file):
                os.remove(ncurses_file)
            os.symlink(file, ncurses_file)


        # update ldconfig
        super(NCursesRecipe, self).post_install()
