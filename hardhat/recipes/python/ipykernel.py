from .base import PipBaseRecipe


class IPyKernelRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(IPyKernelRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '5a54f25f0e6c8ee74c362c23f9a95e10' \
                      'e74c6b7f5ef42059c861ff6f26d89462'

        self.name = 'ipykernel'
        self.version = '4.5.2'
