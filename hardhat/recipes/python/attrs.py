from .base import SetupPyRecipe


class AttrsRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(AttrsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e0d0eb91441a3b53dab4d9b743eafc1a' \
                      'c44476296a2053b6ca3af0b139faf87b'
        self.pythons = ['python3']
        self.name = 'attrs'
        self.version = '18.1.0'
        self.url = 'https://files.pythonhosted.org/packages/e4/ac/a04671e118b57bee87dabca1e0f2d3bda816b7a551036012d0ca24190e71/attrs-18.1.0.tar.gz'
