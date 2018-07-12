from .base import PipBaseRecipe


class DocutilsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DocutilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '51e64ef2ebfb29cae1faa133b3710143' \
                      '496eca21c530f3f71424d77687764274'

        self.name = 'docutils'
        self.depends = []
        self.version = '0.14'
