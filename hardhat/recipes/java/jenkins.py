import os
from .base import JarBase


class JenkinsRecipe(JarBase):
    def __init__(self, *args, **kwargs):
        super(JenkinsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '014f669f32bc6e925e926e260503670b' \
                      '32662f006799b133a031a70a794c8a14'
        self.name = 'jenkins'
        self.version = '2.89.2'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'http://mirrors.jenkins.io/war-stable/'
        self.url = 'http://mirrors.jenkins.io/war-stable/$version/jenkins.war'
        self.installed_file = os.path.join(self.java_dir, 'bin', 'jenkins.war')
