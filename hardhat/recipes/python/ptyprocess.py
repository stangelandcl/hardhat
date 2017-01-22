from .base import PipBaseRecipe


class PtyProcessRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PtyProcessRecipe, self).__init__(*args, **kwargs)
        self.name = 'ptyprocess'
        self.version = '0.5.1'
        self.sha256 = '0530ce63a9295bfae7bd06edc02b6aa9' \
                      '35619f486f0f1dc0972f516265ee81a6'
