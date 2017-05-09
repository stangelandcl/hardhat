import json
import os
import re
import shutil
from string import Template
from ..base import Downloader, Recipe, Configure, Make, MakeInstall
from ..base import TarballRecipe, GnuRecipe, GetVersionMixin
from hardhat.util import run, read_url, Object
from hardhat.urls import Urls
from hardhat.version import Versions, extension_regex


class PythonBaseRecipe(Object):
    def __init__(self, *args, **kwargs):
        super(PythonBaseRecipe, self).__init__(*args, **kwargs)
        self.pythons = ['python2', 'python3']
        self.depends = []
        self.pydepends = []

    @property
    def python(self):
        if hasattr(self, '_python'):
            return self._python
        return self.running_name.split('-')[0]

    @python.setter
    def python(self, value):
        self._python = value

    @property
    def provides(self):
        names = [x + '-' + self.name for x in self.pythons]
        return names

    @property
    def depends(self):
        return self._depends + ['python-' + x for x in self.pydepends]

    @depends.setter
    def depends(self, value):
        self._depends = value

    @property
    def pypi_name(self):
        if hasattr(self, '_pypi_name'):
            return self._pypi_name
        return self.name

    @pypi_name.setter
    def pypi_name(self, value):
        self._pypi_name = value

    @property
    def url(self):
        if not hasattr(self, '_url'):
            return self.find_url()
        return Template(self._url).substitute(
            name=self.name,
            version=self.version)

    @url.setter
    def url(self, value):
        self._url = value

    def find_url(self):
        url = Urls.pypi(self.pypi_name)
        text = read_url(url).decode('utf-8')
        pkg = json.loads(text)
        pkgs = pkg['releases'][self.version]
        pkg = pkgs[0]
        for p in pkgs:
            if p['packagetype'] == 'sdist':
                pkg = p
                break
        # md5 = pkg['md5_digest']
        # filename = pkg['filename']
        url = pkg['url']
        return url


class PythonGnuRecipe(PythonBaseRecipe, GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PythonGnuRecipe, self).__init__(*args, **kwargs)


class SetupPyRecipe(PythonBaseRecipe, Configure, Make, MakeInstall,
                    TarballRecipe):
    def __init__(self, *args, **kwargs):
        super(SetupPyRecipe, self).__init__(*args, **kwargs)

    def configure(self):
        pass

    def compile(self):
        self.compile_args = [self.python,
                             'setup.py',
                             'build']
        super(SetupPyRecipe, self).compile()

    def install(self):
        self.install_args = [self.python,
                             'setup.py',
                             'install',
                             '--force']
        super(SetupPyRecipe, self).install()


class PipBaseRecipe(PythonBaseRecipe, Downloader, GetVersionMixin, Recipe):
    def __init__(self, *args, **kwargs):
        super(PipBaseRecipe, self).__init__(*args, **kwargs)
        # ignore betas and release candidates using $
        self.version_regex = '(?P<version>\d+\.\d+(\.\d+)?)$'

    def _clean_build_dir(self):
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)

    def clean(self):
        # Never delete ourselves
        if self.name == 'pip':
            return

        self._clean_build_dir()

        args = self.shell_args + [
            '-c',
            '"%s -m pip list"' % (self.python)
            ]

        self.log_dir('clean', self.prefix_dir, ' '.join(args))
        output = run(args, self.prefix_dir, self.environment)
        lines = output.split('\n')
        package_is_installed = False
        for line in lines:
            if line.startswith('%s ' % (self.running_name)):
                package_is_installed = True
                break

        if package_is_installed:
            args = self.shell_args + [
                '-c',
                '"%s -m pip uninstall --yes %s==%s"' %
                (self.python, self.pypi_name, self.version)
                ]

            self.log_dir('clean', self.prefix_dir, ' '.join(args))
            self.run_exe(args, self.prefix_dir, self.environment)

    def install(self):
        # Cleaning build directory is required.
        # Pip will not try to reinstall otherwise
        self._clean_build_dir()

        args = self.shell_args + [
            '-c',
            '"%s -m pip install -v --no-index'
            ' --no-clean'
            ' --build %s'
            ' --find-links %s'
            ' --ignore-installed %s==%s"' %
            (self.python,
             self.directory,
             self.tarball_dir,
             self.pypi_name,
             self.version)
            ]
        if hasattr(self, 'extra_install_args'):
            args += self.extra_install_args

        self.log_dir('install', self.prefix_dir, ' '.join(args))
        self.run_exe(args, self.prefix_dir, self.environment)

    @property
    def version_regex(self):
        if hasattr(self, '_version_regex'):
            return self._version_regex

    @version_regex.setter
    def version_regex(self, value):
        self._version_regex = value

    def get_version(self):
        if self.url == self.find_url():
            url = Urls.pypi(self.pypi_name)
            text = read_url(url).decode('utf-8')
            pkg = json.loads(text)
            versions = pkg['releases'].keys()
            if self.version_regex:
                versions = [re.match(self.version_regex, n) for n in versions]
                versions = list(filter(lambda x: x, versions))
                versions = [x.group('version') for x in versions]
            return (Versions.max(versions), len(set(versions)) > 1)


# Unused - trial code
def pip_recipe(recipe_name, pip_name, pip_version, python_versions):
    base_class = Template("""
class ${name}Recipe(PipRecipe):
    def __init__(self, *args):
        super(${name}Recipe, self).__init__(*args)

        self.name = '$pip_name'
        self.version = '$pip_version'
""").substitute(name=recipe_name,
                pip_name=pip_name,
                pip_version=pip_version)

    python_template = Template("""
class Python${version}${name}Recipe(${name}Recipe):
    def __init__(self, *args):
        super(Python${version}${name}Recipe, self).__init__(*args)
        self.python = 'python${version}'

""")

    text = base_class + '\n'
    for version in python_versions:
        text += python_template.substitute(name=recipe_name,
                                           version=version)
        text += '\n'

    print('executing %s' % (text))
    d = dict()
    exec(text, globals())
