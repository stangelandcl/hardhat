from .gcc_prereq import GccPrereqRecipe


class CrossGccMpcRecipe(GccPrereqRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossGccMpcRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e664603757251fd8a352848276497a4c' \
                      '79b7f8b21fd8aedd5cc0598a38fee3e4'
        self.gcc_directory = None
        self.name = 'cross-mpc'
        self.version = '0.8.1'
        self.extension = 'tar.gz'
