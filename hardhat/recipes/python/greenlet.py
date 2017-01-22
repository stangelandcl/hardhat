from .base import PipBaseRecipe


class GreenletRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(GreenletRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '79f9b8bbbb1c599c66aed5e643e8b53b' \
                      'ae697cae46e0acfc4ee461df48a90012'

        self.name = 'greenlet'
        self.version = '0.4.9'
