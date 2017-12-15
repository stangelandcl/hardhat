from .base import PipBaseRecipe


class FutureRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(FutureRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '3d3b193f20ca62ba7d87825899228788' \
                      '20d0a023b885882deec830adbf639b97'
        self.name = 'future'
        self.version = '0.15.2'  # for apache-airflow
