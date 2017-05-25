import os

directory = os.path.dirname(__file__)


def load(settings):
    from hardhat.util import load_recipes
    recipes = load_recipes(directory, 'hardhat.recipes.python')

    dependencies = [
        # only one version of cython is needed so alias it
        ['cython', 'python3-cython'],  # alias
        ['devpi', 'python3-devpi-client',
                  'python3-devpi-server',
                  'python3-devpi-web'],
        ['guess-renames', 'python2-guess-renames'],
        ['hg-git', 'python2-hg-git'],  # alias
        ['meld', 'python2-meld'],
        ['nuitka', 'python2-nuitka'],
        ['tortoisehg', 'python2-tortoisehg'],
    ]

    for recipe in recipes:
        recipe = recipe(settings=settings)
        for python in recipe.pythons:
            name = python + '-' + recipe.name
            if not hasattr(recipe, 'depends'):
                recipe.depends = []

            # Get dependencies and replace 'python-' prefix with current python
            # version for this recipe ('python2-' or 'python3-')
            depends = list(recipe.depends)
            for i in range(len(depends)):
                dep = depends[i]
                if dep.startswith('python-'):
                    depends[i] = python + dep[len('python'):]

            depends.insert(0, name)
            dependencies.append(depends)

    for d in dependencies:
        if needs_python(d, 2):
            d += ['python2']
        elif needs_python(d, 3):
            d += ['python3']

    return (recipes, dependencies)


def needs_python(depends, version):
    needs = False
    has = False
    for d in depends:
        if d.startswith('python%s-' % version):
            needs = True
        elif d == 'python%s' % version:
            has = True
    return needs and not has
