import os
from .base import GnuRecipe
from ..urls import Urls


class ArdbRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ArdbRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '9dfe021e96598ca0179b120536645028' \
                      '8d540b05d2f43902092c3b57de4dc0bb'

        self.name = 'ardb'
        self.description = 'client-server key value database in C++'
        self.version = '0.9.3'
        self.url = Urls.github_commit('yinqiwen', self.name,
                                      'v' + self.version)
        self.depends = ['cJSON', 'cpp-btree',
                        'jemalloc', 'lmdb', 'lua',
                        'snappy', 'sparsehash']
        self.compile_args += ['storage_engine=lmdb']

    def configure(self):
        pass

    def patch(self):
        text = r'''
#-------------------------------------------------------------------------------
# Copyright (c) 2013-2016, yinqiwen <yinqiwen@gmail.com>
# All rights reserved.
#
# Redistribution and use in source and binary forms, with or without
# modification, are permitted provided that the following conditions are met:
#
#   * Redistributions of source code must retain the above copyright notice,
#     this list of conditions and the following disclaimer.
#   * Redistributions in binary form must reproduce the above copyright
#     notice, this list of conditions and the following disclaimer in the
#     documentation and/or other materials provided with the distribution.
#   * Neither the name of Redis nor the names of its contributors may be used
#     to endorse or promote products derived from this software without
#     specific prior written permission.
#
# THIS SOFTWARE IS PROVIDED BY THE COPYRIGHT HOLDERS AND CONTRIBUTORS "AS IS"
# AND ANY EXPRESS OR IMPLIED WARRANTIES, INCLUDING, BUT NOT LIMITED TO, THE
# IMPLIED WARRANTIES OF MERCHANTABILITY AND FITNESS FOR A PARTICULAR PURPOSE
# ARE DISCLAIMED. IN NO EVENT SHALL THE COPYRIGHT OWNER OR CONTRIBUTORS
# BE LIABLE FOR ANY DIRECT, INDIRECT, INCIDENTAL, SPECIAL, EXEMPLARY, OR
# CONSEQUENTIAL DAMAGES (INCLUDING, BUT NOT LIMITED TO, PROCUREMENT OF
# SUBSTITUTE GOODS OR SERVICES; LOSS OF USE, DATA, OR PROFITS; OR BUSINESS
# INTERRUPTION) HOWEVER CAUSED AND ON ANY THEORY OF LIABILITY, WHETHER IN
# CONTRACT, STRICT LIABILITY, OR TORT (INCLUDING NEGLIGENCE OR OTHERWISE)
# ARISING IN ANY WAY OUT OF THE USE OF THIS SOFTWARE, EVEN IF ADVISED OF
# THE POSSIBILITY OF SUCH DAMAGE.
#-------------------------------------------------------------------------------
#Makefile
#
# Created on: 2013-3-28
#     Author: yinqiwen

CXX?=g++
CC?=gcc

ARDB_VERSION=0.9.3

uname_S := $(shell sh -c 'uname -s 2>/dev/null || echo not')

LIB_PATH=$(PWD)/../deps


# Cross compiling variables
XC_HOST=
XC_TGT=
XC_BUILD=

OPTIMIZATION?=-O0
OPT=$(OPTIMIZATION)

CXXFLAGS=-Wall -g ${OPT} -fPIC -D__STDC_FORMAT_MACROS -D__STDC_LIMIT_MACROS -DARDB_VERSION='"${ARDB_VERSION}"'
CCFLAGS=-Wall -std=gnu99 ${OPT} -fPIC -pedantic -g -D__STDC_FORMAT_MACROS -DARDB_VERSION='"${ARDB_VERSION}"'
LDFLAGS=-g

LEVELDB_OPT=-g $(OPT)

INCS=-I./ -I./common -I${LIB_PATH}/cpp-btree -DLUA_COMPAT_5_1 -DLUA_COMPAT_5_2


ifeq ($(MALLOC),libc)
#do nothing
else
MALLOC_LIBA=-ljemalloc
DEP_LIBS+=jemalloc
endif

storage_engine?=lmdb

LIBS=-llua ${MALLOC_LIBA} -lsnappy -llmdb -lpthread

# Default allocator
ifeq ($(uname_S),Linux)
	MALLOC=jemalloc
	CXXFLAGS+=-DCORO_ASM
	CCFLAGS+=-DCORO_ASM
	LIBS+=-lrt
else
	MALLOC=libc
	CXXFLAGS+=-DCORO_UCONTEXT -D_XOPEN_SOURCE
	CCFLAGS+=-DCORO_UCONTEXT -D_XOPEN_SOURCE
endif

%.o : %.cpp
	${CXX} -c ${CXXFLAGS} ${INCS} $< -o $@

%.o : %.c
	${CC} -c ${CCFLAGS} ${INCS} $< -o $@


COMMON_VPATH=common/channel common/channel/socket common/channel/fifo common/channel/codec common/channel/timer common/channel/signal \
             common/util common/util/exception  common/thread  common/coro common/redis common/buffer common/geo common/channel/redis
COMMON_CPPFILES := $(foreach dir, $(COMMON_VPATH), $(wildcard $(dir)/*.cpp))
COMMON_CFILES := $(foreach dir, $(COMMON_VPATH), $(wildcard $(dir)/*.c))
COMMON_OBJECTS := $(patsubst %.cpp, %.o, $(COMMON_CPPFILES)) $(patsubst %.c, %.o, $(COMMON_CFILES))

COMMAND_VPATH=command
COMMAND_CPPFILES := $(foreach dir, $(COMMAND_VPATH), $(wildcard $(dir)/*.cpp))
COMMAND_OBJECTS := $(patsubst %.cpp, %.o, $(COMMAND_CPPFILES))

DB_VPATH=db repl
DB_CPPFILES := $(foreach dir, $(DB_VPATH), $(wildcard $(dir)/*.cpp))
DB_CFILES := $(foreach dir, $(DB_VPATH), $(wildcard $(dir)/*.c))
DB_OBJECTS := $(patsubst %.cpp, %.o, $(DB_CPPFILES)) $(patsubst %.c, %.o, $(DB_CFILES))

CORE_OBJECTS :=  config.o cron.o logger.o network.o types.o statistics.o\
                $(COMMON_OBJECTS)  $(COMMAND_OBJECTS) $(DB_OBJECTS)

TESTOBJ := ../test/test_main.o
REPAIR_TOOL_OBJ := tools/repair.o
SERVEROBJ := main.o

STORAGE_ENGINE_VPATH=db/${storage_engine}
STORAGE_ENGINE_CPPFILES := $(foreach dir, $(STORAGE_ENGINE_VPATH), $(wildcard $(dir)/*.cpp))
STORAGE_ENGINE_CFILES := $(foreach dir, $(STORAGE_ENGINE_VPATH), $(wildcard $(dir)/*.c))
STORAGE_ENGINE_OBJ := $(patsubst %.cpp, %.o, $(STORAGE_ENGINE_CPPFILES)) $(patsubst %.c, %.o, $(STORAGE_ENGINE_CFILES))
STORAGE_ENGINE_ALL_OBJ := db/*/*.o


#DIST_LIB = libardb.so
DIST_LIBA = libardb.a

ifeq ($(storage_engine), leveldb)
  STORAGE_ENGINE=$(LEVELDB_LIBA)
  STORAGE_ENGINE_PATH=$(LEVELDB_PATH)
  INCS+=-I${LEVELDB_PATH}/include
  LIBS:=${LEVELDB_LIBA} ${LIBS}
  CXXFLAGS+=-D__USE_LEVELDB__
else
ifeq ($(storage_engine), forestdb)
  STORAGE_ENGINE=$(FORESTDB_LIBA)
  STORAGE_ENGINE_PATH=$(FORESTDB_PATH)
  INCS+=-I${FORESTDB_PATH}/include
  LIBS:=${FORESTDB_LIBA} ${LIBS}
  CXXFLAGS+=-D__USE_FORESTDB__
  ifeq ($(uname_S),Darwin)
     SEDCMD:=sed -i '.bak' 's/SHARED/STATIC/g' CMakeLists.txt
  else
     SEDCMD:=sed -i 's/SHARED/STATIC/g' CMakeLists.txt
  endif
  ifneq ("$(wildcard /usr/include/libaio.h)","")
     LIBS+=-laio
  endif
else
ifeq ($(storage_engine), lmdb)
  STORAGE_ENGINE=$(LMDB_LIBA)
  STORAGE_ENGINE_PATH=$(LMDB_PATH)
  CXXFLAGS+=-D__USE_LMDB__
else
ifeq ($(storage_engine), rocksdb)
  STORAGE_ENGINE=$(ROCKSDB_LIBA)
  STORAGE_ENGINE_PATH=$(ROCKSDB_PATH)
  INCS+=-I${ROCKSDB_PATH}/include
  LIBS:= ${ROCKSDB_LIBA} ${LIBS} -lz -lbz2
  CXXFLAGS+=-D__USE_ROCKSDB__ -std=c++11
else
ifeq ($(storage_engine), wiredtiger)
  STORAGE_ENGINE=$(WIREDTIGER_LIBA)
  STORAGE_ENGINE_PATH=$(WIREDTIGER_PATH)
  INCS+=-I${WIREDTIGER_PATH}
  #wiredtiger use dlsym to load extension, must use -rdynamic to export symbol
  LIBS:= ${WIREDTIGER_LIBA} ${LIBS} -rdynamic -ldl
  CXXFLAGS+=-D__USE_WIREDTIGER__
else
ifeq ($(storage_engine), perconaft)
  STORAGE_ENGINE=$(PERCONAFT_LIBA)
  STORAGE_ENGINE_PATH=$(PERCONAFT_PATH)
  INCS+=-I${PERCONAFT_PATH}/prefix/include
  LIBS:= ${PERCONAFT_LIBA} ${PERCONAFT_LIBA2} ${LIBS} -lz -ldl
  CXXFLAGS+=-D__USE_PERCONAFT__
else
  $(error Only leveldb/lmdb/rocksdb/perconaft/wiredtiger/forestdb supported as env storage_engine value)
endif
endif
endif
endif
endif
endif

LAST_ENGINE := $(shell sh -c 'cat .kv_engine 2>&1')
ifeq ($(storage_engine), $(LAST_ENGINE))
#do nothing
else
   $(shell sh -c 'echo $(storage_engine) > .kv_engine')
   PREBUILD = clean_db_obj
endif
#

#$(CORE_OBJECTS) $(SERVEROBJ) $(TESTOBJ): |  $(STORAGE_ENGINE_PATH)

all: ${PREBUILD}  test server tools

$(STORAGE_ENGINE_OBJ): $(STORAGE_ENGINE)

$(DIST_LIB): $(STORAGE_ENGINE_OBJ) $(CORE_OBJECTS)
	${CXX} -shared -o $@ $^

$(DIST_LIBA):$(STORAGE_ENGINE_OBJ) $(CORE_OBJECTS)
	ar rcs $@ $^

lib: $(DIST_LIBA)

server: lib $(CORE_OBJECTS) ${SERVEROBJ}
	${CXX} -o ardb-server $(SERVEROBJ)  $(CORE_OBJECTS) ${STORAGE_ENGINE_OBJ} $(LIBS)

test: lib ${TESTOBJ} $(CORE_OBJECTS)
	${CXX} -o ardb-test ${STORAGE_ENGINE_OBJ} ${TESTOBJ} $(CORE_OBJECTS) $(LIBS)

tools: repair

repair: lib ${REPAIR_TOOL_OBJ}
	${CXX} -o ardb-repair ${REPAIR_TOOL_OBJ} $(DIST_LIBA) $(LIBS)


clean_db_obj:
	rm -f db/db.o

clean_test:
	rm -f ${TESTOBJ};rm -f ardb-test

clean_deps:
	rm -rf $(LEVELDB_PATH) 	$(ROCKSDB_PATH)
	$(MAKE) -C $(LUA_PATH) clean

noopt:
	$(MAKE) OPT="-O0"

valgrind:
	$(MAKE) OPT="-O0" MALLOC="libc"

dist:clean all
	rm -rf ardb-${ARDB_VERSION};mkdir -p ardb-${ARDB_VERSION}/bin ardb-${ARDB_VERSION}/conf ardb-${ARDB_VERSION}/logs ardb-${ARDB_VERSION}/data ardb-${ARDB_VERSION}/repl ardb-${ARDB_VERSION}/backup; \
	cp ardb-server ardb-${ARDB_VERSION}/bin; cp ardb-test ardb-${ARDB_VERSION}/bin; cp ardb-repair ardb-${ARDB_VERSION}/bin; cp ../ardb.conf ardb-${ARDB_VERSION}/conf; \
	tar czvf ardb-bin-${ARDB_VERSION}.tar.gz ardb-${ARDB_VERSION}; rm -rf ardb-${ARDB_VERSION};

clean:
	rm -f  ${CORE_OBJECTS} $(SERVEROBJ) ${STORAGE_ENGINE_ALL_OBJ} ${TESTOBJ} ${REPAIR_TOOL_OBJ} ${DIST_LIBA} ${DIST_LIB} \
	       ardb-test  ardb-server ardb-repair

clobber: clean_deps clean

'''

        filename = os.path.join(self.directory, 'src', 'Makefile')
        with open(filename, 'wt') as f:
            f.write(text)

        text = r'''
 diff -Naur ardb-0.9/src/command/lua_scripting.cpp ardb-0.9.bak/src/command/lua_scripting.cpp
--- ardb-0.9/src/command/lua_scripting.cpp	2016-09-20 02:00:25.000000000 +0000
+++ ardb-0.9.bak/src/command/lua_scripting.cpp	2017-01-10 00:08:04.295668694 +0000
@@ -42,13 +42,17 @@

 #define MAX_LUA_STR_SIZE 1024

+#define lua_open() lua_newstate(NULL, NULL)
+
 namespace ardb
 {
     extern "C"
     {
+        #if 0
         int (luaopen_cjson)(lua_State *L);
         int (luaopen_struct)(lua_State *L);
         int (luaopen_cmsgpack)(lua_State *L);
+        #endif
     }
     static const char* g_lua_file = "";
     struct LuaExecContext
@@ -442,9 +446,11 @@
         luaLoadLib(m_lua, LUA_MATHLIBNAME, luaopen_math);
         luaLoadLib(m_lua, LUA_DBLIBNAME, luaopen_debug);

+	#if 0
         luaLoadLib(m_lua, "cjson", luaopen_cjson);
         luaLoadLib(m_lua, "struct", luaopen_struct);
         luaLoadLib(m_lua, "cmsgpack", luaopen_cmsgpack);
+	#endif
         return 0;
     }

'''
        self.apply_patch(self.directory, text)
