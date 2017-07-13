from .base import PipBaseRecipe


class RequestsRecipe(PipBaseRecipe):
    def __init__(self, *args, **kwargs):
        super(RequestsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'b3b191d677e526c1e512db86bc7387cc' \
                      'b8356e8826bcc7faa07f78f09afe68dd'

        self.name = 'requests'
        self.version = '2.14.1'
