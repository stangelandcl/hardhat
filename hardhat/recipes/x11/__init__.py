import os
from pprint import pprint
from hardhat.util import load_recipes, add_dependencies
from .apps import APPS

directory = os.path.dirname(__file__)


def load(settings):
    recipes = load_recipes(directory, 'hardhat.recipes.x11')

    dependencies = []

    add_dependencies(settings, dependencies, recipes)

    xorg_libs = ['xorg-libs'] + [x[0] for x in dependencies]

    app_dependencies = []
    add_dependencies(settings, app_dependencies, APPS)

    xorg_apps = ['xorg-apps'] + [x[0] for x in app_dependencies]
    dependencies += app_dependencies

    data_recipes = load_recipes(os.path.join(directory, 'data'),
                                'hardhat.recipes.x11.data')
    data_dependencies = []
    add_dependencies(settings, data_dependencies, data_recipes)

    server_recipes = load_recipes(os.path.join(directory, 'server'),
                                  'hardhat.recipes.x11.server')
    server_dependencies = []
    add_dependencies(settings, server_dependencies, server_recipes)

    driver_recipes = load_recipes(os.path.join(directory, 'driver'),
                                  'hardhat.recipes.x11.driver')
    driver_dependencies = []
    add_dependencies(settings, driver_dependencies, driver_recipes)

    recipes += APPS
    recipes += data_recipes
    recipes += server_recipes
    recipes += driver_recipes
    dependencies.append(xorg_libs)
    dependencies.append(xorg_apps)
    dependencies += data_dependencies
    dependencies += server_dependencies
    dependencies += driver_dependencies

    return (recipes, dependencies)
