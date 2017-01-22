from .base import PipBaseRecipe


class PipRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(PipRecipe, self).__init__(*args, **kwargs)

        self.name = 'pip'
        self.version = '8.1.1'
        self.sha256 = '3e78d3066aaeb633d185a57afdccf700' \
                      'aa2e660436b4af618bcb6ff0fa511798'
