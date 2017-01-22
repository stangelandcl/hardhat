from .base import SetupPyRecipe


class DjangoPython3LdapRecipe(SetupPyRecipe):
    def __init__(self, *args, **kwargs):
        super(DjangoPython3LdapRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'f7ec491f93f37062316f69bb5d71bfdd' \
                      'a705475d0f5564fbcad8dabb2b1de603'

        self.pythons = ['python3']
        self.name = 'django-ldap'
        self.version = '09971943bfe76577dd12889200a91bed1510b0d2'
        self.url = 'https://github.com/etianen/django-python3-ldap/archive/' \
                   '$version.tar.gz'
