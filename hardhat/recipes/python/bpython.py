import os
from .base import SetupPyRecipe
from hardhat.util import patch


class BPythonRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(BPythonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3f4f7a32416371da2ee0774726875ce6' \
                      '3d3f9fed8b58e5a9ad1580b33fd3cef7'

        self.depends = ['ncurses']
        self.pydepends = ['curtsies', 'greenlet', 'pygments', 'requests']
        self.name = 'bpython'
        self.version = '0.15'

    def patch(self):
        if self.python == 'python2':
            return

        self.log_dir('patch', self.directory, 'bpython => bpython3')
        filename = os.path.join(self.directory, 'setup.py')

        src = 'bpython = bpython.curtsies:main'
        dst = 'bpython3 = bpython.curtsies:main'
        patch(filename, src, dst)

        src = 'bpython-urwid = bpython.urwid:main [urwid]'
        dst = 'bpython3-urwid = bpython.urwid:main [urwid]'
        patch(filename, src, dst)

        src = 'bpdb = bpdb:main'
        dst = 'bpdb3 = bpdb:main'
        patch(filename, src, dst)
