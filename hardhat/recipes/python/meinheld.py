from .base import PipBaseRecipe


class MeinheldHttpRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(MeinheldHttpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6338e66cb36bc24de1c1a71bca70e2c9' \
                      '50c3e42fbb300cf64b486b3360c1c757'

        self.depends = ['python-greenlet']
        self.name = 'meinheld'
        self.version = '0.5.9'
