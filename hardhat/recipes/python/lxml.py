from .base import PipBaseRecipe


class LxmlRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(LxmlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '736f72be15caad8116891eb6aa4a078b' \
                      '590d231fdc63818c40c21624ac71db96'
        self.name = 'lxml'
        self.version = '3.8.0'  # < 4 for apache-airflow
