from .base import SetupPyRecipe
import os


class PyProtobufRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(PyProtobufRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6a093cbdb6b40e593c508a03bc9a8842' \
                      '39c7bfb377b79d0c0bf43eafe007fb0e'

        self.name = 'protobuf'
        self.version = '3.0.0'
        self.url = 'https://github.com/google/protobuf/releases/download/' \
                   'v$version/protobuf-python-$version.tar.gz'

    def patch(self):
        self.directory = os.path.join(self.directory, 'python')
