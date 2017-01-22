from .base import PipBaseRecipe


class NotebookRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(NotebookRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '922b911f3cd1b20cf37d5ac365521586' \
                      '678fca4b8d20476fc369907b4a0ae1af'

        self.name = 'notebook'
        self.version = '4.3.1'
        self.pydepends = ['ipykernel',
                          'ipython',
                          'jinja2',
                          'jupyter_client',
                          'jupyter_core',
                          'nbconvert',
                          'nbformat',
                          'terminado',
                          'tornado']
