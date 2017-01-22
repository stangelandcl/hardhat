import os
from string import Template
try:
    from urllib.parse import urlparse, ParseResult
except:
    # python 2
    from urlparse import urlparse, ParseResult


class GithubProject:
    def __init__(self, user, name):
        self.user = user
        self.name = name

    def __str__(self):
        return 'https://github.com/%s/%s' % (self.user, self.name)

    @property
    def releases_url(self):
        return '%s/releases' % self


class GithubUrl:
    def __init__(self, project, name, path, file):
        self.project = GithubProject(project, name)
        self.path = path
        self.file = file

    @staticmethod
    def from_project(project, file, path=None):
        return GithubUrl(project, file, path)

    def url(self):
        if self.path:
            return '%s/%s/%s' % (self.project, self.path, self.file)
        return '%s/%s' % (self.project, self.file)

    def from_version(self, version):
        url = self.url()
        return Template(url).substitute(
            version=version,
            project=self.project.user,
            name=self.project.name)

    def __str__(self):
        if hasattr(self, 'version'):
            return self.from_version(self.version)
        url = self.url()
        return Template(url).substitute(
            project=self.project.user,
            name=self.project.name)


class Urls(object):

    @staticmethod
    def sourceforge(project, *args):
        url = 'http://downloads.sourceforge.net/project/%s/' % (project)
        for arg in args:
            url += arg
        return url

    @staticmethod
    def gnu(project, *args):
        url = 'http://ftpmirror.gnu.org/%s/' % (project)
        for arg in args:
            url += arg
        return url

    @staticmethod
    def pypi(name):
        return 'https://pypi.python.org/pypi/%s/json' % name

    @staticmethod
    def gnu_template(name, version, extension='tar.gz'):
        url = Template('http://ftpmirror.gnu.org/$name/'
                       '$name-$version.$extension')
        url = url.substitute(name=name, version=version, extension=extension)
        return url

    @staticmethod
    def savannah(name, version, extension='tar.gz'):
        url = Template('http://download.savannah.gnu.org/releases/$name/'
                       '$name-$version.$extension')
        return url.substitute(name=name, version=version, extension=extension)


    @staticmethod
    def github_commit(user, name, commit):
        return 'https://github.com/%s/%s/archive/' \
                   '%s.tar.gz' % (user, name, commit)

    @staticmethod
    def drop_file(url):
        p = urlparse(url)
        path = os.path.dirname(p.path)
        p = ParseResult(
            p.scheme, p.netloc, path, p.params, p.query, p.fragment)
        url = p.geturl()
        return url
