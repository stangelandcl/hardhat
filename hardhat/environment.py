import os
from string import Template
from .dotdict import dotdict


LIBRARY_PATH = '/usr/lib64'
ROOT_PATH = '/usr/local/bin:/usr/local/sbin:/usr/bin:/usr/sbin:/bin:/sbin'


ENVIRONMENT = Template('''
export HARDHAT_PREFIX=$HARDHAT_PREFIX
export HARDHAT_PATH="$HARDHAT_PATH"
export HARDHAT_DOWNLOAD_DIR="$HARDHAT_DOWNLOAD_DIR"
export HARDHAT_TARGET=$HARDHAT_TARGET
export HARDHAT_MARCH=$HARDHAT_MARCH
export PREFIX=$PREFIX
export XORG_PREFIX=$XORG_PREFIX
export XML_CATALOG_FILES=$XML_CATALOG_FILES

export GOROOT=$HARDHAT_PREFIX/go
export LC_ALL=C
export ROOT_PATH="$ROOT_PATH"
export PATH="$$HARDHAT_PATH:$$ROOT_PATH"
export CC=$CC
export CPP=$CPP
export CXX=$CXX
export AR=$AR
export AS=$AS
export LD=$LD
export FC=$FC
export F77=$F77
export F90=$F90
export F95=$F95
export LIBRARY_PATH=$LIBRARY_PATH
export OPT="$OPT"

export CFLAGS_NO_OPT="$CFLAGS_NO_OPT"
export CXXFLAGS_NO_OPT="$CXXFLAGS_NO_OPT"
export FFLAGS_NO_OPT="$FFLAGS_NO_OPT"

export CFLAGS="$$CFLAGS_NO_OPT $$OPT"
export CXXFLAGS="$$CXXFLAGS_NO_OPT $$OPT"
export FFLAGS="$$FFLAGS_NO_OPT $$OPT"
export CPPFLAGS="$CPPFLAGS"

export LD_OPT="$LD_OPT"
export LDFLAGS_NO_OPT="$LDFLAGS_NO_OPT"
export LDFLAGS="$$LDFLAGS_NO_OPT $$LD_OPT"

export TMPDIR=$TMPDIR
export JAVA_HOME=$JAVA_HOME
export LIBS="$LIBS"
export CCACHE_DIR=$HARDHAT_PREFIX/$USER/.ccache
export PREFIX=$PREFIX


#export TERM=xterm-256color

mkdir -p "$$CCACHE_DIR"


cflags_no_opt()
{
    export CFLAGS="$$CFLAGS_NO_OPT"
    export FFLAGS="$$FFLAGS_NO_OPT"
}

cflags_opt()
{
    export CFLAGS="$$CFLAGS_NO_OPT $$OPT"
    export CXXFLAGS="$$CXXFLAGS_NO_OPT $$OPT"
    export FFLAGS="$$FFLAGS_NO_OPT $$OPT"
}

ldflags_no_opt()
{
    export LDFLAGS="$$LDFLAGS_NO_OPT"
}

ldflags_opt()
{
    export LDFLAGS="$$LDFLAGS_NO_OPT $$LD_OPT"
}

path_no_root()
{
    export PATH="$$HARDHAT_PATH"
}

path_with_root()
{
    export PATH="$$HARDHAT_PATH:$$ROOT_PATH"
}

''')


