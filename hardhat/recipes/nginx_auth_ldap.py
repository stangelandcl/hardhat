import os
import shutil
from .base import GnuRecipe


class NginxAuthLdapRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(NginxAuthLdapRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6c469670dfa469f54e46651ebbfa9fd2' \
                      '7c6c953ce4217aa021c7fd876d9121eb'
        self.name = 'nginx-auth-ldap'
        self.version = '0bed9d5b01441876c194eb465e9ac4bf59e3d2fd'
        self.url = self.github_commit('stangelandcl')

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

