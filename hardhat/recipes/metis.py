import os
from .base import GnuRecipe
from ..util import patch


class MetisRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(MetisRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '76faebe03f6c963127dbb73c13eab58c' \
                      '9a3faeae48779f049066a21c087c5db2'
        self.name = 'metis'
        self.version = '5.1.0'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.depends = ['cmake']
        self.url = 'http://glaros.dtc.umn.edu/gkhome/fetch/sw/metis/' \
                   'metis-$version.tar.gz'
        self.configure_args = [
            'cmake',
            '-G',
            '"Unix Makefiles"',
            '-DCMAKE_BUILD_TYPE=Release',
            '-DCMAKE_INSTALL_PREFIX=%s' % self.prefix_dir,
            ]

    def patch(self):
        self.log_dir('patch', self.directory,
                     'have thread local storage')
        src = '''# Custom check for TLS.
if(MSVC)
   set(GKlib_COPTIONS "${GKlib_COPTIONS} -D__thread=__declspec(thread)")
else()
  # This if checks if that value is cached or not.
  if("${HAVE_THREADLOCALSTORAGE}" MATCHES "^${HAVE_THREADLOCALSTORAGE}$")
    try_compile(HAVE_THREADLOCALSTORAGE
      ${CMAKE_BINARY_DIR}
      ${GKLIB_PATH}/conf/check_thread_storage.c)
    if(HAVE_THREADLOCALSTORAGE)
      message(STATUS "checking for thread-local storage - found")
    else()
      message(STATUS "checking for thread-local storage - not found")
    endif()
  endif()
  if(NOT HAVE_THREADLOCALSTORAGE)
    set(GKlib_COPTIONS "${GKlib_COPTIONS} -D__thread=")
  endif()
endif()'''

        dst = ''
        filename = os.path.join(self.directory, 'GKlib/GKlibSystem.cmake')
        patch(filename, src, dst)

        self.log_dir('patch', self.directory, 'index sizes')

        src = '#define IDXTYPEWIDTH 32'
        dst = '#define IDXTYPEWIDTH 64'
        filename = os.path.join(self.directory, 'include', 'metis.h')
        patch(filename, src, dst)

        src = '#define REALTYPEWIDTH 32'
        dst = '#define REALTYPEWIDTH 64'
        filename = os.path.join(self.directory, 'include', 'metis.h')
        patch(filename, src, dst)

    def install(self):
        super(MetisRecipe, self).install()

        self.log_dir('install',
                     self.directory,
                     'building shared library')
        self.configure_args += ['-DSHARED=yes']
        super(MetisRecipe, self).configure()
        super(MetisRecipe, self).compile()
        super(MetisRecipe, self).install()
