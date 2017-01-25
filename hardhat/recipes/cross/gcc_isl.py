from .gcc_prereq import GccPrereqRecipe


class CrossGccIslRecipe(GccPrereqRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossGccIslRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7e3c02ff52f8540f6a85534f54158968' \
                      '417fd676001651c8289c705bd0228f36'
        self.gcc_directory = None
        self.name = 'cross-isl'
        self.version = '0.14'