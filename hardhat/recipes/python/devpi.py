from .base import PipBaseRecipe


class DevPiServerRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DevPiServerRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'a756a4485eca488aa06d3bc4f33a1d51' \
                      '4137bd8e2a313f8ee2f2f5d2e17070ee'

        self.pythons = ['python3']
        self.pydepends = ['argon2_cffi',
                          'defusedxml',
                          'devpi-common', 'execnet', 'itsdangerous',
                          'passlib', 'py', 'pyramid',
                          'waitress']
        self.name = 'devpi-server'
        self.version = '4.3.0'


class DevCommonRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DevCommonRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'd89634a57981ed43cb5dcd25e00c9454' \
                      'ea111189c5ddc08d945b3d5187ada5fd'

        self.pythons = ['python3']
        self.name = 'devpi-common'
        self.version = '3.1.0'


class DevPiWebRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DevPiWebRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ca074d35d2f8079b718938773ac571e2' \
                      '8123358f4d565d2c925e62d5a0d620f0'

        self.pythons = ['python3']
        self.pydepends = ['devpi-server', 'pyramid_chameleon',
                          'readme_renderer',
                          'Whoosh']
        self.name = 'devpi-web'
        self.version = '3.2.0'


class DevPiClientRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DevPiClientRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '27510e70cbd20a61e51383fe4454089a' \
                      '6dff1685ded2ad0ebc7695d9544cc151'
        self.pythons = ['python3']
        self.pydepends = ['check-manifest', 'pkginfo', 'tox']
        self.name = 'devpi-client'
        self.version = '3.0.0'
