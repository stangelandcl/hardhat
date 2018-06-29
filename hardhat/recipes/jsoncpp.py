import os
import shutil
from .base import GnuRecipe


class JsonCppRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(JsonCppRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'c49deac9e0933bcb7044f08516861a2d' \
                      '560988540b23de2ac1ad443b219afdb6'

        self.name = 'jsoncpp'
        self.version = '1.8.4'
        self.version_url = 'https://github.com/open-source-parsers/' \
                           'jsoncpp/releases/'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)\.tar\.gz'
        self.url = 'https://github.com/open-source-parsers/jsoncpp/archive/' \
                   '$version.tar.gz'

        self.configure_args = ['python2',
                               'amalgamate.py']

        self.dist = os.path.join(self.directory, 'dist')
        self.install_args = ['make', 'install', 'DESTDIR=%s' % self.prefix_dir]

    def patch(self):
        if not os.path.exists(self.dist):
            os.makedirs(self.dist)

        makefile = os.path.join(self.dist, 'Makefile')
        with open(makefile, 'wt') as f:
            f.write(MAKEFILE)

    def compile(self):
        dir = self.directory
        self.directory = self.dist
        super(JsonCppRecipe, self).compile()

MAKEFILE = r'''
LIBNAME=jsoncpp
CXX?=g++
AR?=ar
SOURCES=jsoncpp.cpp
OBJECTS=jsoncpp.o
STATIC_LIB=libjsoncpp.a
DYNAMIC_LIB=libsoncpp.so
prefix	=
exec_prefix = $(prefix)
libdir = $(exec_prefix)/lib
includedir = $(prefix)/include
datarootdir = $(prefix)/share
mandir = $(datarootdir)/man


.PHONY:	all clean install

all:	$(STATIC_LIB) $(DYNAMIC_LIB)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -fPIC -c $<

$(STATIC_LIB):	$(OBJECTS)
	$(AR) rcs $@ $(OBJECTS)

$(DYNAMIC_LIB): $(OBJECTS)
	$(CXX) $(LDFLAGS) $(OBJECTS) -shared -o $@

install:
	cp $(STATIC_LIB) $(DESTDIR)$(libdir)
	cp $(DYNAMIC_LIB) $(DESTDIR)$(libdir)
	cp -R json $(DESTDIR)$(includedir)
	cp jsoncpp.cpp $(DESTDIR)$(includedir)/json

clean:
	rm -f *.o *.so *.a

'''
