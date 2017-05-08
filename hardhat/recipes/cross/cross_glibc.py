import os
import shutil
from hardhat.util import check_directory, run_or_error, patch
from .base import CrossGnuRecipe


class CrossGLibCRecipe(CrossGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CrossGLibCRecipe, self).__init__(*args, **kwargs)
        self.sha256 = self.glibc_sha256
        self.name = 'cross-glibc'
        self.version = self.glibc_version
        self.url = 'http://ftp.wayne.edu/gnu/libc/glibc-%s.tar.gz' \
            % (self.version)

        self.directory = os.path.join(self.base_extract_dir,
                                      '%s-%s-build' % (
                                          self.name,
                                          self.version))
        # directory is not set until after extract
        self.configure_args = self.shell_args + [
            '%s/configure' % (self.extract_dir),
            '--prefix=%s/%s' % (self.cross_prefix_dir,
                                self.target_triplet),
            '--host=%s' % (self.target_triplet),
            '--build=$(%s/scripts/config.guess)' % (self.extract_dir),
            '--enable-kernel=2.6.32',
            '--libdir=%s/%s/lib64' % (self.cross_prefix_dir,
                                      self.target_triplet),
            '--without-selinux',
            '--with-headers=%s/%s/include' % (self.cross_prefix_dir,
                                              self.target_triplet),
            'libc_cv_forced_unwind=yes',
            'libc_cv_c_cleanup=yes'
            ]

    def version_check(self):
        pass

    def clean(self):
        if os.path.exists(self.extract_dir):
            shutil.rmtree(self.extract_dir)
        if os.path.exists(self.directory):
            shutil.rmtree(self.directory)

    def symlink_crts(self):
        # in gcc pass 2 xgcc when build libgcc refuses to search in lib64
        src = os.path.join(self.cross_prefix_dir,
                           self.target_triplet, 'lib64')
        dst = os.path.join(self.cross_prefix_dir,
                           self.target_triplet, 'lib')
        self.log_dir('symlink_crts', src, 'symlink crts for gcc pass 2')
        for file in os.listdir(src):
            src_file = os.path.join(src, file)
            dst_file = os.path.join(dst, file)
            os.symlink(src_file, dst_file)

    def patch(self):
        self.log_dir('patch', self.directory, 'creating build directory')
        check_directory(self.directory)

        with open(os.path.join(self.directory, 'configparms'), 'wt') as f:
            f.write("slibdir=%s/%s/lib64\n" % (self.cross_prefix_dir,
                                               self.target_triplet))

        # _CS_PATH is used by execlp when PATH is null
        # PATH is null when execlp is called from a binary
        # that is setuid
        self.log_dir('patch', self.extract_dir, 'patch _CS_PATH')
        filename = os.path.join(self.extract_dir, 'sysdeps/unix/confstr.h')
        src = '"/bin:/usr/bin"'
        dst = '"%s/bin:%s/texlive/bin:%s/java/bin:/bin:/usr/bin"' % (self.prefix_dir, self.prefix_dir, self.prefix_dir)
        patch(filename, src, dst)



    def post_install(self):
        # test that we can compile an exe and that it
        # contains the correct dynamic linker
        dir = self.environment['TMPDIR']
        filename = os.path.join(dir, 'dummy.c')
        with open(filename, 'wt') as f:
            f.write('#include <stdio.h>\nint main(){}')

        args = ['%s/bin/%s-gcc' % (self.cross_prefix_dir,
                                   self.target_triplet),
                'dummy.c']
        self.log_dir('test', dir, 'creating test exe')
        self.run_exe(args, dir, self.environment)

        args = ['./a.out']
        self.log_dir('test', dir, 'running test exe')
        self.run_exe(args, dir, self.environment)

        args = ['readelf', '-a', 'a.out']
        self.log_dir('test', dir, 'searching for dynamic linker')
        text = run_or_error(args, dir, self.environment)

        linker = os.path.join(self.cross_prefix_dir,
                              self.target_triplet,
                              'lib64',
                              'ld-linux-x86-64.so.2')

        if linker not in text:
            for line in text.split():
                self.log_verbose(line)
            raise Exception('Could not find linker %s in readelf -a a.out'
                            % (linker))

        self.symlink_crts()
