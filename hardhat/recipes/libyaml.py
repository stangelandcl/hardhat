from .base import GnuRecipe


class LibYamlRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibYamlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8088e457264a98ba451a90b8661fcb4f' \
                      '9d6f478f7265d48322a196cec2480729'

        self.name = 'libyaml'
        self.version = '0.1.7'
        self.url = 'http://pyyaml.org/download/libyaml/yaml-0.1.7.tar.gz'
