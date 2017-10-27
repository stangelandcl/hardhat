#!/bin/bash

set -e

# Parsing from http://stackoverflow.com/questions/192249/how-do-i-parse-command-line-arguments-in-bash
PREFIX=""
DOWNLOAD_DIR="~/Downloads/hardhat"
CPUS=.9
MARCH="core2"
USE_ROOT=
unset HARDHAT_TARGET
unset HARDHAT_USE_ROOT

for i in "$@"; do
    case $i in
	--prefix=*)
	    PREFIX="${i#*=}"
	    ;;
	--downloads=*)
	    DOWNLOAD_DIR="${i#*=}"
	    ;;
	--cpus=*)
	    CPUS="${i#*=}"
	    ;;
	--pkgfile=*)
	    PKG_FILE="${i#*=}"
	    PKG_FILE="${PKG_FILE/#\~/$HOME}"
	    ;;
	--march=*)
	    MARCH="${i#*=}"
	    ;;
    --use-root*)
        USE_ROOT="--use-root"
        ;;
	*)
	    # skip unknown
	    ;;
    esac
done

if [ -z "$PREFIX" ]; then
    echo "This script downloads setuptools, argparse and importlib python packages."
    echo "These are required by hardhat but not included in Python 2.6"
    echo "It then installs these into a local ./bootstrap directory where it will "
    echo "run hardhat from to build the toolchain, python3, and install hardhat into"
    echo "your chosen prefix/sysroot (PREFIX) directory."
    echo
    echo "Usage: ./bootstrap.sh --prefix=PREFIX [--downloads=DOWNLOAD_DIR] [--cpus=CPUS] [--pkgfile=PKG_FILE] [--use-root]"
    echo "PREFIX = directory to create new sysroot at"
    echo "DOWNLOAD_DIR = default is ~/Downloads/hardhat"
    echo "CPUS = default is .9 (for 90%) use 100 for 100% or an integer like 2 for 2 cores"
    echo "--use-root for not building gcc and glibc but using root and using root libraries"
    echo "When bootstrap is finished run '. PREFIX/init.sh' (without the quotes) to use"
    echo "the new sysroot."
    exit 1
fi

function check_prerequisites()
{
    set +e

    required=(gcc g++ make patch)
    missing=0
    for exe in ${required[@]}; do
        command -v $exe >/dev/null 2>&1
        if [ $? -ne 0 ]; then
            echo "'$exe' is required to bootstrap"
            missing=1
        fi
    done

    if [ $missing -ne 0 ]; then
        exit 1
    fi
    
    set -e
}

check_prerequisites

# From http://stackoverflow.com/questions/3963716/how-to-manually-expand-a-special-variable-ex-tilde-in-bash
# Replace ~ with $HOME because ~/path/bin/python3 will not be found at the end if tilde is used.
PREFIX="${PREFIX/#\~/$HOME}"


DIR=$PWD
export PYTHONPATH=$DIR/bootstrap/lib/python
SETUPTOOLS=setuptools-20.10.1
ARGPARSE=argparse-1.4.0
IMPORTLIB=importlib-1.0.3

if [ ! -e $DIR/$SETUPTOOLS.tar.gz ]; then
    wget https://pypi.python.org/packages/d3/16/21cf5dc6974280197e42d57bf7d372380562ec69aef9bb796b5e2dbbed6e/$SETUPTOOLS.tar.gz
fi

if [ ! -e $DIR/setuptools ]; then
    tar xvf $SETUPTOOLS.tar.gz
    mv $SETUPTOOLS setuptools
fi

if [ ! -e $DIR/$ARGPARSE.tar.gz ]; then
    wget https://pypi.python.org/packages/18/dd/e617cfc3f6210ae183374cd9f6a26b20514bbb5a792af97949c5aacddf0f/$ARGPARSE.tar.gz
fi

if [ ! -e $DIR/argparse ]; then
    tar xvf $ARGPARSE.tar.gz
    mv $ARGPARSE argparse
fi

if [ ! -e $DIR/$IMPORTLIB.tar.gz ]; then
    wget https://pypi.python.org/packages/0e/9c/daad476c540c4c36e7b35cf367331f0acf10d09d112cc5083c3e16a77347/$IMPORTLIB.tar.gz
fi

if [ ! -e $DIR/importlib ]; then
    tar xvf $IMPORTLIB.tar.gz
    mv $IMPORTLIB importlib
fi

if [ ! -f $DIR/bootstrap/bin/hardhat ]; then
    rm -rf $DIR/bootstrap

    if [ ! -x "$(which $PYTHON)" ]; then   
	if [ -x "$(which python3)" ]; then
            PYTHON="$(which python3)"       
	elif [ -x "$(which python2)" ]; then
            PYTHON="$(which python2)"
	elif [ -x "$(which python)" ]; then
            PYTHON="$(which python)"
	else
            echo "$PYTHON, python, python2 or python3 is required"
            exit 1
	fi
    fi                         

    if [ ! -e $DIR/bootstrap ]; then
	mkdir -p $DIR/bootstrap/lib/python
	cd setuptools && "$PYTHON" setup.py install --home=$DIR/bootstrap
	cd ..
	cd argparse && "$PYTHON" setup.py install --home=$DIR/bootstrap
	cd ..
	cd importlib && "$PYTHON" setup.py install --home=$DIR/bootstrap
	cd ..
    fi

    if [ ! -f $DIR/bootstrap/bin/hardhat ]; then
	"$PYTHON" setup.py install --home=$DIR/bootstrap
    fi
fi

OLDPATH=$PATH
export PATH=$DIR/bootstrap/bin:$PATH
if [ ! -e $PREFIX/bin/python3 ]; then
    if [ -e $PREFIX/init.sh ]; then
	# for HARDHAT_TARGET so we use the same compiler
	. $PREFIX/init.sh
	# init.sh overwrites path
	export PATH=$DIR/bootstrap/bin:$PATH
    fi
    hardhat $USE_ROOT --march=$MARCH --cpus=$CPUS --prefix=$PREFIX --downloads=$DOWNLOAD_DIR install python3-beautifulsoup
fi
export PATH=$PREFIX/bin:$OLDPATH
export PYTHONPATH=""

if [ ! -e $PREFIX/bin/hardhat ]; then
    cp -R $DIR $PREFIX/hardhat
    rm -rf $PREFIX/hardhat/bootstrap
    rm -rf $PREFIX/hardhat/build
    rm -rf $PREFIX/hardhat/dist
    rm -f $PREFIX/hardhat/*.tar.gz
    # To set HARDHAT_TARGET environment variable correctly
    . $PREFIX/init.sh
    cd $PREFIX/hardhat && $PREFIX/bin/python3 setup.py develop
fi

if [ "$PKG_FILE" != "" ]; then       
    hardhat $USE_ROOT --march=$MARCH --cpus=$CPUS --prefix=$PREFIX --downloads=$DOWNLOAD_DIR install --file=$PKG_FILE
fi

echo "Run '. $PREFIX/init.sh' or 'source $PREFIX/init.sh' (without quotes) to step into your new sysroot environment at $PREFIX."


