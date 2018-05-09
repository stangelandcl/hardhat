from .base import PipBaseRecipe


class AttrsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AttrsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e0d0eb91441a3b53dab4d9b743eafc1a' \
                      'c44476296a2053b6ca3af0b139faf87b'
        self.pythons = ['python3']
        self.name = 'attrs'
        self.version = '18.1.0'
