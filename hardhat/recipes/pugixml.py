import os
from .base import GnuRecipe


class PugiXmlRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PugiXmlRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fbe10d46f61d769f7d92a296102e4e2b' \
                      'd3ee16130f11c5b10a1aae590ea1f5ca'

        self.name = 'pugixml'
        self.version = '1.7'
        self.url = 'http://github.com/zeux/pugixml/releases/download/' \
                   'v$version/pugixml-$version.tar.gz'
        self.install_args += ['DESTDIR=%s' % self.prefix_dir]

    def patch(self):
        self.log_dir('patch', self.directory, 'adding Makefile')
        makefile = os.path.join(self.directory, 'Makefile')
        with open(makefile, 'wt') as f:
            f.write(MAKEFILE)

    def configure(self):
        pass


MAKEFILE = r"""
LIBNAME=pugixml
CXXFLAGS+=-std=c++11 -fPIC
SOURCES=$(shell find src -name *.cpp)
OBJECTS=$(patsubst %.cpp,%.o,$(SOURCES))
STATIC_LIB=lib$(LIBNAME).a
DYNAMIC_LIB=lib$(LIBNAME).so


.PHONY: all clean install

all:    $(STATIC_LIB) $(DYNAMIC_LIB)

%.o: %.cpp
	$(CXX) $(CXXFLAGS) -c $< -o $@

$(STATIC_LIB):  $(OBJECTS)
	$(AR) rcs $@ $(OBJECTS)

$(DYNAMIC_LIB): $(OBJECTS)
	$(CXX) $(LDFLAGS) $(OBJECTS) -shared -o $@

install:
	cp $(STATIC_LIB) $(DESTDIR)/lib
	cp $(DYNAMIC_LIB) $(DESTDIR)/lib
	cp src/* $(DESTDIR)/include


clean:
	rm -f *.o *.so *.a

"""
