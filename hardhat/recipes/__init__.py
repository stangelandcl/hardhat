import os

directory = os.path.dirname(__file__)

import hardhat.recipes.cross
import hardhat.recipes.doc
import hardhat.recipes.java
import hardhat.recipes.ocaml
import hardhat.recipes.perl
import hardhat.recipes.python
import hardhat.recipes.toolchain
import hardhat.recipes.x11


def load(settings):
    from hardhat.util import load_recipes, add_dependencies
    #  Fedora query to find dependencies: dnf repoquery --requires libtool

    # alias for autotools
    if settings.mingw64:
        autotools = ['autotools', '']
    else:
        autotools = ['autotools', 'autoconf', 'automake', 'libtool']
    dependencies = [
        ['asciidoc', 'python2'],
        ['apache', 'apr-util', 'openssl', 'pcre'],
        ['apr-util', 'apr', 'openssl'],
        ['atk', 'glib', 'gobject-introspection'],
        ['awk', 'gawk'],
        autotools,
        ['fonts', 'cantarell-fonts', 'dejavu-fonts', 'freefont'], # alias for all fonts
        ['fontconfig', 'harfbuzz'],
        ['freetype', 'libpng', 'which'],
        ['gcrypt', 'libgpg-error'],
        ['gdb', 'expat', 'ncurses', 'python3', 'readline', 'xz', 'zlib'],
        ['gdk-pixbuf', 'glib', 'libjpeg-turbo', 'libpng', 'libtiff', 'xorg-libs'],
        ['gmime', 'glib', 'libgpg-error'],
        ['gnutls', 'libidn', 'nettle', 'libtasn1', 'zlib', 'p11-kit', 'gmp'],
        ['gnu-system', 'autotools', 'posix', 'texinfo'],  # alias for autotools + posix
        ['gobject-introspection', 'glib'],
        ['jsoncpp', 'python2'],
        ['libassuan', 'libgpg-error'],
        ['libjpeg-turbo', 'yasm'],
        ['libuuid', 'util-linux'],  # alias for util-linux
        ['man', 'man-pages', 'man-db'],
        ['ncurses', 'pkgconfig', 'libtool'],
        ['p11-kit', 'libtasn1', 'libffi', 'pkgconfig'],
        ['pixman', 'libpng'],
        ['posix', 'bash', 'bc', 'bison', 'coreutils', 'diffutils', 'expect',
                  'findutils', 'flex',
                  'gawk', 'grep', 'gzip', 'file', 'less', 'make',
                  'man',
                  'patch', 'sed',
                  'tar',
                  'texinfo', 'which'],  # alias for posix
        ['readline', 'ncurses'],
        ['scons', 'python2'],
        ['sgml-common', 'autotools'],
        ['sqlite3', 'readline'],
        ['w3m', 'gc', 'ncurses', 'openssl', 'zlib'],
        ['wget', 'cacert', 'gnutls'],
        ['xapian', 'util-linux'],  # util-linux for libuuid
        ['yasm', 'python2', 'cython']
    ]

    recipes = load_recipes(directory, 'hardhat.recipes')
    add_dependencies(settings, dependencies, recipes)

    cross = hardhat.recipes.cross.load(settings)
    doc = hardhat.recipes.doc.load(settings)
    java = hardhat.recipes.java.load(settings)
    mingw64 = hardhat.recipes.mingw64.load(settings)
    ocaml = hardhat.recipes.ocaml.load(settings)
    perl = hardhat.recipes.perl.load(settings)
    python = hardhat.recipes.python.load(settings)
    toolchain = hardhat.recipes.toolchain.load(settings)
    x11 = hardhat.recipes.x11.load(settings)

    dependencies += mingw64[1] + ocaml[1] + perl[1]
    dependencies += python[1] + toolchain[1] + x11[1]

    if not settings.use_root:
        toolchain_depends = []
        for d in toolchain[1]:
            if d[0] == 'toolchain':
                toolchain_depends = set(d)
                break

        if not settings.mingw64:
            # mingw64 assumes mingw64 already installed
            for d in dependencies:
                if d[0] not in toolchain_depends:
                    d += ['toolchain']



    # Java dependencies do not rely on toolchain
    dependencies += java[1]
    dependencies += doc[1]
    dependencies += cross[1]

    recipes += cross[0] + doc[0] + java[0] + mingw64[0] + ocaml[0] + \
               perl[0] + python[0] + toolchain[0] + x11[0]
    return (recipes, dependencies)
