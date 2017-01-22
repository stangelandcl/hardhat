from .base import PipBaseRecipe


class FlaskRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(FlaskRecipe, self).__init__(*args, **kwargs)

        self.name = 'flask'
        self.version = '0.10.1'
        self.pypi_name = 'Flask'
        self.pydepends = ['jinja2', 'itsdangerous', 'werkzeug']
        self.sha256 = '4c83829ff83d408b5e1d499547226541' \
                      '1d2c414112298f2eb4b359d9e4563373'
