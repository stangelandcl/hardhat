from .gcc_prereq import GccPrereqRecipe


class GccIslRecipe(GccPrereqRecipe):
    def __init__(self, *args, **kwargs):
        super(GccIslRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '7e3c02ff52f8540f6a85534f54158968' \
                      '417fd676001651c8289c705bd0228f36'
        self.gcc_directory = None
        self.name = 'isl'
        self.version = '0.14'
