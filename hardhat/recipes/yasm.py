from .base import GnuRecipe


class YasmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(YasmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8309e82abce883f3adb54866bb45dfd1' \
                      '2f631e7b8274bf603021865d3a23ef16'
        self.name = 'yasm'
        self.version = 'e256985c4929f4e550d8f70cad5fb936f81b7b06'
        self.url = self.github_commit('yasm')
        self.configure_args = [['./autogen.sh'],
                               self.configure_args]
