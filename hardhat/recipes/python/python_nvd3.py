from .base import PipBaseRecipe


class PythonNvd3Recipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PythonNvd3Recipe, self).__init__(*args, **kwargs)
        self.sha256 = '86ca51a9526ced2ebe8faff999b06607' \
                      '55f51f2d00af7871efba9b777470ae95'
        self.name = 'python-nvd3'
        self.version = '0.14.2'  # for apache-airflow
        self.pydepends = ['python-slugify']
