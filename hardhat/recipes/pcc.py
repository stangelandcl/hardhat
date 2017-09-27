import os
from .base import GnuRecipe
from ..version import extension_regex
from ..util import patch


class PccRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PccRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'ea7a5be2ca10640f7cbadfb04ac5106e' \
                      '1d9f33df066c26f1d1fdc6b3c406d7f9'
        self.description = 'broken Portable C compiler.' \
                           " It can't handle multiple include directories"
        self.name = 'pcc'
        self.version = '20170927'
        self.version_regex = r'pcc-(?P<version>\d+)' + extension_regex
        self.version_url = 'http://pcc.ludd.ltu.se/ftp/pub/pcc/'
        self.url = 'http://pcc.ludd.ltu.se/ftp/pub/pcc/pcc-$version.tgz'
        self.depends = ['bison']
        gcc_version = '7.1.0'
        self.configure_args += [
            '--enable-tls',
            '--with-incdir=%s/include:%s/%s/include:%s/include/linux:%s/lib/gcc/%s/%s/include' %
            (self.prefix_dir,
             self.prefix_dir,
             self.target_triplet,
             self.prefix_dir,
             self.prefix_dir,
             self.target_triplet,
             gcc_version),
            '--with-libdir=%s/lib' % self.prefix_dir
            ]


    def patch(self):
        pcc = os.path.join(self.prefix_dir, 'bin', 'pcc')
        if os.path.exists(pcc):
            os.remove(pcc)
        self.log_dir('patch', self.directory, 'allow multiple includedirs')
        filename = os.path.join(self.directory, 'cc/cc/cc.c')
        text = r'''
        char buf[4096], buf2[4096];
        char *next, *str=buf;
        strcpy(buf, STDINC);
#if 0
        printf("INCLUDEDIR=%s\n", INCLUDEDIR);
        printf("PCCINCDIR=%s\n", PCCINCDIR);
        printf("STDINC=%s\n", STDINC);
#endif
        while((next=strtok(str, ":")))
        {
            str = NULL;
            buf2[0] = '=';
            strcpy(&buf2[1], next);
            printf("including %s\n", next);
            strlist_append(&sysincdirs, buf2);
        }
'''
        patch(filename,
              'strlist_append(&sysincdirs, "=" STDINC);',
              text)
