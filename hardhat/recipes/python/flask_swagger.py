from .base import PipBaseRecipe


class FlaskSwaggerRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(FlaskSwaggerRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '42420efbed1aad86f7ca6bb869df550e' \
                      '09591e1d540ebd3040c197906c0f0be6'
        self.name = 'flask-swagger'
        self.version = '0.2.13'  # for apache-airflow
        self.pydepends = ['flask']
