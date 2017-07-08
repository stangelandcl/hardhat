from .base import PipBaseRecipe


class AwsCliRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(AwsCliRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6f77d8d7b990f43795c2fac6117ff56d' \
                      '751ef8f8e71116c5cc7f4ab16a3f4154'

        self.pydepends = ['botocore', 'colorama', 'pyyaml', 'rsa', 's3transfer']
        self.name = 'awscli'
        self.version = '1.11.117'
