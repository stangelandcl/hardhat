from .base import PipBaseRecipe


class DocutilsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DocutilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '718c0f5fb677be0f34b781e04241c406' \
                      '7cbd9327b66bdd8e763201130f5175be'

        self.name = 'docutils'
        self.depends = []
        self.version = '0.13.1'
