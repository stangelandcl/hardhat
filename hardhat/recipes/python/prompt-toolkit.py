from .base import PipBaseRecipe


class PromptToolkitRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PromptToolkitRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'cd6523b36adc174cc10d54b1193eb626' \
                      'b4268609ff6ea92c15bcf1996609599c'

        self.name = 'prompt-toolkit'
        self.pydepends = ['wcwidth']
        self.version = '1.0.9'
