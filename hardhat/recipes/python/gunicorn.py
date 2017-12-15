from .base import PipBaseRecipe


class GunicornRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(GunicornRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '8bc835082882ad9a012cd790c460011e' \
                      '4d96bf3512d98a04d3dabbe45393a089'
        self.name = 'gunicorn'
        self.version = '19.3.0'  # for apache-airflow
