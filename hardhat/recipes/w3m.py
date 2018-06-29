import os
import shutil
from .base import GnuRecipe


class W3mRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(W3mRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e994d263f2fd2c22febfbe45103526e0' \
                      '0145a7674a0fda79c822b97c2770a9e3'
        self.name = 'w3m'
        self.depends = ['gc', 'glib', 'libnsl']
        self.version = '0.5.3'
        self.version_url = 'https://sourceforge.net/projects/w3m/files/w3m/'
        self.url = 'http://downloads.sourceforge.net/project/w3m/w3m/' \
                   'w3m-$version/w3m-$version.tar.gz'

        self.configure_args += [
            '--disable-messagel10n',
            '--disable-help_cgi',
            '--with-charset=US-ASCII',
            '--enable-color',
            '--enable-cookie',
            '--enable-m17n',
            '--enable-mouse',
            '--enable-unicode',
            '--with-termlib=tinfow',
            '--with-editor=emacs',
            '--enable-image=no', # this could be changed
            '--with-browser=',
            'ac_cv_func_setpgrp_void=yes']

    def patch(self):
        # Replace file_handle with file_handle_rofl in istream.* files

        def replace(file, src, dest):
            filename = os.path.join(self.directory, file)
            with open(filename, 'rt') as f:
                text = f.read()
            text = text.replace(src, dest)
            with open(filename, 'wt') as f:
                f.write(text)

        files = ['istream.h', 'istream.c']
        for file in files:
            replace(file, 'file_handle', 'file_handle_rofl')
        replace('main.c',
                'orig_GC_warn_proc = GC_set_warn_proc(wrap_GC_warn_proc);',
                'GC_set_warn_proc(wrap_GC_warn_proc);')

        shutil.rmtree(os.path.join(self.directory, 'gc'))
