import os
import shutil
from ..base import GnuRecipe


class JavaBase(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JavaBase, self).__init__(*args, **kwargs)

    @property
    def java_dir(self):
        if hasattr(self, '_java_dir'):
            return self._java_dir
        return os.path.join(self.prefix_dir, 'java')

    @java_dir.setter
    def java_dir(self, value):
        self._java_dir = value

    @property
    def install_dir(self):
        if hasattr(self, '_install_dir'):
            return self._install_dir
        return os.path.join(self.java_dir, self.name)

    @install_dir.setter
    def install_dir(self, value):
        self._install_dir = value

    def clean(self):
        if os.path.exists(self.install_dir):
            shutil.rmtree(self.install_dir)

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        shutil.copytree(self.directory, self.install_dir)
        src = os.path.join(self.install_dir, self.name)
        dst = os.path.join(self.java_dir, 'bin', self.name)
        if os.path.exists(dst):
            os.remove(dst)
        os.symlink(src, dst)
