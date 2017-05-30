import multiprocessing
import os
from string import Template
import subprocess
import sys
import time


from hardhat.args import parse_args
from hardhat.environment import runtime_env
from hardhat.installer import Installer, InstallFile, DependencyFinder
import hardhat.recipes
from hardhat.terminal import Terminal
from hardhat.proxy import Proxy
from hardhat.util import is_file_open
from hardhat.config import read_file_list


try:
    from urllib.request import ProxyHandler, build_opener
    from urllib.request import install_opener
except ImportError:
    from urllib2 import ProxyHandler, build_opener, install_opener


def prefetch(recipes):
    for recipe in recipes:
        recipe.download()


def print_settings(title, key_value_pairs):
    print('%s:\n' % (title))
    KEY_WIDTH = 18

    key_value_pairs.sort(key=lambda x: x[0])
    for k, v in key_value_pairs:
        k = str(k)
        v = str(v)
        count = KEY_WIDTH - len(k)
        k = Terminal.bold_white(k)
        equals = Terminal.light_white('=')
        text = '%s' % (k)
        while count > 0:
            text += Terminal.light_white('.')
            count -= 1
        text += v
        print(text)


def format_installed(name, installed, name_spaces=28):
    spaces = max(name_spaces - len(name), 1)
    if installed:
        itext = Terminal.normal_green('installed')
    else:
        itext = Terminal.bold_red('missing')
    text = name
    while spaces:
        spaces -= 1
        text += ' '  # Terminal.light_white(space_text)
    text += itext

    return text


def print_package_info(package, recipes, installer):
    package_template = Template("""
Package: $name $version $installed
$description
$dependencies
""")

    for recipe in recipes:
        if package == recipe.name:
            installed = recipe.name in installer.installed
            if installed:
                itext = Terminal.normal_green('installed')
            else:
                itext = Terminal.bold_red('missing')
            description = ''
            dependencies = installer.depends(recipe.name)
            depends = ''
            start = False
            for name, installed in dependencies:
                if start or name == 'toolchain':
                    start = True
                else:
                    continue
                if name != recipe.name:
                    depends += format_installed(name, installed) + '\n'
            name = Terminal.bold_white(recipe.name)
            text = package_template.substitute(name=name,
                                               version=recipe.version,
                                               installed=itext,
                                               description=description,
                                               dependencies=depends)
            print(text)
            break


def main():
    args, settings = parse_args()

    log_file = os.path.join(settings.prefix_dir, 'install.log')
    if args.cmd != 'log' and os.path.exists(log_file):
        open(log_file, 'w').close()  # truncate

    log_file_is_open = is_file_open(log_file)
    settings.install_file = InstallFile(settings.prefix_dir)

    RECIPES, dependencies = hardhat.recipes.load(settings)
    recipes = [x(settings=settings) for x in RECIPES]

    installer = Installer(settings.prefix_dir,
                          recipes,
                          dependencies,
                          settings.target_triplet,
                          settings.install_file,
                          settings.tarball_dir,
                          settings)

    settings.installer = installer
    for recipe in recipes:
        recipe.installer = installer

    settings_dict = {'Prefix Directory': settings.prefix_dir,
                     'Target': settings.target_triplet,
                     'CPU Count': '%s of %s' % (settings.cpu_count,
                                                multiprocessing.cpu_count()),
                     'March':settings.march
                    }
    print('')
    print_settings('Settings', list(settings_dict.items()))



#    prefetch(RECIPES)

    if args.cmd == 'env':
        env = runtime_env(settings.prefix_dir,
                          settings.target_triplet,
                          settings.tarball_dir)
        print('\n')
        print_settings('Environment', list(env.items()))
    elif args.cmd == 'info':
        for package in args.package:
            print_package_info(package, recipes, installer)
    elif args.cmd == 'install':
        if not args.package:
            if not args.file:
                print('\nError: hardhat install - either packages or a '
                      'filename must be provided to install')
                return -1
            args.package = read_file_list(args.file)
        args.package.sort()
        installer.install(args.package)
    elif args.cmd == 'list':
        print('\n')
        print(Terminal.bold_white('Packages'))
        for recipe in dependencies:
            name = Terminal.normal_white(recipe[0])
            installed = recipe[0] in installer.install_file.installed
            if args.missing == args.installed:
                show = True
            elif args.missing:
                show = not installed
            elif args.installed:
                show = installed
            if show:
                text = format_installed(name, installed)
#            print(repr(format.format(name, itext)))
                print(text)
    elif args.cmd == 'reinstall':
        installer.reinstall(args.package)
    elif args.cmd == 'depends':
        finder = DependencyFinder(None, RECIPES, dependencies,
                                  settings.prefix_dir)
        depends = []
        for package in args.package:
            depends += finder.gather(package)
        if len(args.package) > 1:
            print(set(depends))
        print(depends)
    elif args.cmd == 'proxy':
        with Proxy('/home/stangecl/Downloads/tmp') as proxy:
            print('proxy listening on %s' % (proxy.port))
            while 1:
                time.sleep(.1)
    elif args.cmd == 'log':
        if args.log == 'ui':
            editor = os.environ.get('EDITOR', 'vi')
            subprocess.call([editor, log_file])
        elif log_file_is_open:
            subprocess.call(['tail', '-f', log_file])
        else:
            with open(log_file, 'rb') as f:
                print(f.read().decode('utf-8'))
    elif args.cmd == 'download':
        args.package.sort()
        if len(args.package) == 1 and os.path.exists(args.package[0]):
            args.package = read_packages(args.package[0])
        installer.download(args.package)
    elif args.cmd == 'version':
        if args.installed:
            installer.check_version(installed=True)
        elif args.missing:
            installer.check_version(missing=True)
        elif args.all:
            installer.check_version(installed=True, missing=True)
        else:
            args.package.sort()
            if len(args.package) == 1 and os.path.exists(args.package[0]):
                args.package = read_packages(args.package[0])
            installer.check_version(args.package)

if __name__ == '__main__':
    try:
        rc = main()
        if rc:
            sys.exit(rc)
    except Exception as e:
        print('Main error: %s' % e)
