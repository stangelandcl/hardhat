from .base import PipBaseRecipe


class FuncSigsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(FuncSigsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '2310f9d4a77c284e920ec572dc252536' \
                      '6a107b08d216ff8dbb891d95b6a77563'
        self.name = 'funcsigs'
        self.version = '1.0.0'  # for apache-airflow
        self.pydepends = ['ordereddict']
