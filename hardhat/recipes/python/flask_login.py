from .base import PipBaseRecipe


class FlaskLoginRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(FlaskLoginRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '83d5f10e5c4f214feed6cc41c212db63' \
                      'a58a15ac32e56df81591bfa0a5cee3e5'
        self.name = 'flask-login'
        self.version = '0.2.11'  # for apache-airflow
        self.pydepends = ['flask']
