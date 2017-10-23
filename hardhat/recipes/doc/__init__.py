import os
from hardhat.util import load_recipes

directory = os.path.dirname(__file__)


def load(settings):
    recipes = load_recipes(directory, 'hardhat.recipes.doc')

    dependencies = []

    for recipe in recipes:
        recipe = recipe(settings=settings)
        if not hasattr(recipe, 'depends'):
            recipe.depends = []

        depends = list(recipe.depends)
        depends.insert(0, recipe.name)
        dependencies.append(depends)

    return (recipes, dependencies)
