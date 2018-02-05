from .base import PipBaseRecipe


class DevPiServerRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DevPiServerRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '74de3ec0396d8f6f3b2eafd7c50d6d3a' \
                      'f560a6d80770bd518bee1a312d9be778'
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
        self.sha256 = 'e9afa277a9b227d92335c49fab40be2e' \
                      '9bb112c0f4dda84906c14addb1ded2f7'
        self.pythons = ['python3']
        self.pydepends = ['requests']
        self.name = 'devpi-common'
        self.version = '3.2.1'


class DevPiWebRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DevPiWebRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5ec1d61ccfdc460ff5084188f49308c6' \
                      '801c3471e5417bfd213623c499138fd7'
        self.pythons = ['python3']
        self.pydepends = ['devpi-server', 'pyramid_chameleon',
                          'readme_renderer',
                          'setuptools_scm',
                          'Whoosh']
        self.name = 'devpi-web'
        self.version = '3.2.2'


class DevPiClientRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DevPiClientRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '4e65b4086cd6bcf8bcffd95f40650dff' \
                      '94d24c8fda4b1c5a71c91fdac54e8e56'
        self.pythons = ['python3']
        self.pydepends = ['check-manifest', 'pkginfo', 'requests', 'tox']
        self.name = 'devpi-client'
        self.version = '4.0.1'
