from .gcc_prereq import GccPrereqRecipe


class GccGmpRecipe(GccPrereqRecipe):
    def __init__(self, *args, **kwargs):
        super(GccGmpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '936162c0312886c21581002b79932829' \
                      'aa048cfaf9937c6265aeaa14f1cd1775'
        self.gcc_directory = None
        self.name = 'gmp'
        self.version = '4.3.2'
