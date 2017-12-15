from .base import PipBaseRecipe


class FlaskRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(FlaskRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b4713f2bfb9ebc2966b8a49903ae0d39' \
                      '84781d5c878591cf2f7b484d28756b0e'
        self.name = 'flask'
        self.version = '0.11.1'  # apache-airflow requires < 0.12
        self.pypi_name = 'Flask'
        self.pydepends = ['click', 'jinja2', 'itsdangerous', 'werkzeug']
