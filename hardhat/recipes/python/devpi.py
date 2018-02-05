from .base import PipBaseRecipe


class DevPiServerRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DevPiServerRecipe, self).__init__(*args, **kwargs)
        self.pythons = ['python3']
        self.pydepends = ['argon2_cffi',
                          'defusedxml',
                          'devpi-common', 'execnet', 'itsdangerous',
                          'passlib', 'py', 'pyramid',
                          'waitress']
        self.name = 'devpi-server'
        self.version = '4.4.0'


class DevCommonRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DevCommonRecipe, self).__init__(*args, **kwargs)
        self.pythons = ['python3']
        self.pydepends = ['requests']
        self.name = 'devpi-common'
        self.version = '3.2.1'


class DevPiWebRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DevPiWebRecipe, self).__init__(*args, **kwargs)
        self.pythons = ['python3']
        self.pydepends = ['devpi-server', 'pyramid_chameleon',
                          'readme_renderer',
                          'Whoosh']
        self.name = 'devpi-web'
        self.version = '3.2.2'


class DevPiClientRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DevPiClientRecipe, self).__init__(*args, **kwargs)
        self.pythons = ['python3']
        self.pydepends = ['check-manifest', 'pkginfo', 'tox']
        self.name = 'devpi-client'
        self.version = '4.0.1'