def runtime_env(prefix, target, download_dir):
    shell = '/bin/bash'
    bin_shell = os.path.join(prefix, 'bin', 'bash')
    if os.path.exists(bin_shell):
        shell = bin_shell

    path = '$prefix/bin:$prefix/usr/bin:$prefix/sbin:$prefix/gnu/bin' \
           ':$prefix/$target/bin:$prefix/java/bin:$prefix/go/bin'
    path = Template(path).substitute(prefix=prefix, target=target)

    lib_path = '$prefix/lib:$prefix/$target/lib64:$prefix/$target/lib' \
               ':$prefix/lib64'
    lib_path = Template(lib_path).substitute(prefix=prefix, target=target)

    ldflags = '-L$prefix/lib -L$prefix/lib64 -L$prefix/$target/lib' \
              ' -L$prefix/$target/lib64'
    ldflags = Template(ldflags).substitute(prefix=prefix, target=target)

    ld_opt = '-O3 -flto -fuse-linker-plugin'
    ld_opt_flags = ldflags + ' ' + ld_opt

    arch = os.environ['HARDHAT_MARCH']
    opt = '-O3 -mtune=native -march=%s' \
          ' -flto -ffat-lto-objects -fomit-frame-pointer' \
          ' -momit-leaf-frame-pointer ' % arch
    # -ffast-math breaks sqlite so needs disabled for sqlite3 and bdb at least
# -falign-functions=1 -falign-jumps=1 -falign-loops=1

    cflags = '-Wno-error=format-nonliteral -Wno-error=implicit-fallthrough='

    c_opt_flags = cflags
    if c_opt_flags:
        c_opt_flags += ' '
    c_opt_flags += opt

#    cflags = '-I$prefix/include -I$prefix/$target/include'
#    cflags = Template(cflags).substitute(prefix=prefix, target=target)

    def target_exe(exe):
        return '%s/bin/%s-%s' % (prefix, target, exe)

    env = dotdict({
        'HARDHAT_PREFIX': prefix,
        'HARDHAT_DOWNLOAD_DIR': download_dir,
        'HARDHAT_MARCH': os.environ['HARDHAT_MARCH'],
        'PREFIX': prefix,
        'XORG_PREFIX': prefix,
        'HOME': os.environ.get('HOME', os.path.expanduser('~')),
        'HARDHAT_PATH': path,
        'ROOT_PATH': ROOT_PATH,
        'PATH': '%s:%s' % (path, ROOT_PATH),
        'XML_CATALOG_FILES': os.path.join(prefix, 'etc', 'xml', 'catalog'),
        'CPP': target_exe('cpp'),
        'CC': target_exe('gcc'),
        'CXX': target_exe('g++'),
        'AR': target_exe('ar'),
        'AS': target_exe('as'),
        'LD': target_exe('ld'),
        'FC': target_exe('gfortran'),
        'F77': target_exe('gfortran'),
        'F90': target_exe('gfortran'),
        'F95': target_exe('gfortran'),
        'TMPDIR': '%s/tmp' % (prefix),
        'LIBRARY_PATH': lib_path,
        'JAVA_HOME': '%s/java' % (prefix),
        'CCACHE_DIR': '%s/%s/.ccache' % (prefix, os.environ['USER']),
        'R_SHELL': '%s/bin/bash' % (prefix),
        'LDFLAGS_NO_OPT': ldflags,
        'LDFLAGS': ld_opt_flags,
        'LD_OPT': ld_opt,
        'OPT': opt,
        'CFLAGS_NO_OPT': cflags,
        'CXXFLAGS_NO_OPT': cflags,
        'FFLAGS_NO_OPT': cflags,
        'CFLAGS': c_opt_flags,
        'CPPFLAGS': '-DNDEBUG',
        'CXXFLAGS': c_opt_flags,
        'FFLAGS': c_opt_flags,
        'LIBS': '-lrt',
        'LFLAGS': '',
#        'CCACHE_DISABLE': '1',
        'SH': shell,
        'SHELL': shell,
        'CONFIG_SHELL': shell  # for R
        })

    for k, v in proxy_env().items():
        if k not in env:
            env[k] = v

    return env


def export_init_script(filename, prefix, target, download_dir):
    with open(filename, 'wt') as f:
        env = runtime_env(prefix, target, download_dir)
        env['PREFIX'] = prefix
        env['HARDHAT_TARGET'] = target
        text = ENVIRONMENT.substitute(env)
        f.write(text)


def toolchain_bin_dir(prefix):
    return os.path.join(prefix, 'bin')


def toolchain_sbin_dir(prefix):
    return os.path.join(prefix, 'sbin')


