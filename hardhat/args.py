import argparse
import multiprocessing
import os
from .settings import RecipeSettings


def parse_args():
    default_prefix_dir = os.environ.get('HARDHAT_PREFIX',
                                        os.path.expanduser('~/hardhat'))
    default_download_dir = os.environ.get(
        'HARDHAT_DOWNLOAD_DIR',
        os.path.expanduser('~/Downloads/hardhat'))

    parser = argparse.ArgumentParser(
        description='install packages from source as non-root user')
    parser.add_argument('--cpus',
                        help='cpu count to use during compiling. Can be' +
                             ' negative meaning use all cpus minus the count' +
                             ' given. If cpus is a decimal number then it is' +
                             ' multiplied by the cpu count. So .5 means use' +
                             ' half of the available cpus.',
                        type=float,
                        default=_default_cpu_count())
    parser.add_argument('--march',
                        help='architecture=core2|native',
                        type=str)
    parser.add_argument('--prefix',
                        default=default_prefix_dir,
                        help='the root-like directory packages ' +
                             'will be installed in')
    parser.add_argument('--downloads',
                        default=default_download_dir,
                        help='the directory to download packages to. '
                             'Cached for offline installs')
    parser.add_argument('-v', '--verbose',
                        help='verbose logging',
                        action='store_true')
    parser.add_argument('--silent',
                        help='no logging',
                        action='store_true')
    parser.add_argument('--just',
                        help="don't install dependencies",
                        action='store_true')
    parser.add_argument('--version',
                        help='print version',
                        version='0.1',
                        action='version')

    sub_parsers = parser.add_subparsers(dest='cmd', help='sub parser help')

    depends_parser = sub_parsers.add_parser(
        'depends',
        help='show packages this package depends on')

    depends_parser.add_argument('package',
                                help='package to get dependencies for',
                                nargs='+')

    depends_on_parser = sub_parsers.add_parser(
        'depends-on',
        help='show packages that depend on this package')

    depends_on_parser.add_argument('package',
                                   help='package name',
                                   nargs='+')

    download_parser = sub_parsers.add_parser('download',
                                             help='download package and dependencies only')
    download_parser.add_argument('package',
                                 help='package(s) (and dependencies) to download',
                                 nargs='+')

    env_parser = sub_parsers.add_parser(
        'env', help='show environment used when compiling')


    info_parser = sub_parsers.add_parser('info',
                                         help='package info')
    info_parser.add_argument('package',
                             help='packages to list info about',
                             nargs='+')


    install_parser = sub_parsers.add_parser(
        'install', help='install a package or packages')
    install_parser.add_argument('package',
                                help='package to install',
                                nargs='*')
    install_parser.add_argument('--file',
                                help='install packages in config file',
                                type=str)
    install_parser.add_argument('--no-clean',
                                help="leave build directory after install",
                                action='store_true')


    list_parser = sub_parsers.add_parser('list',
                                         help='list packages')

    list_parser.add_argument('--missing',
                             help='show only missing packages',
                             action='store_true')
    list_parser.add_argument('--installed',
                             help='show only installed packages',
                             action='store_true')

    log_parser = sub_parsers.add_parser('log',
                                        help='print install.log file to screen')
    log_sub_parsers = log_parser.add_subparsers(dest='log',
                                                help='log subparsers')
    log_ui_parser = log_sub_parsers.add_parser('ui',
                                               help='Show in $EDITOR')

    proxy_parser = sub_parsers.add_parser('proxy',
                                          help='test caching proxy server')

    reinstall_parser = sub_parsers.add_parser(
        'reinstall', help='(re)install a package or packages')
    reinstall_parser.add_argument('package',
                                  help='package to (re)install',
                                  nargs='+')
    reinstall_parser.add_argument('--no-clean',
                                  help="leave build directory after install",
                                  action='store_true')

    version_parser = sub_parsers.add_parser(
        'version',
        help='check for new version of package or packages')
    version_parser.add_argument('package',
                                help='package(s) to check versions',
                                nargs='*')
    version_parser.add_argument('--all',
                                help='version check all packages',
                                action='store_true')
    version_parser.add_argument('--installed',
                                help='show only installed packages',
                                action='store_true')
    version_parser.add_argument('--missing',
                                help='show only missing packages',
                                action='store_true')


    args = parser.parse_args()
    if not hasattr(args, 'no_clean'):
        args.no_clean = False
    args.prefix = os.path.expanduser(args.prefix)
    args.prefix = os.path.expandvars(args.prefix)
    args.downloads = os.path.expanduser(args.downloads)
    args.downloads = os.path.expandvars(args.downloads)

    settings = RecipeSettings()
    settings.settings_filename = os.path.join(args.prefix, 'config.ini')
    settings.prefix_dir = args.prefix
    settings.tarball_dir = args.downloads
    settings.silent = args.silent
    settings.quiet = not args.verbose
    settings.cpu_count = _cpu_count(args.cpus)
    settings.post_clean = not args.no_clean
    settings.enable_version_check = args.cmd == 'version'
    if args.march:
        settings.march = args.march
        os.environ['HARDHAT_MARCH'] = args.march

    # TODO: only run this if creating tmp_dir
    tmp = os.path.join(args.prefix, 'tmp')
    if not os.path.exists(tmp):
        os.makedirs(tmp)

    if not os.path.exists(settings.tarball_dir):
        os.makedirs(settings.tarball_dir)

    docdir = os.path.join(args.prefix, 'doc')
    if not os.path.exists(docdir):
        os.makedirs(docdir)

    return (args, settings)


def _default_cpu_count():
    c = multiprocessing.cpu_count()
    if c == 1:
        return c
    if c == 2:
        return 1
    if c <= 4:
        return c - 1
    if c <= 8:
        return c // 2
    return c // 2


def _cpu_count(in_cpus):
    cpus = in_cpus
    if cpus < 0:
        cpus = max(multiprocessing.cpu_count() + cpus, 1)
    elif (cpus - int(cpus)) != 0:
        cpus *= multiprocessing.cpu_count()
        cpus = max(min(multiprocessing.cpu_count(), cpus), 1)
    cpus = int(cpus)
#    print('in_cpus=%s out=%s' % (in_cpus, cpus))
    return cpus
