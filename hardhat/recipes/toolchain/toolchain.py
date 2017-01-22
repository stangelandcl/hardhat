from hardhat.recipes.base import EmptyRecipe
import hardhat.recipes


class ToolchainRecipe(EmptyRecipe):
    def __init__(self, *args, **kwargs):
        super(ToolchainRecipe, self).__init__(*args, **kwargs)
        self.name = 'toolchain'

    def clean(self):
        pass

    def download(self):
        pass
