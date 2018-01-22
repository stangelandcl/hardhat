import os
import shutil
from .base import GnuRecipe


class NginxAuthLdapRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NginxAuthLdapRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '80d6cce9a9877d51dec2f85a11ce7cd2' \
                      '5edbd2d605c28bc28687ecc5695229ee'
        self.name = 'nginx-auth-ldap'
        self.version = '42d195d7a7575ebab1c369ad3fc5d78dc2c2669c'
        self.url = self.github_commit('kvspb')

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'copy')

        dir = os.path.dirname(self.directory)
        dir = os.path.join(dir, 'nginx-auth-ldap')
        if os.path.exists(dir):
            shutil.rmtree(dir)
        shutil.copytree(self.directory, dir)

