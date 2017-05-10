from .base import GnuRecipe


class TreRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(TreRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd2810576685b10c6bf9270793550032b' \
                      'dada04afd963fa4670a08fdc57859bdd'

        self.description = 'Regex library'
        self.name = 'tre'
        self.version = '6fb7206b935b35814c5078c20046dbe065435363'
        self.url = self.github_commit('laurikari')

        self.configure_args = [
            ['./utils/autogen.sh'],
            self.configure_args]
