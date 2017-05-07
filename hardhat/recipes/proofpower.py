from .base import GnuRecipe


class ProofPowerRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ProofPowerRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fc94ff23e670a2e9f5371ce4f0b3bb36' \
                      '6fa4b12f195bd9609fcae6899a608e80'

        self.name = 'proofpower'
        self.version = '3.1w7'
        self.depends = ['motif', 'polyml', 'texlive']
        self.version_regex = r'(?P<version>\d+\.\d+\w+\d+)'
        self.url = 'http://www.lemma-one.com/ProofPower/getting/versions/' \
                   'OpenProofPower-$version.tgz'

        self.environment['PPDOCFORMAT'] = 'PDF'
        self.environment['PPHOME'] = '%s/proofpower' % self.prefix_dir
        self.environment['PPPOLYHOME'] = self.prefix_dir

        self.install_args = self.shell_args + ['./install']

    def compile(self):
        pass
