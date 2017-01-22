import os
from .base import GnuRecipe
from hardhat.util import patch


class CdParanoiaRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CdParanoiaRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '005db45ef4ee017f5c32ec124f913a05' \
                      '46e77014266c6a1c50df902a55fe64df'
        self.name = 'cdparanoia'
        self.version = '10.2'
        self.url = 'http://downloads.xiph.org/releases/cdparanoia/' \
                   'cdparanoia-III-$version.src.tgz'
#        self.environment['CFLAGS'] += ' -std=gnu99'
        self.configure_strip_cross_compile()
        self.environment_strip_lto()
        self.environment['CFLAGS'] = '-O0 -Wno-pointer-sign -Wno-unused -fPIC'
        self.environment['CXXFLAGS'] = '-O0 -Wno-pointer-sign -Wno-unused -fPIC'

    def patch(self):
        src = r"""(exit $ac_status); } &&
	 { ac_try='test -z "$ac_c_werror_flag"
			 || test ! -s conftest.err'
  { (eval echo "$as_me:$LINENO: \"$ac_try\"") >&5
  (eval $ac_try) 2>&5
  ac_status=$?
  echo "$as_me:$LINENO: \$? = $ac_status" >&5
  (exit $ac_status); }; } &&
	 { ac_try='test -s conftest.$ac_objext'
  { (eval echo "$as_me:$LINENO: \"$ac_try\"") >&5
  (eval $ac_try) 2>&5
  ac_status=$?
  echo "$as_me:$LINENO: \$? = $ac_status" >&5
  (exit $ac_status); }; };"""

        dst = "  (exit $ac_status); }; "

        filename = os.path.join(self.directory, 'configure')
        patch(filename, src, dst)
