import os
from .base import Mingw64BaseRecipe
from hardhat.util import patch


class Mingw64IcuRecipe(Mingw64BaseRecipe):
    def __init__(self, *args, **kwargs):
        super(Mingw64IcuRecipe, self).__init__(*args, **kwargs)
        self.name = 'mingw64-icu'
        self.version = '62.1'
        self.version_regex = '(?P<version>\d+\.\d+)/'
        self.version_url = 'http://download.icu-project.org/files/icu4c/'
        underscore_version = self.version.replace('.', '_')
        self.url = 'http://download.icu-project.org/files/icu4c/$version/' \
            'icu4c-%s-src.tgz' % (underscore_version)

        # ICU requires a working host ICU to cross-compile
        if self.mingw64:
            self.configure_args += ['--with-cross-build=%s/build/%s/source' %
                                    (os.environ['HARDHAT_PREFIX'],
                                     os.path.basename(self.directory))]
        else:
            self.configure_strip_cross_compile()
        self.environment_strip_lto()
        self.environment['CXXFLAGS'] += ' -fvisibility=default'
        self.environment['CFLAGS'] += ' -fvisibility=default'
        self.environment['LDFLAGS'] += ' -fvisibility=default'
        self.compile_args += ['VERBOSE=1']
        self.post_clean = False  # needed to cross compile later

    def clean(self):
        super(Mingw64IcuRecipe, self).clean()
        self.log_dir('clean', self.directory, 'removing old libicus')
        files = ['libicudata',
                 'libicui18n',
                 'libicuio',
                 'libicule',
                 'libiculx',
                 'libicutest',
                 'libicutu',
                 'libicuuc']
        dir = os.path.join(self.prefix_dir, 'lib')
        for file in files:
            args = ['rm', '-f', file + '.*']
            self.run_exe(args, dir, self.environment)

    def patch(self):
       ##  return # since 59.1

##         filename = os.path.join(self.directory, 'source', 'common', 'ulist.c')
##         patch(filename, 'int32_t currentIndex;', '')
##         patch(filename, 'newList->currentIndex = -1;', '')
##         patch(filename, 'list->currentIndex++;', '')
##         patch(filename, 'list->currentIndex = 0;', '')
##         src = r'''    list->curr = NULL;'''
##         dst = r'''    if (p == list->curr) {
##         list->curr = p->next;
##     }
## '''
##         patch(filename, src, dst)


##         text = r'''
## Submitted By: Pierre Labastie <pierre dot labastie at neuf dot fr>
## Date: 2016-11-15
## Initial Package Version: 58.1
## Upstream Status: Applied
## Origin: Upstream, rediffed so that patch -p1 works.
## Description: Fix a regression in 58.1, which made mozilla applications

## diff -Naur icu.old/source/i18n/ucol_res.cpp icu.new/source/i18n/ucol_res.cpp
## --- icu.old/source/i18n/ucol_res.cpp	2016-09-28 04:26:02.000000000 +0200
## +++ icu.new/source/i18n/ucol_res.cpp	2016-11-15 16:11:10.000596933 +0100
## @@ -680,6 +680,7 @@
##          return NULL;
##      }
##      memcpy(en, &defaultKeywordValues, sizeof(UEnumeration));
## +    ulist_resetList(sink.values);  // Initialize the iterator.
##      en->context = sink.values;
##      sink.values = NULL;  // Avoid deletion in the sink destructor.
##      return en;
## '''
##         self.apply_patch(self.directory, text)
        self.directory = os.path.join(self.directory, 'source')

        if self.mingw64:
            filename = os.path.join(self.directory, 'common', 'putil.cpp')
            self.log_dir('patch', self.directory, 'fix slashes in includes')
            files = [
                r'unicode\uloc.h',
                r'wrl\wrappers\corewrappers.h',
                r'wrl\client.h',
                ]
            for file in files:
                patch(filename, file, file.replace('\\', '/'))

            self.log_dir('patch', self.directory, 'disable strtod_l')
            src = '#   define U_USE_STRTOD_L 1'
            dst = '#   define U_USE_STRTOD_L 0'
            filename = os.path.join(self.directory, 'i18n/digitlst.cpp')
            patch(filename, src, dst)

            src = r'''        // TODO: test this code path, including wperm.
        wchar_t wperm[40] = {};
        size_t  retVal;
        mbstowcs_s(&retVal, wperm, perm, _TRUNCATE);
        FILE *systemFile = _wfopen((const wchar_t *)filename, wperm);
        if (systemFile) {
            result = finit_owner(systemFile, locale, codepage, TRUE);
        }
        if (!result) {
            /* Something bad happened.
               Maybe the converter couldn't be opened. */
            fclose(systemFile);
        }'''
            dst = ''
            filename = os.path.join(self.directory, 'io/ufile.cpp')
            self.log_dir('patch', self.directory, 'disable mbstowcs_s')
            patch(filename, src, dst)

            filename = os.path.join(self.directory, 'tools/toolutil/pkg_genc.cpp')
            src = '#include "pkg_genc.h"'
            dst = src + '\n#include "filetools.h"\n'
            patch(filename, src, dst)
