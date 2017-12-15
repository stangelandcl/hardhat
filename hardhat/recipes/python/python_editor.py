from .base import PipBaseRecipe


class PythonEditorRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PythonEditorRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a3c066acee22a1c94f63938341d4fb37' \
                      '4e3fdd69366ed6603d7b24bed1efc565'
        self.name = 'python-editor'
        self.version = '1.0.3'
