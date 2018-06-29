import os
from .base import GnuRecipe
from ..util import patch, gcc_version


class ICURecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ICURecipe, self).__init__(*args, **kwargs)
        self.name = 'icu'

        version = gcc_version(self.environment['CC'])
        if version[0] <= 4 or (version[0] == 4 and version[1] < 8):
            self.sha256 = '2b0a4410153a9b20de0e20c7d8b66049' \
                          'a72aef244b53683d0d7521371683da0c'
            self.version = '58.2'
        else:
            self.sha256 = '3dd9868d666350dda66a6e305eecde9d' \
                          '479fb70b30d5b55d78a1deffb97d5aa3'
            self.version = '62.1'  # 59.1 gcc 4.8+ required
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
        super(ICURecipe, self).clean()
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
        if int(self.version.split('.')[0]) < 59:
            filename = os.path.join(
                self.directory, 'source', 'common', 'ulist.c')
            patch(filename, 'int32_t currentIndex;', '')
            patch(filename, 'newList->currentIndex = -1;', '')
            patch(filename, 'list->currentIndex++;', '')
            patch(filename, 'list->currentIndex = 0;', '')
            src = r'''    list->curr = NULL;'''
            dst = r'''    if (p == list->curr) {
     list->curr = p->next;
 }
'''
            patch(filename, src, dst)

            text = r'''
Submitted By: Pierre Labastie <pierre dot labastie at neuf dot fr>
Date: 2016-11-15
Initial Package Version: 58.1
Upstream Status: Applied
Origin: Upstream, rediffed so that patch -p1 works.
Description: Fix a regression in 58.1, which made mozilla applications

diff -Naur icu.old/source/i18n/ucol_res.cpp icu.new/source/i18n/ucol_res.cpp
--- icu.old/source/i18n/ucol_res.cpp	2016-09-28 04:26:02.000000000 +0200
+++ icu.new/source/i18n/ucol_res.cpp	2016-11-15 16:11:10.000596933 +0100
@@ -680,6 +680,7 @@
         return NULL;
     }
     memcpy(en, &defaultKeywordValues, sizeof(UEnumeration));
+    ulist_resetList(sink.values);  // Initialize the iterator.
     en->context = sink.values;
     sink.values = NULL;  // Avoid deletion in the sink destructor.
     return en;
'''
            self.apply_patch(self.directory, text)
        self.directory = os.path.join(self.directory, 'source')
