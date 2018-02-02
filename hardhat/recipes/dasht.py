import os
import shutil
from .base import GnuRecipe

class Extra:
    def __init__(self, name):
        self.name = name
        self.sha256 = None
        self.version = '1.0'
        self.url = None


class DashtRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(DashtRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ba3e20b351c0c0b4bd526d306c577e10' \
                      '4414656a9ac011d672cb46892d394030'
        self.name = 'dasht'
        self.version = '2.2.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['gawk', 'socat', 'sqlite3', 'w3m', 'wget']
        self.url = 'https://github.com/sunaku/dasht/archive/v$version.tar.gz'
        self.documentation = r'''
Usage

First, install some docsets using dasht-docsets-install(1):

dasht-docsets-install bash

Next, perform a direct search from the terminal using dasht(1):

dasht 'c - x'

Then, repeat the search in a web browser using dasht-server(1):

dasht-server

You are now ready to use dasht! Read the manuals below to learn even more.
'''

        self.msdn = Extra('msdn')
        self.msdn.url = 'http://rotemy.com/dash/msdn/msdn.tgz'
        self.msdn.sha256 = '081d9c3961024355497a68a521acc90ecf5ea81b3a689032c02770bbb8d6562e'
        self.extra_downloads.append(self.msdn)

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'installing')

        src = os.path.join(self.directory, 'bin')
        dst = os.path.join(self.prefix_dir, 'bin')
        for name in os.listdir(src):
            src_file = os.path.join(src, name)
            dst_file = os.path.join(dst, name)
            shutil.copy2(src_file, dst_file)


        src = os.path.join(self.directory, 'man', 'man1')
        dst = os.path.join(self.prefix_dir, 'man', 'man1')
        if not os.path.exists(dst):
            os.makedirs(dst)
        for name in os.listdir(src):
            src_file = os.path.join(src, name)
            dst_file = os.path.join(dst, name)
            shutil.copy2(src_file, dst_file)

        self.log_dir('install', self.directory, 'installing docsets')

        docsets = [
            'Bash',
            'Boost',
            'C',
            'C++',
            'CMake',
            'Emacs_Lisp',
            'NET_Framework',
            'Python_3',
            'R',
            'SQLite',
            'Tcl']

        for docset in docsets:
            args = ['dasht-docsets-install', '--force', r"""'^%s$'""" % docset]
            self.run_exe(args, self.directory, self.environment)

        args = ['dasht-docsets-extract', self.msdn.filename]
        self.run_exe(args, self.directory, self.environment)
