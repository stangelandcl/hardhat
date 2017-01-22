from .base import PipBaseRecipe


class DevPiServerRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DevPiServerRecipe, self).__init__(*args, **kwargs)

        self.pythons = ['python3']
        self.name = 'devpi-server'
        self.version = '3.1.0'
        self.sha256 = None


class DevPiWebRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DevPiWebRecipe, self).__init__(*args, **kwargs)

        self.pythons = ['python3']
        self.depends = ['devpi-server']
        self.name = 'devpi-web'
        self.version = '3.1.0'
        self.sha256 = None


class DevPiClientRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(DevPiClientRecipe, self).__init__(*args, **kwargs)

        self.pythons = ['python3']
        self.depends = ['devpi-client']
        self.name = 'devpi-client'
        self.version = '2.6.2'
        self.sha256 = '0c04a55250c5180bf5f5652ff6e75bc6' \
                      'cc72d9825e0c2ea91217768fc626384a'
