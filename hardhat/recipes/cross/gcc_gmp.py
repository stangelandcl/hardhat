from .gcc_prereq import GccPrereqRecipe


class CrossGccGmpRecipe(GccPrereqRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossGccGmpRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '936162c0312886c21581002b79932829' \
                      'aa048cfaf9937c6265aeaa14f1cd1775'
        self.gcc_directory = None
        self.name = 'cross-gmp'
        self.version = '4.3.2'
