from .base import GnuRecipe


class LibDsmRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(LibDsmRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '986696078f240086808191d7d739f2e4' \
                      'd3cc1af6695493d3845c58299feb7b38'

        self.description = 'Small portable C SMB client library'
        self.name = 'libdsm'
        self.depends = ['autotools', 'libtasn1']
        self.version = '0.2.8'
        self.version_regex = r'(?P<version>\d+\.\d+\.\d+)'
        self.version_url = 'https://github.com/videolabs/libdsm/releases'
        self.depends = ['autotools', 'pcre', 'pkgconfig', 'xz', 'zlib']
        self.url = 'https://github.com/videolabs/libdsm/releases/download/' \
                   'v$version/libdsm-$version.tar.gz'


    def install(self):
        super(LibDsmRecipe, self).install()

        example = r'''
#include <arpa/inet.h>
#include <stdio.h>

#include <bsdm/bdsm.h>

int main()
{
  struct in_addr  addr;
  smb_session   *session;
  smb_tid     tid;
  smb_fd      fd;

  session = smb_session_new();
  if (session == NULL)
    exit(1);

  inet_aton("127.0.0.1", &addr.sin_addr);

  if (smb_session_connect(session, "MYNAME",
      addr.sin_addr.s_addr, SMB_TRANSPORT_TCP))
  {
    printf("Unable to connect to host\n");
    exit(2);
  }

  smb_session_set_creds(session, "MYNAME", "login",
              "password");
  if (smb_session_login(session))
  {
    if (session->guest)
      printf("Logged in as GUEST \n");
    else
      printf("Successfully logged in\n");
  }
  else
  {
    printf("Auth failed\n");
    exit(3);
  }

  tid = smb_tree_connect(session, "MyShare");
  if (!tid)
  {
    printf("Unable to connect to share\n");
    exit(4);
  }

  fd = smb_fopen(session, tid, "\\My\\File");
  if (!fd)
  {
    printf("Unable to open file\n");
    exit(5);
  }

  char buffer[512];
  smb_fread(session, fd, buffer, 512);

  /* Use data */

  smb_fclose(session, fd);
  smb_tree_disconnect(session, tid);
  smb_session_destroy(session);

  return(0);
}
'''
