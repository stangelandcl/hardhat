import os
from sys import platform
from .base import Mingw64BaseRecipe
from hardhat.urls import Urls
from hardhat.util import patch


class Mingw64CLapackRecipe(Mingw64BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64CLapackRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '6dc4c382164beec8aaed8fd2acc36ad2' \
                      '4232c406eda6db462bd4c41d5e455fac'

        # depends on wine but self.depends = ['wine'] doesn't work
        self.name = 'mingw64-clapack'
        self.version = '3.2.1'
        self.url = 'http://www.netlib.org/clapack/clapack.tgz'

#        if self.is_atom():
#            self.compile_args += ['TARGET=ATOM']
#        else:
#            # hardcoded because it failed to compile when detecting for itself
#            self.compile_args += ['TARGET=CORE2']

#        self.compile_args += ['USE_THREAD=1']
        self.install_args = ['cp', '*.a', '%s/lib' % self.prefix_dir]

    def patch(self):
        filename = os.path.join(self.directory, 'F2CLIBS', 'libf2c', 'Makefile')
        src = './a.out'
        dst = '%s/../bin/wine64 ./a.exe' % self.prefix_dir
        patch(filename, src, dst)

        filename = os.path.join(self.directory, 'INSTALL', 'second.c')
        text = r'''
#include "f2c.h"
#include <time.h>

doublereal second_()
{
        return (doublereal)(clock() / CLOCKS_PER_SEC);
} /* second_ */
'''
        with open(filename, 'wt') as f:
            f.write(text)

        filename = os.path.join(self.directory, 'INSTALL', 'dsecnd.c')
        text = r'''
#include "blaswrap.h"
#include "f2c.h"
#include <time.h>

doublereal dsecnd_()
{
        return (doublereal)(clock() / CLOCKS_PER_SEC);
} /* dsecnd_ */
'''
        with open(filename, 'wt') as f:
            f.write(text)

        filename = os.path.join(self.directory, 'make.inc')
        text = r'''
# -*- Makefile -*-
####################################################################
#  LAPACK make include file.                                       #
#  LAPACK, Version 3.2.1                                           #
#  June 2009		                                               #
####################################################################
#
# See the INSTALL/ directory for more examples.
#
SHELL = /bin/sh
#
#  The machine (platform) identifier to append to the library names
#
PLAT = _Winx64
#
#  Modify the FORTRAN and OPTS definitions to refer to the
#  compiler and desired compiler options for your machine.  NOOPT
#  refers to the compiler options desired when NO OPTIMIZATION is
#  selected.  Define LOADER and LOADOPTS to refer to the loader
#  and desired load options for your machine.
#
#######################################################
# This is used to compile C libary
CC        := $(CC)
# if no wrapping of the blas library is needed, uncomment next line
#CC        = gcc -DNO_BLAS_WRAP
CFLAGS    = -O3 -I$(TOPDIR)/INCLUDE -DUSE_CLOCK=1
LOADER    = gcc
LOADOPTS  =
NOOPT     = -O0 -I$(TOPDIR)/INCLUDE
DRVCFLAGS = $(CFLAGS)
F2CCFLAGS = $(CFLAGS)
#######################################################################

#
# Timer for the SECOND and DSECND routines
#
# Default : SECOND and DSECND will use a call to the EXTERNAL FUNCTION ETIME
# TIMER    = EXT_ETIME
# For RS6K : SECOND and DSECND will use a call to the EXTERNAL FUNCTION ETIME_
# TIMER    = EXT_ETIME_
# For gfortran compiler: SECOND and DSECND will use a call to the INTERNAL FUNCTION ETIME
# TIMER    = INT_ETIME
# If your Fortran compiler does not provide etime (like Nag Fortran Compiler, etc...)
# SECOND and DSECND will use a call to the Fortran standard INTERNAL FUNCTION CPU_TIME
TIMER    = INT_CPU_TIME
# If neither of this works...you can use the NONE value... In that case, SECOND and DSECND will always return 0
# TIMER     = NONE
#
#  The archiver and the flag(s) to use when building archive (library)
#  If you system has no ranlib, set RANLIB = echo.
#
ARCH     = $(AR)
ARCHFLAGS= cr
RANLIB   = ranlib
#
#  The location of BLAS library for linking the testing programs.
#  The target's machine-specific, optimized BLAS library should be
#  used whenever possible.
#
BLASLIB      = ../../blas$(PLAT).a
#
#  Location of the extended-precision BLAS (XBLAS) Fortran library
#  used for building and testing extended-precision routines.  The
#  relevant routines will be compiled and XBLAS will be linked only if
#  USEXBLAS is defined.
#
# USEXBLAS    = Yes
XBLASLIB     =
# XBLASLIB    = -lxblas
#
#  Names of generated libraries.
#
LAPACKLIB    = lapack$(PLAT).a
F2CLIB       = ../../F2CLIBS/libf2c.a
TMGLIB       = tmglib$(PLAT).a
EIGSRCLIB    = eigsrc$(PLAT).a
LINSRCLIB    = linsrc$(PLAT).a
F2CLIB		 = ../../F2CLIBS/libf2c.a

'''
        with open(filename, 'wt') as f:
            f.write(text)

        src = '"stdio.h"'
        dst = '<stdio.h>'
        patch(os.path.join(self.directory, 'SRC', 'xerbla.c'), src, dst)

    def configure(self):
        pass

    def is_atom(self):
        lines = []
        if platform == "linux" or platform == "linux2":
            with open('/proc/cpuinfo', 'rt') as f:
                lines = f.readlines()

        for line in lines:
            if line.startswith('model name'):
                model = line[len('model_name'):].strip()
                model = model[2:]
                if 'Intel(R) Celeron(R) CPU  N2940' in model:
                    return True
                break
        return False

    def compile(self):
        args = self.compile_args

        self.compile_args = args + ['f2clib']
        super(Mingw64CLapackRecipe, self).compile()

        self.compile_args = args + ['blaslib']
        super(Mingw64CLapackRecipe, self).compile()

        dir = self.directory
        self.directory = os.path.join(self.directory, 'INSTALL')
        self.compile_args = args + ['slamch.o', 'second.o', 'dlamch.o', 'dsecnd.o', 'ilaver.o', 'lsame.o']
        super(Mingw64CLapackRecipe, self).compile()
        self.directory = dir

        dir = self.directory
        self.directory = os.path.join(self.directory, 'SRC')
        self.compile_args = args
        super(Mingw64CLapackRecipe, self).compile()
        self.directory = dir
