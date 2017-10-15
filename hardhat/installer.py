import json
import os
from pprint import pprint
import sys
from .environment import export_init_script
from .settings import RecipeSettings
from .terminal import Terminal
from .util import Object


class DependencyFinder(Object):
    def __init__(self, installed, recipes, dependencies, directory=None):
        self.recipes = recipes
        self.dependencies = dependencies
        if directory and not installed:
            installed = InstallFile(directory).load()
        self.installed = set(installed)
        self.included = set()

    def is_installed(self, name):
        return name in self.installed

    def gather(self, name, depth=0):
        if name in self.included:
            return []

        result = []
        depends = []
        for d in self.dependencies:
            if d[0] == name:
                depends = d[1:]
                break
        for d in depends:
            result += self.gather(d, depth+1)
        found = False
        for recipe in self.recipes:
            if name in recipe.provides:
                if name not in self.included:
                    self.included.add(name)
                    result += [(name, name in self.installed)]
                    self.installed.add(name)
                    found = True
                    break
        if not found and depth > 0 and not depends:
            # if it has dependencies, may be using them as an alias for
            # the recipe itself like ['cython', 'python3-cython']
            raise Exception('Could not find required recipe: ' + name)
        return result

    def _gather_edges(self, graph):
        edges = []
        recipes = set()
        for recipe in self.recipes:
            for name in recipe.provides:
                recipes.add(name)

        count = 0
        while graph:
            level = []
            excluded = []
            for k, v in graph.items():
                if not v:
                    if k in recipes:
                        level.append(k)
                    else:
                        excluded.append(k)
            for edge in level:
                del graph[edge]
            for edge in excluded:
                del graph[edge]
            edge_set = set(excluded + level)
            keys = list(graph.keys())
            for k in keys:
                v = graph[k]
                v = list(filter(lambda x: x not in edge_set, v))
                graph[k] = v
            level.sort()
            edges += level
            count += 1
            if count > 100000:
                pprint(graph)
                raise Exception('Circular dependencies')
        return edges

    def _split_installed(self, edges, force_uninstalled):
        installed = []
        uninstalled = []
        force_uninstalled = set(force_uninstalled)
        for edge in edges:
            if edge in self.installed and edge not in force_uninstalled:
                installed.append(edge)
            else:
                uninstalled.append(edge)
        return (installed, uninstalled)

    def _gather_graph1(self, name, graph):
#        print('gather_graph1: ', name)
        for d in self.dependencies:
            if d[0] == name:
                graph[name] = d[1:]
        if name not in graph:
            graph[name] = []
            return

        for d in graph[name]:
            if d not in graph:
                self._gather_graph1(d, graph)

    def gather_graph(self, names, reinstall=False):
        graph = dict()
        for name in names:
            self._gather_graph1(name, graph)
        edges = self._gather_edges(graph)
        if not reinstall:
            names = []
        return self._split_installed(edges, names)


class InstallFile(object):
    def __init__(self, directory):
        self.installed_file = os.path.join(directory, 'installed.json')
        self.installed = self.load()

    def load(self):
        if os.path.exists(self.installed_file):
            with open(self.installed_file, 'rt') as f:
                installed = json.load(f)
                return set(installed)
        return set()

    def save(self):
        tmp = self.installed_file + '.tmp'
        with open(tmp, 'wt') as f:
            files = list(self.installed)
            json.dump(files, f)
        os.rename(tmp, self.installed_file)


class Installer(object):
    def __init__(self, directory, recipes, dependencies,
                 target, install_file, download_dir, settings):
        self.directory = directory
        self.recipes = recipes
        self.dependencies = dependencies
        self.install_file = install_file
        self.settings = settings
        if not settings.mingw64:
            # mingw64 assumes we are running from external hardhat
            init_file = os.path.join(self.directory, 'init.sh')
            export_init_script(init_file, self.directory, target, download_dir)

    def _log_required(self, required, installed):
        text = '\nRequired packages:'
        format = '{0:<25} {1:<22}'
        for recipe in required:
            text += '\n'
            if installed:
                itext = 'installed'
                itext = Terminal.light_white(itext)
            else:
                itext = '[installing]'
                itext = Terminal.normal_green(itext)

            recipe = Terminal.bold_white(recipe)
            text += format.format(recipe, itext)

        print(text)

    def _recipe(self, name):
        for recipe in self.recipes:
            if name in recipe.provides:
                return recipe
        raise Exception('required recipe not found: %s' % (name))

    def _install(self, recipe):
        recipe.clean()
        recipe.run()
        self.install_file.installed.add(recipe.running_name)
        self.install_file.save()

    def depends(self, name):
        depends = DependencyFinder(self.install_file.installed,
                                   self.recipes,
                                   self.dependencies)
        return depends.gather(name)

    def install(self, names):
        depends = DependencyFinder(self.install_file.installed,
                                   self.recipes,
                                   self.dependencies)

        installed, missing = depends.gather_graph(names)
        self._log_required(installed, True)
        self._log_required(missing, False)
        for recipe in self._get_recipes(missing):
            self._install(recipe)

    def _download(self, name):
        recipe = self._recipe(name)
        recipe.running_name = name
        recipe.download()

    def download(self, names):
        depends = DependencyFinder(self.install_file.installed,
                                   self.recipes,
                                   self.dependencies)

        installed, missing = depends.gather_graph(names)
        self._log_required(installed, True)
        self._log_required(missing, False)
        for recipe in missing + installed:
            self._download(recipe)

    def _check_version(self, name):
        recipe = self._recipe(name)
        recipe.running_name = name
        recipe.version_check()

    def check_version(self, names=None, installed=False, missing=False):
        if not names:
            names = []
        depends = DependencyFinder(self.install_file.installed,
                                   self.recipes,
                                   self.dependencies)
        if installed:
            for recipe in self.recipes:
                name = recipe.provides[0]
                if depends.is_installed(name):
                    names.append(name)
        if missing:
            for recipe in self.recipes:
                name = recipe.provides[0]
                if not depends.is_installed(name):
                    names.append(name)
        names.sort()
        for name in names:
            self._check_version(name)

    def _check_sudo(self, recipes):
        recipes = list(filter(lambda x: x.sudo, recipes))
        if recipes and not self.settings.no_sudo:
            names = [x.name for x in recipes]
            names.sort()
            names = ', '.join(names)
            import getpass
            password = getpass.getpass(
                '%s requires sudo password: ' % names)
            try:
                # install python3-python-pam to use this code
                import pam
                p = pam.pam()
                user = os.environ['USER']
                if p.authenticate(user, password):
                    print('Authenticated')
                else:
                    print('Authentication FAILED')
                    sys.exit(1)  # Could not continue until get to sudo
            except: pass
            for recipe in recipes:
                recipe.password = password

    def _get_recipes(self, names):
        recipes = []
        for recipe_name in names:
            recipe = self._recipe(recipe_name)
            recipe.running_name = recipe_name
            recipes.append(recipe)

        self._check_sudo(recipes)
        return recipes


    def reinstall(self, names):
        if isinstance(names, str):
            names = [names]
        if not isinstance(names, list):
            raise Exception('installer.reinstall(). Expected list: %s' % names)
        names = list(filter(lambda x: x != 'toolchain', names))
        depends = DependencyFinder(self.install_file.installed,
                                   self.recipes,
                                   self.dependencies)

        installed, missing = depends.gather_graph(names, reinstall=True)
        self._log_required(installed, True)
        self._log_required(missing, False)

        for recipe in self._get_recipes(missing):
            self._install(recipe)
