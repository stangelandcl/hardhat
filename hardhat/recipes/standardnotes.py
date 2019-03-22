from .base import GnuRecipe
import os
import shutil


class StandardNotesRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(StandardNotesRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4ebfe83945062d665c85034929b5d6d0' \
                      '83d6baf1229addf0f6a9e68c608a5241'
        self.doc = 'https://standardnotes.org note taking app syncs with mobile'
        self.name = 'standardnotes'
        self.version = '3.0.6'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.url = 'https://github.com/standardnotes/desktop/releases/' \
                   'download/v$version/standard-notes-$version-x86_64.AppImage'

    def extract(self):
        pass

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'installing to ' + self.prefix_dir + '/bin')
        args = ['chmod', '+x', self.filename]
        self.run_exe(args, '/tmp', self.environment)
        shutil.copy2(self.filename, os.path.join(self.prefix_dir, 'bin', 'standardnotes'))




