from .base import PipBaseRecipe


class S3TransferRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(S3TransferRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ba1a9104939b7c0331dc4dd234d79afe' \
                      'ed8b66edce77bbeeecd4f56de74a0fc1'

        self.name = 's3transfer'
        self.version = '0.1.10'