def toolchain_tmp_dir(prefix):
    return os.path.join(prefix, 'tmp')


def toolchain_lib_path(prefix, target):
    lib = os.path.join(prefix, 'lib')
    lib64 = os.path.join(prefix, 'lib64')
    gcc_lib = os.path.join(prefix, target, 'lib')
    gcc_lib64 = os.path.join(prefix, target, 'lib64')

    return '%s:%s:%s:%s' % (lib, lib64, gcc_lib, gcc_lib64)


OLD_LIB_ENV = {
    'LIBRARY_PATH': LIBRARY_PATH
}

CLEAN_PATH_ENV = {
    'PATH': ROOT_PATH,
    'LIBRARY_PATH': LIBRARY_PATH,
    'CCACHE_DISABLE': '1'
}


def proxy_env():
    http_proxy = os.environ.get('http_proxy')
    HTTP_PROXY = os.environ.get('HTTP_PROXY')
    https_proxy = os.environ.get('https_proxy')
    HTTPS_PROXY = os.environ.get('HTTPS_PROXY')
    ftp_proxy = os.environ.get('ftp_proxy')
    FTP_PROXY = os.environ.get('FTP_PROXY')

    proxy = dotdict()
    if http_proxy:
        proxy['http_proxy'] = http_proxy
    if HTTP_PROXY:
        proxy['HTTP_PROXY'] = HTTP_PROXY
    if https_proxy:
        proxy['https_proxy'] = https_proxy
    if HTTPS_PROXY:
        proxy['HTTPS_PROXY'] = HTTPS_PROXY
    if ftp_proxy:
        proxy['ftp_proxy'] = ftp_proxy
    if FTP_PROXY:
        proxy['FTP_PROXY'] = FTP_PROXY
    return proxy


def target_path_env(*prefixes):
    """
    Includes the new toolchain (x86_64-hardhat-linux-gnu) bin and sbin
    subdirectories as well as the root path.
    """

    path = ''
    for prefix in prefixes:
        if path:
            path += ':'
        path += toolchain_bin_dir(prefix)
        path += ':'
        path += toolchain_sbin_dir(prefix)
    if path:
        path += ':'
    path += ROOT_PATH

    arch = os.environ['HARDHAT_MARCH']
    cflags = '-O3 -mtune=native -march=%s' \
             ' -fomit-frame-pointer' \
             ' -momit-leaf-frame-pointer -DNDEBUG' % arch

    return dotdict({
        'PATH': path,
        'LDFLAGS': '',
        'LIBRARY_PATH': '',
        'LIBS': '',
        'LFLAGS': '',
        'CC': '',
        'CFLAGS': cflags,
        'CPP': 'cpp',
        'CPPFLAGS': '-DNDEBUG',
        'CXX': '',
        'CXXFLAGS': cflags,
        'AR': '',
        'AS': '',
        'FC': '',
        'F77': '',
        'F90': '',
        'F95': '',
        'LD': '',
        'RANLIB': '',
        'DLLTOOL': '',
        'PKGSRC_BASE_DIR': '',
        'PKGSRC_DIR': '',
        'PKGSRC_VERSION': '',
        'TMPDIR': toolchain_tmp_dir(prefixes[0]),
        'JAVA_HOME': '',
        'CCACHE_DISABLE': '1'
    })


def merge(dest, src):
    for k, v in src.items():
        dest[k] = v


def toolchain_env(*prefixes):
    env = target_path_env(*prefixes)
    merge(env, proxy_env())
    merge(env, OLD_LIB_ENV)
    return env


def clean_env(prefix):
    env = target_path_env(prefix)
    merge(env, CLEAN_PATH_ENV)
    merge(env, proxy_env())
    return env


def environment_strip_lto(env):
    env['CFLAGS'] = env['CFLAGS'] \
        .replace('-flto -ffat-lto-objects', '')
    env['CXXFLAGS'] = env['CFLAGS']
    env['LDFLAGS'] = env['LDFLAGS'] \
        .replace('-flto -fuse-linker-plugin', '')
