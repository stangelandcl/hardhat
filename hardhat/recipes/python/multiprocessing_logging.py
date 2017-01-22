from .base import PipBaseRecipe


class MultiprocessingLoggingRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(MultiprocessingLoggingRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c5cc2c9c03e1d9b7383fb2f07f5f61fd' \
                      '563fee623d2be4649900a4c19eb0cce4'

        self.name = 'multiprocessing-logging'
        self.version = '0.2.4'
