from .base import GnuRecipe


class ProtobufRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ProtobufRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '318e8f375fb4e5333975a40e0d1215e8' \
                      '55b4a8c581d692eb0eb7df70db1a8d4e'

        self.name = 'protobuf'
        self.version = '3.0.0'
        self.url = 'https://github.com/google/protobuf/releases/download/' \
                   'v$version/protobuf-cpp-$version.tar.gz'
