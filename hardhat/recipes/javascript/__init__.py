import os

directory = os.path.dirname(__file__)


def load(settings):
    from hardhat.util import load_recipes
    recipes = load_recipes(directory, 'hardhat.recipes.javascript')

    dependencies = [
    ]

    for recipe in recipes:
        recipe = recipe(settings=settings)
        depends = list(recipe.depends)
        depends.insert(0, recipe.name)
        if needs_nodejs(depends):
            depends.append('nodejs')

        dependencies.append(depends)
    return (recipes, dependencies)


def needs_nodejs(depends):
    needs = False
    has = False
    for d in depends:
        if d.startswith('nodejs-'):
            needs = True
        elif d == '':
            has = True
    return needs and not has
