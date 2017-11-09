import os
from hardhat.util import load_recipes

directory = os.path.dirname(__file__)


def load(settings):
    recipes = load_recipes(directory, 'hardhat.recipes.rpkg')

    dependencies = []

    for recipe in recipes:
        recipe = recipe(settings=settings)
        if not hasattr(recipe, 'depends'):
            recipe.depends = []

        depends = list(recipe.depends)
        depends.insert(0, recipe.name)
        dependencies.append(depends)

    for d in dependencies:
        if d[0] != 'r':
            d += ['r']

    return (recipes, dependencies)
