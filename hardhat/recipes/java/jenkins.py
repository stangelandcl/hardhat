import os
import shutil
import stat
from .base import JavaBase


class JenkinsRecipe(JavaBase):
    def __init__(self, *args, **kwargs):
        super(JenkinsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'efbb4360de55947189f67895be0960dd' \
                      'fd75104732802948f082f8a5e93228ca'

        self.name = 'jenkins'
        self.depends = ['java']
        self.version = '2.32.1'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'http://mirrors.jenkins.io/war-stable/'
        self.url = 'http://mirrors.jenkins.io/war-stable/$version/jenkins.war'
        self.installed_file = os.path.join(self.java_dir, 'bin', 'jenkins.war')

    def extract(self):
        pass

    def clean(self):
        if os.path.exists(self.installed_file):
            os.remove(self.installed_file)

    def configure(self):
        pass

    def compile(self):
        pass

    def install(self):
        self.log_dir('install', self.directory, 'installing')
        shutil.copy2(self.filename, self.installed_file)

        java = os.path.join(self.java_dir, 'bin', 'java')
        script = r'''#!/bin/sh
%s -jar %s "$@"
''' % (java, self.installed_file)

        dst = os.path.join(self.java_dir, 'bin', 'jenkins')
        with open(dst, 'wt') as f:
            f.write(script)

        os.chmod(dst, stat.S_IRWXU | stat.S_IRWXG | stat.S_IROTH)
