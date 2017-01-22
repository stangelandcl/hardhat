import os
import sys
import tarfile
from .util import Object


def open_tarball(filename):
    if filename.endswith('.xz'):
#        print('filename=', filename)
        if sys.version[0] == '2':
            try:
                from backports import lzma
            except ImportError:
                print('Error: backports.lzma is required in python 2 for xz' +
                      ' decompression')
                sys.exit(1)
        else:
            import lzma

        xz = lzma.LZMAFile(filename, 'rb')
        return tarfile.open(fileobj=xz)
    return tarfile.open(filename)


def base_dirname(name):
    last = name
    while name:
        last = name
        name = os.path.dirname(name)
    return last


class Tarball(Object):
    def __init__(self, filename):
        self.filename = filename

    def __enter__(self):
        self.tarball = open_tarball(self.filename)

        dirs = set()
        for member in self.tarball:
            dir = base_dirname(member.name)
            dirs.add(dir)
            if len(dirs) > 1:
                break
            self.tarball.members = []   # To decrease memory use
        self.replace_prefix = len(dirs) == 1
        # Close and re-open otherwise members are missing
        self.tarball.close()
        self.tarball = open_tarball(self.filename)
        return self

    def contents(self):
        for member in self.tarball:
            if self.replace_prefix:
                dir = member.name
                dir = dir[len(base_dirname(dir)) + 1:]
                member.name = dir
            yield member
            self.tarball.members = []  # To decrease memory use

    def extract(self, directory):
#        os.system('tar -czf %s %s/' % (self.filename, directory))
        for member in self.contents():
            self.tarball.extract(member, directory)

    def close(self):
        self.tarball.close()

    def __exit__(self, type, value, traceback):
        self.close()
