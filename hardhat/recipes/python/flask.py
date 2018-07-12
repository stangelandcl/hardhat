from .base import PipBaseRecipe


class FlaskRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(FlaskRecipe, self).__init__(*args, **kwargs)
        self.name = 'flask'
        self.version = '1.0.2'  # apache-airflow requires < 0.12
        self.pypi_name = 'Flask'
        self.pydepends = ['click', 'jinja2', 'itsdangerous', 'werkzeug']
