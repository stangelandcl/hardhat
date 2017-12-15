from .base import PipBaseRecipe


class FlaskWtfRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(FlaskWtfRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a938bfabc450b61e2d76f8b32288b65d' \
                      '0cd43ce33c2de496e1b28152c5d141cf'
        self.name = 'flask-wtf'
        self.version = '0.14'  # for apache-airflow
        self.pydepends = ['flask']
