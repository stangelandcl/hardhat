import os

directory = os.path.dirname(__file__)


def load(settings):
    from hardhat.util import load_recipes
    recipes = load_recipes(directory, 'hardhat.recipes.mingw64')

    dependencies = [
    ]

    for recipe in recipes:
        recipe = recipe(settings=settings)
        depends = list(recipe.depends)
        depends.insert(0, recipe.name)
        if needs_mingw64(depends):
            depends.append('mingw64')

        dependencies.append(depends)
    return (recipes, dependencies)


def needs_mingw64(depends):
    needs = False
    has = False
    for d in depends:
        if d.startswith('mingw64-'):
            needs = True
        elif d == 'mingw64':
            has = True
    return needs and not has
