from .base import PipBaseRecipe


class VenusianRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(VenusianRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9902e492c71a89a241a18b2f9950bea7' \
                      'e41d025cc8f3af1ea8d8201346f8577d'
        self.name = 'venusian'
        self.version = '1.1.0'
