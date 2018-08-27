from .base import GnuRecipe


class CoreutilsRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(CoreutilsRecipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e831b3a86091496cdba720411f9748de' \
                      '81507798f6130adeaef872d206e1b057'

        self.name = 'coreutils'
        self.version = '8.30'
        self.depends = ['autoconf', 'automake', 'bison']
        self.url = 'http://ftpmirror.gnu.org/coreutils/' \
                   'coreutils-$version.tar.xz'

        self.configure_strip_cross_compile()
        self.configure_args = [['autoreconf', '-fiv'],
                               self.configure_args + ['--disable-silent-rules',
                               '--enable-no-install-program=kill,uptime']]


    def patch(self):
        text = r'''
Submitted by:            DJ Lucas (dj_AT_linuxfromscratch_DOT_org)
Date:                    2016-12-03
Initial Package Version: 8.26
Upstream Status:         Rejected
Origin:                  Based on Suse's i18n patches at
                         https://build.opensuse.org/package/show/Base:System/coreutils/
Description:             Fixes i18n issues with various Coreutils programs

diff -Naurp coreutils-8.26-orig/bootstrap.conf coreutils-8.26/bootstrap.conf
--- coreutils-8.26-orig/bootstrap.conf	2016-11-06 16:15:29.000000000 -0600
+++ coreutils-8.26/bootstrap.conf	2016-12-02 19:15:23.514391986 -0600
@@ -152,6 +152,7 @@ gnulib_modules="
   maintainer-makefile
   malloc-gnu
   manywarnings
+  mbfile
   mbrlen
   mbrtowc
   mbsalign
diff -Naurp coreutils-8.26-orig/configure.ac coreutils-8.26/configure.ac
--- coreutils-8.26-orig/configure.ac	2016-11-29 12:03:45.000000000 -0600
+++ coreutils-8.26/configure.ac	2016-12-02 19:15:23.515391902 -0600
@@ -427,6 +427,8 @@ fi
 # I'm leaving it here for now.  This whole thing needs to be modernized...
 gl_WINSIZE_IN_PTEM

+gl_MBFILE
+
 gl_HEADER_TIOCGWINSZ_IN_TERMIOS_H

 if test $gl_cv_sys_tiocgwinsz_needs_termios_h = no && \
diff -Naurp coreutils-8.26-orig/lib/linebuffer.h coreutils-8.26/lib/linebuffer.h
--- coreutils-8.26-orig/lib/linebuffer.h	2016-07-15 14:47:39.000000000 -0500
+++ coreutils-8.26/lib/linebuffer.h	2016-12-02 19:15:23.515391902 -0600
@@ -21,6 +21,11 @@

 # include <stdio.h>

+/* Get mbstate_t.  */
+# if HAVE_WCHAR_H
+#  include <wchar.h>
+# endif
+
 /* A 'struct linebuffer' holds a line of text. */

 struct linebuffer
@@ -28,6 +33,9 @@ struct linebuffer
   size_t size;                  /* Allocated. */
   size_t length;                /* Used. */
   char *buffer;
+# if HAVE_WCHAR_H
+  mbstate_t state;
+# endif
 };

 /* Initialize linebuffer LINEBUFFER for use. */
diff -Naurp coreutils-8.26-orig/lib/mbfile.c coreutils-8.26/lib/mbfile.c
--- coreutils-8.26-orig/lib/mbfile.c	1969-12-31 18:00:00.000000000 -0600
+++ coreutils-8.26/lib/mbfile.c	2016-12-02 19:15:23.515391902 -0600
@@ -0,0 +1,3 @@
+#include <config.h>
+#define MBFILE_INLINE _GL_EXTERN_INLINE
+#include "mbfile.h"
diff -Naurp coreutils-8.26-orig/lib/mbfile.h coreutils-8.26/lib/mbfile.h
--- coreutils-8.26-orig/lib/mbfile.h	1969-12-31 18:00:00.000000000 -0600
+++ coreutils-8.26/lib/mbfile.h	2016-12-02 19:15:23.516391818 -0600
@@ -0,0 +1,255 @@
+/* Multibyte character I/O: macros for multi-byte encodings.
+   Copyright (C) 2001, 2005, 2009-2015 Free Software Foundation, Inc.
+
+   This program is free software: you can redistribute it and/or modify
+   it under the terms of the GNU General Public License as published by
+   the Free Software Foundation; either version 3 of the License, or
+   (at your option) any later version.
+
+   This program is distributed in the hope that it will be useful,
+   but WITHOUT ANY WARRANTY; without even the implied warranty of
+   MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
+   GNU General Public License for more details.
+
+   You should have received a copy of the GNU General Public License
+   along with this program.  If not, see <http://www.gnu.org/licenses/>.  */
+
+/* Written by Mitsuru Chinen <mchinen@yamato.ibm.com>
+   and Bruno Haible <bruno@clisp.org>.  */
+
+/* The macros in this file implement multi-byte character input from a
+   stream.
+
+   mb_file_t
+     is the type for multibyte character input stream, usable for variable
+     declarations.
+
+   mbf_char_t
+     is the type for multibyte character or EOF, usable for variable
+     declarations.
+
+   mbf_init (mbf, stream)
+     initializes the MB_FILE for reading from stream.
+
+   mbf_getc (mbc, mbf)
+     reads the next multibyte character from mbf and stores it in mbc.
+
+   mb_iseof (mbc)
+     returns true if mbc represents the EOF value.
+
+   Here are the function prototypes of the macros.
+
+   extern void          mbf_init (mb_file_t mbf, FILE *stream);
+   extern void          mbf_getc (mbf_char_t mbc, mb_file_t mbf);
+   extern bool          mb_iseof (const mbf_char_t mbc);
+ */
+
+#ifndef _MBFILE_H
+#define _MBFILE_H 1
+
+#include <assert.h>
+#include <stdbool.h>
+#include <stdio.h>
+#include <string.h>
+
+/* Tru64 with Desktop Toolkit C has a bug: <stdio.h> must be included before
+   <wchar.h>.
+   BSD/OS 4.1 has a bug: <stdio.h> and <time.h> must be included before
+   <wchar.h>.  */
+#include <stdio.h>
+#include <time.h>
+#include <wchar.h>
+
+#include "mbchar.h"
+
+#ifndef _GL_INLINE_HEADER_BEGIN
+ #error "Please include config.h first."
+#endif
+_GL_INLINE_HEADER_BEGIN
+#ifndef MBFILE_INLINE
+# define MBFILE_INLINE _GL_INLINE
+#endif
+
+struct mbfile_multi {
+  FILE *fp;
+  bool eof_seen;
+  bool have_pushback;
+  mbstate_t state;
+  unsigned int bufcount;
+  char buf[MBCHAR_BUF_SIZE];
+  struct mbchar pushback;
+};
+
+MBFILE_INLINE void
+mbfile_multi_getc (struct mbchar *mbc, struct mbfile_multi *mbf)
+{
+  size_t bytes;
+
+  /* If EOF has already been seen, don't use getc.  This matters if
+     mbf->fp is connected to an interactive tty.  */
+  if (mbf->eof_seen)
+    goto eof;
+
+  /* Return character pushed back, if there is one.  */
+  if (mbf->have_pushback)
+    {
+      mb_copy (mbc, &mbf->pushback);
+      mbf->have_pushback = false;
+      return;
+    }
+
+  /* Before using mbrtowc, we need at least one byte.  */
+  if (mbf->bufcount == 0)
+    {
+      int c = getc (mbf->fp);
+      if (c == EOF)
+        {
+          mbf->eof_seen = true;
+          goto eof;
+        }
+      mbf->buf[0] = (unsigned char) c;
+      mbf->bufcount++;
+    }
+
+  /* Handle most ASCII characters quickly, without calling mbrtowc().  */
+  if (mbf->bufcount == 1 && mbsinit (&mbf->state) && is_basic (mbf->buf[0]))
+    {
+      /* These characters are part of the basic character set.  ISO C 99
+         guarantees that their wide character code is identical to their
+         char code.  */
+      mbc->wc = mbc->buf[0] = mbf->buf[0];
+      mbc->wc_valid = true;
+      mbc->ptr = &mbc->buf[0];
+      mbc->bytes = 1;
+      mbf->bufcount = 0;
+      return;
+    }
+
+  /* Use mbrtowc on an increasing number of bytes.  Read only as many bytes
+     from mbf->fp as needed.  This is needed to give reasonable interactive
+     behaviour when mbf->fp is connected to an interactive tty.  */
+  for (;;)
+    {
+      /* We don't know whether the 'mbrtowc' function updates the state when
+         it returns -2, - this is the ISO C 99 and glibc-2.2 behaviour - or
+         not - amended ANSI C, glibc-2.1 and Solaris 2.7 behaviour.  We
+         don't have an autoconf test for this, yet.
+         The new behaviour would allow us to feed the bytes one by one into
+         mbrtowc.  But the old behaviour forces us to feed all bytes since
+         the end of the last character into mbrtowc.  Since we want to retry
+         with more bytes when mbrtowc returns -2, we must backup the state
+         before calling mbrtowc, because implementations with the new
+         behaviour will clobber it.  */
+      mbstate_t backup_state = mbf->state;
+
+      bytes = mbrtowc (&mbc->wc, &mbf->buf[0], mbf->bufcount, &mbf->state);
+
+      if (bytes == (size_t) -1)
+        {
+          /* An invalid multibyte sequence was encountered.  */
+          /* Return a single byte.  */
+          bytes = 1;
+          mbc->wc_valid = false;
+          break;
+        }
+      else if (bytes == (size_t) -2)
+        {
+          /* An incomplete multibyte character.  */
+          mbf->state = backup_state;
+          if (mbf->bufcount == MBCHAR_BUF_SIZE)
+            {
+              /* An overlong incomplete multibyte sequence was encountered.  */
+              /* Return a single byte.  */
+              bytes = 1;
+              mbc->wc_valid = false;
+              break;
+            }
+          else
+            {
+              /* Read one more byte and retry mbrtowc.  */
+              int c = getc (mbf->fp);
+              if (c == EOF)
+                {
+                  /* An incomplete multibyte character at the end.  */
+                  mbf->eof_seen = true;
+                  bytes = mbf->bufcount;
+                  mbc->wc_valid = false;
+                  break;
+                }
+              mbf->buf[mbf->bufcount] = (unsigned char) c;
+              mbf->bufcount++;
+            }
+        }
+      else
+        {
+          if (bytes == 0)
+            {
+              /* A null wide character was encountered.  */
+              bytes = 1;
+              assert (mbf->buf[0] == '\0');
+              assert (mbc->wc == 0);
+            }
+          mbc->wc_valid = true;
+          break;
+        }
+    }
+
+  /* Return the multibyte sequence mbf->buf[0..bytes-1].  */
+  mbc->ptr = &mbc->buf[0];
+  memcpy (&mbc->buf[0], &mbf->buf[0], bytes);
+  mbc->bytes = bytes;
+
+  mbf->bufcount -= bytes;
+  if (mbf->bufcount > 0)
+    {
+      /* It's not worth calling memmove() for so few bytes.  */
+      unsigned int count = mbf->bufcount;
+      char *p = &mbf->buf[0];
+
+      do
+        {
+          *p = *(p + bytes);
+          p++;
+        }
+      while (--count > 0);
+    }
+  return;
+
+eof:
+  /* An mbchar_t with bytes == 0 is used to indicate EOF.  */
+  mbc->ptr = NULL;
+  mbc->bytes = 0;
+  mbc->wc_valid = false;
+  return;
+}
+
+MBFILE_INLINE void
+mbfile_multi_ungetc (const struct mbchar *mbc, struct mbfile_multi *mbf)
+{
+  mb_copy (&mbf->pushback, mbc);
+  mbf->have_pushback = true;
+}
+
+typedef struct mbfile_multi mb_file_t;
+
+typedef mbchar_t mbf_char_t;
+
+#define mbf_init(mbf, stream)                                           \
+  ((mbf).fp = (stream),                                                 \
+   (mbf).eof_seen = false,                                              \
+   (mbf).have_pushback = false,                                         \
+   memset (&(mbf).state, '\0', sizeof (mbstate_t)),                     \
+   (mbf).bufcount = 0)
+
+#define mbf_getc(mbc, mbf) mbfile_multi_getc (&(mbc), &(mbf))
+
+#define mbf_ungetc(mbc, mbf) mbfile_multi_ungetc (&(mbc), &(mbf))
+
+#define mb_iseof(mbc) ((mbc).bytes == 0)
+
+#ifndef _GL_INLINE_HEADER_BEGIN
+ #error "Please include config.h first."
+#endif
+_GL_INLINE_HEADER_BEGIN
+
+#endif /* _MBFILE_H */
diff -Naurp coreutils-8.26-orig/m4/mbfile.m4 coreutils-8.26/m4/mbfile.m4
--- coreutils-8.26-orig/m4/mbfile.m4	1969-12-31 18:00:00.000000000 -0600
+++ coreutils-8.26/m4/mbfile.m4	2016-12-02 19:15:23.516391818 -0600
@@ -0,0 +1,14 @@
+# mbfile.m4 serial 7
+dnl Copyright (C) 2005, 2008-2015 Free Software Foundation, Inc.
+dnl This file is free software; the Free Software Foundation
+dnl gives unlimited permission to copy and/or distribute it,
+dnl with or without modifications, as long as this notice is preserved.
+
+dnl autoconf tests required for use of mbfile.h
+dnl From Bruno Haible.
+
+AC_DEFUN([gl_MBFILE],
+[
+  AC_REQUIRE([AC_TYPE_MBSTATE_T])
+  :
+])
diff -Naurp coreutils-8.26-orig/src/cut.c coreutils-8.26/src/cut.c
--- coreutils-8.26-orig/src/cut.c	2016-10-15 16:00:55.000000000 -0500
+++ coreutils-8.26/src/cut.c	2016-12-02 19:15:23.517391733 -0600
@@ -28,6 +28,11 @@
 #include <assert.h>
 #include <getopt.h>
 #include <sys/types.h>
+
+/* Get mbstate_t, mbrtowc().  */
+#if HAVE_WCHAR_H
+# include <wchar.h>
+#endif
 #include "system.h"

 #include "error.h"
@@ -38,6 +43,18 @@

 #include "set-fields.h"

+/* MB_LEN_MAX is incorrectly defined to be 1 in at least one GCC
+   installation; work around this configuration error.        */
+#if !defined MB_LEN_MAX || MB_LEN_MAX < 2
+# undef MB_LEN_MAX
+# define MB_LEN_MAX 16
+#endif
+
+/* Some systems, like BeOS, have multibyte encodings but lack mbstate_t.  */
+#if HAVE_MBRTOWC && defined mbstate_t
+# define mbrtowc(pwc, s, n, ps) (mbrtowc) (pwc, s, n, 0)
+#endif
+
 /* The official name of this program (e.g., no 'g' prefix).  */
 #define PROGRAM_NAME "cut"

@@ -54,6 +71,52 @@
     }									\
   while (0)

+/* Refill the buffer BUF to get a multibyte character. */
+#define REFILL_BUFFER(BUF, BUFPOS, BUFLEN, STREAM)                        \
+  do                                                                        \
+    {                                                                        \
+      if (BUFLEN < MB_LEN_MAX && !feof (STREAM) && !ferror (STREAM))        \
+        {                                                                \
+          memmove (BUF, BUFPOS, BUFLEN);                                \
+          BUFLEN += fread (BUF + BUFLEN, sizeof(char), BUFSIZ, STREAM); \
+          BUFPOS = BUF;                                                        \
+        }                                                                \
+    }                                                                        \
+  while (0)
+
+/* Get wide character on BUFPOS. BUFPOS is not included after that.
+   If byte sequence is not valid as a character, CONVFAIL is true. Otherwise false. */
+#define GET_NEXT_WC_FROM_BUFFER(WC, BUFPOS, BUFLEN, MBLENGTH, STATE, CONVFAIL) \
+  do                                                                        \
+    {                                                                        \
+      mbstate_t state_bak;                                                \
+                                                                        \
+      if (BUFLEN < 1)                                                        \
+        {                                                                \
+          WC = WEOF;                                                        \
+          break;                                                        \
+        }                                                                \
+                                                                        \
+      /* Get a wide character. */                                        \
+      CONVFAIL = false;                                                        \
+      state_bak = STATE;                                                \
+      MBLENGTH = mbrtowc ((wchar_t *)&WC, BUFPOS, BUFLEN, &STATE);        \
+                                                                        \
+      switch (MBLENGTH)                                                        \
+        {                                                                \
+        case (size_t)-1:                                                \
+        case (size_t)-2:                                                \
+          CONVFAIL = true;                                                        \
+          STATE = state_bak;                                                \
+          /* Fall througn. */                                                \
+                                                                        \
+        case 0:                                                                \
+          MBLENGTH = 1;                                                        \
+          break;                                                        \
+        }                                                                \
+    }                                                                        \
+  while (0)
+

 /* Pointer inside RP.  When checking if a byte or field is selected
    by a finite range, we check if it is between CURRENT_RP.LO
@@ -61,6 +124,9 @@
    CURRENT_RP.HI then we make CURRENT_RP to point to the next range pair. */
 static struct field_range_pair *current_rp;

+/* Length of the delimiter given as argument to -d.  */
+size_t delimlen;
+
 /* This buffer is used to support the semantics of the -s option
    (or lack of same) when the specified field list includes (does
    not include) the first field.  In both of those cases, the entire
@@ -77,15 +143,25 @@ enum operating_mode
   {
     undefined_mode,

-    /* Output characters that are in the given bytes. */
+    /* Output bytes that are at the given positions. */
     byte_mode,

+    /* Output characters that are at the given positions. */
+    character_mode,
+
     /* Output the given delimiter-separated fields. */
     field_mode
   };

 static enum operating_mode operating_mode;

+/* If nonzero, when in byte mode, don't split multibyte characters.  */
+static int byte_mode_character_aware;
+
+/* If nonzero, the function for single byte locale is work
+   if this program runs on multibyte locale. */
+static int force_singlebyte_mode;
+
 /* If true do not output lines containing no delimiter characters.
    Otherwise, all such lines are printed.  This option is valid only
    with field mode.  */
@@ -97,6 +173,9 @@ static bool complement;

 /* The delimiter character for field mode. */
 static unsigned char delim;
+#if HAVE_WCHAR_H
+static wchar_t wcdelim;
+#endif

 /* The delimiter for each line/record. */
 static unsigned char line_delim = '\n';
@@ -164,7 +243,7 @@ Print selected parts of lines from each
   -f, --fields=LIST       select only these fields;  also print any line\n\
                             that contains no delimiter character, unless\n\
                             the -s option is specified\n\
-  -n                      (ignored)\n\
+  -n                      with -b: don't split multibyte characters\n\
 "), stdout);
       fputs (_("\
       --complement        complement the set of selected bytes, characters\n\
@@ -280,6 +359,82 @@ cut_bytes (FILE *stream)
     }
 }

+#if HAVE_MBRTOWC
+/* This function is in use for the following case.
+
+   1. Read from the stream STREAM, printing to standard output any selected
+   characters.
+
+   2. Read from stream STREAM, printing to standard output any selected bytes,
+   without splitting multibyte characters.  */
+
+static void
+cut_characters_or_cut_bytes_no_split (FILE *stream)
+{
+  size_t idx;                /* number of bytes or characters in the line so far. */
+  char buf[MB_LEN_MAX + BUFSIZ];  /* For spooling a read byte sequence. */
+  char *bufpos;                /* Next read position of BUF. */
+  size_t buflen;        /* The length of the byte sequence in buf. */
+  wint_t wc;                /* A gotten wide character. */
+  size_t mblength;        /* The byte size of a multibyte character which shows
+                           as same character as WC. */
+  mbstate_t state;        /* State of the stream. */
+  bool convfail = false;  /* true, when conversion failed. Otherwise false. */
+  /* Whether to begin printing delimiters between ranges for the current line.
+     Set after we've begun printing data corresponding to the first range.  */
+  bool print_delimiter = false;
+
+  idx = 0;
+  buflen = 0;
+  bufpos = buf;
+  memset (&state, '\0', sizeof(mbstate_t));
+
+  current_rp = frp;
+
+  while (1)
+    {
+      REFILL_BUFFER (buf, bufpos, buflen, stream);
+
+      GET_NEXT_WC_FROM_BUFFER (wc, bufpos, buflen, mblength, state, convfail);
+      (void) convfail;  /* ignore unused */
+
+      if (wc == WEOF)
+        {
+          if (idx > 0)
+            putchar (line_delim);
+          break;
+        }
+      else if (wc == line_delim)
+        {
+          putchar (line_delim);
+          idx = 0;
+          print_delimiter = false;
+          current_rp = frp;
+        }
+      else
+        {
+          next_item (&idx);
+          if (print_kth (idx))
+            {
+              if (output_delimiter_specified)
+                {
+                  if (print_delimiter && is_range_start_index (idx))
+                    {
+                      fwrite (output_delimiter_string, sizeof (char),
+                              output_delimiter_length, stdout);
+                    }
+                  print_delimiter = true;
+                }
+              fwrite (bufpos, mblength, sizeof(char), stdout);
+            }
+        }
+
+      buflen -= mblength;
+      bufpos += mblength;
+    }
+}
+#endif
+
 /* Read from stream STREAM, printing to standard output any selected fields.  */

 static void
@@ -425,13 +580,211 @@ cut_fields (FILE *stream)
     }
 }

+#if HAVE_MBRTOWC
+static void
+cut_fields_mb (FILE *stream)
+{
+  int c;
+  size_t field_idx;
+  int found_any_selected_field;
+  int buffer_first_field;
+  int empty_input;
+  char buf[MB_LEN_MAX + BUFSIZ];  /* For spooling a read byte sequence. */
+  char *bufpos;                /* Next read position of BUF. */
+  size_t buflen;        /* The length of the byte sequence in buf. */
+  wint_t wc = 0;        /* A gotten wide character. */
+  size_t mblength;        /* The byte size of a multibyte character which shows
+                           as same character as WC. */
+  mbstate_t state;        /* State of the stream. */
+  bool convfail = false;  /* true, when conversion failed. Otherwise false. */
+
+  current_rp = frp;
+
+  found_any_selected_field = 0;
+  field_idx = 1;
+  bufpos = buf;
+  buflen = 0;
+  memset (&state, '\0', sizeof(mbstate_t));
+
+  c = getc (stream);
+  empty_input = (c == EOF);
+  if (c != EOF)
+  {
+    ungetc (c, stream);
+    wc = 0;
+  }
+  else
+    wc = WEOF;
+
+  /* To support the semantics of the -s flag, we may have to buffer
+     all of the first field to determine whether it is `delimited.'
+     But that is unnecessary if all non-delimited lines must be printed
+     and the first field has been selected, or if non-delimited lines
+     must be suppressed and the first field has *not* been selected.
+     That is because a non-delimited line has exactly one field.  */
+  buffer_first_field = (suppress_non_delimited ^ !print_kth (1));
+
+  while (1)
+    {
+      if (field_idx == 1 && buffer_first_field)
+        {
+          int len = 0;
+
+          while (1)
+            {
+              REFILL_BUFFER (buf, bufpos, buflen, stream);
+
+              GET_NEXT_WC_FROM_BUFFER
+                (wc, bufpos, buflen, mblength, state, convfail);
+
+              if (wc == WEOF)
+                break;
+
+              field_1_buffer = xrealloc (field_1_buffer, len + mblength);
+              memcpy (field_1_buffer + len, bufpos, mblength);
+              len += mblength;
+              buflen -= mblength;
+              bufpos += mblength;
+
+              if (!convfail && (wc == line_delim || wc == wcdelim))
+                break;
+            }
+
+          if (len <= 0 && wc == WEOF)
+            break;
+
+          /* If the first field extends to the end of line (it is not
+             delimited) and we are printing all non-delimited lines,
+             print this one.  */
+          if (convfail || (!convfail && wc != wcdelim))
+            {
+              if (suppress_non_delimited)
+                {
+                  /* Empty.        */
+                }
+              else
+                {
+                  fwrite (field_1_buffer, sizeof (char), len, stdout);
+                  /* Make sure the output line is newline terminated.  */
+                  if (convfail || (!convfail && wc != line_delim))
+                    putchar (line_delim);
+                }
+              continue;
+            }
+
+          if (print_kth (1))
+            {
+              /* Print the field, but not the trailing delimiter.  */
+              fwrite (field_1_buffer, sizeof (char), len - 1, stdout);
+              found_any_selected_field = 1;
+            }
+          next_item (&field_idx);
+        }
+
+      if (wc != WEOF)
+        {
+          if (print_kth (field_idx))
+            {
+              if (found_any_selected_field)
+                {
+                  fwrite (output_delimiter_string, sizeof (char),
+                          output_delimiter_length, stdout);
+                }
+              found_any_selected_field = 1;
+            }
+
+          while (1)
+            {
+              REFILL_BUFFER (buf, bufpos, buflen, stream);
+
+              GET_NEXT_WC_FROM_BUFFER
+                (wc, bufpos, buflen, mblength, state, convfail);
+
+              if (wc == WEOF)
+                break;
+              else if (!convfail && (wc == wcdelim || wc == line_delim))
+                {
+                  buflen -= mblength;
+                  bufpos += mblength;
+                  break;
+                }
+
+              if (print_kth (field_idx))
+                fwrite (bufpos, mblength, sizeof(char), stdout);
+
+              buflen -= mblength;
+              bufpos += mblength;
+            }
+        }
+
+      if ((!convfail || wc == line_delim) && buflen < 1)
+        wc = WEOF;
+
+      if (!convfail && wc == wcdelim)
+        next_item (&field_idx);
+      else if (wc == WEOF || (!convfail && wc == line_delim))
+        {
+          if (found_any_selected_field
+              || (!empty_input && !(suppress_non_delimited && field_idx == 1)))
+            putchar (line_delim);
+          if (wc == WEOF)
+            break;
+          field_idx = 1;
+          current_rp = frp;
+          found_any_selected_field = 0;
+        }
+    }
+}
+#endif
+
 static void
 cut_stream (FILE *stream)
 {
-  if (operating_mode == byte_mode)
-    cut_bytes (stream);
+#if HAVE_MBRTOWC
+  if (MB_CUR_MAX > 1 && !force_singlebyte_mode)
+    {
+      switch (operating_mode)
+        {
+        case byte_mode:
+          if (byte_mode_character_aware)
+            cut_characters_or_cut_bytes_no_split (stream);
+          else
+            cut_bytes (stream);
+          break;
+
+        case character_mode:
+          cut_characters_or_cut_bytes_no_split (stream);
+          break;
+
+        case field_mode:
+          if (delimlen == 1)
+            {
+              /* Check if we have utf8 multibyte locale, so we can use this
+                 optimization because of uniqueness of characters, which is
+                 not true for e.g. SJIS */
+              char * loc = setlocale(LC_CTYPE, NULL);
+              if (loc && (strstr (loc, "UTF-8") || strstr (loc, "utf-8") ||
+                  strstr (loc, "UTF8") || strstr (loc, "utf8")))
+                {
+                  cut_fields (stream);
+                  break;
+                }
+            }
+          cut_fields_mb (stream);
+          break;
+
+        default:
+          abort ();
+        }
+    }
   else
-    cut_fields (stream);
+#endif
+    {
+      if (operating_mode == field_mode)
+        cut_fields (stream);
+      else
+        cut_bytes (stream);
+    }
 }

 /* Process file FILE to standard output.
@@ -483,6 +836,7 @@ main (int argc, char **argv)
   bool ok;
   bool delim_specified = false;
   char *spec_list_string IF_LINT ( = NULL);
+  char mbdelim[MB_LEN_MAX + 1];

   initialize_main (&argc, &argv);
   set_program_name (argv[0]);
@@ -505,7 +859,6 @@ main (int argc, char **argv)
       switch (optc)
         {
         case 'b':
-        case 'c':
           /* Build the byte list. */
           if (operating_mode != undefined_mode)
             FATAL_ERROR (_("only one type of list may be specified"));
@@ -513,6 +866,14 @@ main (int argc, char **argv)
           spec_list_string = optarg;
           break;

+        case 'c':
+          /* Build the character list. */
+          if (operating_mode != undefined_mode)
+            FATAL_ERROR (_("only one type of list may be specified"));
+          operating_mode = character_mode;
+          spec_list_string = optarg;
+          break;
+
         case 'f':
           /* Build the field list. */
           if (operating_mode != undefined_mode)
@@ -524,10 +885,38 @@ main (int argc, char **argv)
         case 'd':
           /* New delimiter. */
           /* Interpret -d '' to mean 'use the NUL byte as the delimiter.'  */
-          if (optarg[0] != '\0' && optarg[1] != '\0')
-            FATAL_ERROR (_("the delimiter must be a single character"));
-          delim = optarg[0];
-          delim_specified = true;
+            {
+#if HAVE_MBRTOWC
+              if(MB_CUR_MAX > 1)
+                {
+                  mbstate_t state;
+
+                  memset (&state, '\0', sizeof(mbstate_t));
+                  delimlen = mbrtowc (&wcdelim, optarg, strnlen(optarg, MB_LEN_MAX), &state);
+
+                  if (delimlen == (size_t)-1 || delimlen == (size_t)-2)
+                    ++force_singlebyte_mode;
+                  else
+                    {
+                      delimlen = (delimlen < 1) ? 1 : delimlen;
+                      if (wcdelim != L'\0' && *(optarg + delimlen) != '\0')
+                        FATAL_ERROR (_("the delimiter must be a single character"));
+                      memcpy (mbdelim, optarg, delimlen);
+                      mbdelim[delimlen] = '\0';
+                      if (delimlen == 1)
+                        delim = *optarg;
+                    }
+                }
+
+              if (MB_CUR_MAX <= 1 || force_singlebyte_mode)
+#endif
+                {
+                  if (optarg[0] != '\0' && optarg[1] != '\0')
+                    FATAL_ERROR (_("the delimiter must be a single character"));
+                  delim = (unsigned char) optarg[0];
+                }
+            delim_specified = true;
+          }
           break;

         case OUTPUT_DELIMITER_OPTION:
@@ -540,6 +929,7 @@ main (int argc, char **argv)
           break;

         case 'n':
+          byte_mode_character_aware = 1;
           break;

         case 's':
@@ -579,15 +969,34 @@ main (int argc, char **argv)
               | (complement ? SETFLD_COMPLEMENT : 0) );

   if (!delim_specified)
-    delim = '\t';
+    {
+      delim = '\t';
+#ifdef HAVE_MBRTOWC
+      wcdelim = L'\t';
+      mbdelim[0] = '\t';
+      mbdelim[1] = '\0';
+      delimlen = 1;
+#endif
+    }

   if (output_delimiter_string == NULL)
     {
-      static char dummy[2];
-      dummy[0] = delim;
-      dummy[1] = '\0';
-      output_delimiter_string = dummy;
-      output_delimiter_length = 1;
+#ifdef HAVE_MBRTOWC
+      if (MB_CUR_MAX > 1 && !force_singlebyte_mode)
+        {
+          output_delimiter_string = xstrdup(mbdelim);
+          output_delimiter_length = delimlen;
+        }
+
+      if (MB_CUR_MAX <= 1 || force_singlebyte_mode)
+#endif
+        {
+          static char dummy[2];
+          dummy[0] = delim;
+          dummy[1] = '\0';
+          output_delimiter_string = dummy;
+          output_delimiter_length = 1;
+        }
     }

   if (optind == argc)
diff -Naurp coreutils-8.26-orig/src/expand.c coreutils-8.26/src/expand.c
--- coreutils-8.26-orig/src/expand.c	2016-11-06 16:15:30.000000000 -0600
+++ coreutils-8.26/src/expand.c	2016-12-02 19:15:23.518391649 -0600
@@ -37,6 +37,9 @@
 #include <stdio.h>
 #include <getopt.h>
 #include <sys/types.h>
+
+#include <mbfile.h>
+
 #include "system.h"
 #include "die.h"
 #include "xstrndup.h"
@@ -100,19 +103,41 @@ expand (void)
 {
   /* Input stream.  */
   FILE *fp = next_file (NULL);
+  mb_file_t mbf;
+  mbf_char_t c;
+  /* True if the starting locale is utf8.  */
+  bool using_utf_locale;
+
+  /* True if the first file contains BOM header.  */
+  bool found_bom;
+  using_utf_locale=check_utf_locale();

   if (!fp)
     return;
+  mbf_init (mbf, fp);
+  found_bom=check_bom(fp,&mbf);

-  while (true)
+  if (using_utf_locale == false && found_bom == true)
+  {
+    /*try using some predefined locale */
+
+    if (set_utf_locale () != 0)
     {
-      /* Input character, or EOF.  */
-      int c;
+      error (EXIT_FAILURE, errno, _("cannot set UTF-8 locale"));
+    }
+  }
+

+  if (found_bom == true)
+  {
+    print_bom();
+  }
+
+  while (true)
+    {
       /* If true, perform translations.  */
       bool convert = true;

-
       /* The following variables have valid values only when CONVERT
          is true:  */

@@ -122,17 +147,48 @@ expand (void)
       /* Index in TAB_LIST of next tab stop to examine.  */
       size_t tab_index = 0;

-
       /* Convert a line of text.  */

       do
         {
-          while ((c = getc (fp)) < 0 && (fp = next_file (fp)))
-            continue;
+          while (true) {
+            mbf_getc (c, mbf);
+            if ((mb_iseof (c)) && (fp = next_file (fp)))
+              {
+                mbf_init (mbf, fp);
+                if (fp!=NULL)
+                {
+                  if (check_bom(fp,&mbf)==true)
+                  {
+                    /*Not the first file - check BOM header*/
+                    if (using_utf_locale==false && found_bom==false)
+                    {
+                      /*BOM header in subsequent file but not in the first one. */
+                      error (EXIT_FAILURE, errno, _("combination of files with and without BOM header"));
+                    }
+                  }
+                  else
+                  {
+                    if(using_utf_locale==false && found_bom==true)
+                    {
+                      /*First file conatined BOM header - locale was switched to UTF
+                      /*all subsequent files should contain BOM. */
+                      error (EXIT_FAILURE, errno, _("combination of files with and without BOM header"));
+                    }
+                  }
+                }
+                continue;
+              }
+            else
+              {
+                break;
+              }
+            }
+

           if (convert)
             {
-              if (c == '\t')
+              if (mb_iseq (c, '\t'))
                 {
                   /* Column the next input tab stop is on.  */
                   uintmax_t next_tab_column;
@@ -151,32 +207,34 @@ expand (void)
                     if (putchar (' ') < 0)
                       die (EXIT_FAILURE, errno, _("write error"));

-                  c = ' ';
+                  mb_setascii (&c, ' ');
                 }
-              else if (c == '\b')
+              else if (mb_iseq (c, '\b'))
                 {
                   /* Go back one column, and force recalculation of the
                      next tab stop.  */
                   column -= !!column;
                   tab_index -= !!tab_index;
                 }
-              else
+              /* A leading control character could make us trip over.  */
+              else if (!mb_iscntrl (c))
                 {
-                  column++;
+                  column += mb_width (c);
                   if (!column)
                     die (EXIT_FAILURE, 0, _("input line is too long"));
                 }

-              convert &= convert_entire_line || !! isblank (c);
+              convert &= convert_entire_line || mb_isblank (c);
             }

-          if (c < 0)
+          if (mb_iseof (c))
             return;

-          if (putchar (c) < 0)
+          mb_putc (c, stdout);
+          if (ferror (stdout))
             die (EXIT_FAILURE, errno, _("write error"));
         }
-      while (c != '\n');
+      while (!mb_iseq (c, '\n'));
     }
 }

diff -Naurp coreutils-8.26-orig/src/expand-common.c coreutils-8.26/src/expand-common.c
--- coreutils-8.26-orig/src/expand-common.c	2016-11-06 16:15:30.000000000 -0600
+++ coreutils-8.26/src/expand-common.c	2016-12-02 19:15:23.518391649 -0600
@@ -18,6 +18,7 @@

 #include <stdio.h>
 #include <sys/types.h>
+#include <mbfile.h>
 #include "system.h"
 #include "die.h"
 #include "error.h"
@@ -85,6 +86,119 @@ add_tab_stop (uintmax_t tabval)
     }
 }

+extern int
+set_utf_locale (void)
+{
+      /*try using some predefined locale */
+      const char* predef_locales[] = {"C.UTF8","en_US.UTF8","en_GB.UTF8"};
+
+      const int predef_locales_count=3;
+      for (int i=0;i<predef_locales_count;i++)
+        {
+          if (setlocale(LC_ALL,predef_locales[i])!=NULL)
+          {
+            break;
+          }
+          else if (i==predef_locales_count-1)
+          {
+            return 1;
+            error (EXIT_FAILURE, errno, _("cannot set UTF-8 locale"));
+          }
+        }
+        return 0;
+}
+
+extern bool
+check_utf_locale(void)
+{
+  char* locale = setlocale (LC_CTYPE , NULL);
+  if (locale == NULL)
+  {
+    return false;
+  }
+  else if (strcasestr(locale, "utf8") == NULL && strcasestr(locale, "utf-8") == NULL)
+  {
+    return false;
+  }
+  return true;
+}
+
+extern bool
+check_bom(FILE* fp, mb_file_t *mbf)
+{
+  int c;
+
+
+  c=fgetc(fp);
+
+  /*test BOM header of the first file */
+  mbf->bufcount=0;
+  if (c == 0xEF)
+  {
+    c=fgetc(fp);
+  }
+  else
+  {
+    if (c != EOF)
+    {
+      ungetc(c,fp);
+    }
+    return false;
+  }
+
+  if (c == 0xBB)
+  {
+    c=fgetc(fp);
+  }
+  else
+  {
+    if ( c!= EOF )
+    {
+      mbf->buf[0]=(unsigned char) 0xEF;
+      mbf->bufcount=1;
+      ungetc(c,fp);
+      return false;
+    }
+    else
+    {
+      ungetc(0xEF,fp);
+      return false;
+    }
+  }
+  if (c == 0xBF)
+  {
+    mbf->bufcount=0;
+    return true;
+  }
+  else
+  {
+    if (c != EOF)
+    {
+      mbf->buf[0]=(unsigned char) 0xEF;
+      mbf->buf[1]=(unsigned char) 0xBB;
+      mbf->bufcount=2;
+      ungetc(c,fp);
+      return false;
+    }
+    else
+    {
+      mbf->buf[0]=(unsigned char) 0xEF;
+      mbf->bufcount=1;
+      ungetc(0xBB,fp);
+      return false;
+    }
+  }
+  return false;
+}
+
+extern void
+print_bom(void)
+{
+  putc (0xEF, stdout);
+  putc (0xBB, stdout);
+  putc (0xBF, stdout);
+}
+
 /* Add the comma or blank separated list of tab stops STOPS
    to the list of tab stops.  */
 extern void
diff -Naurp coreutils-8.26-orig/src/expand-common.h coreutils-8.26/src/expand-common.h
--- coreutils-8.26-orig/src/expand-common.h	2016-11-06 16:15:30.000000000 -0600
+++ coreutils-8.26/src/expand-common.h	2016-12-02 19:15:23.518391649 -0600
@@ -34,6 +34,18 @@ extern size_t max_column_width;
 /* The desired exit status.  */
 extern int exit_status;

+extern int
+set_utf_locale (void);
+
+extern bool
+check_utf_locale(void);
+
+extern bool
+check_bom(FILE* fp, mb_file_t *mbf);
+
+extern void
+print_bom(void);
+
 /* Add tab stop TABVAL to the end of 'tab_list'.  */
 extern void
 add_tab_stop (uintmax_t tabval);
diff -Naurp coreutils-8.26-orig/src/fold.c coreutils-8.26/src/fold.c
--- coreutils-8.26-orig/src/fold.c	2016-11-06 16:15:30.000000000 -0600
+++ coreutils-8.26/src/fold.c	2016-12-02 19:15:23.519391564 -0600
@@ -22,12 +22,34 @@
 #include <getopt.h>
 #include <sys/types.h>

+/* Get mbstate_t, mbrtowc(), wcwidth().  */
+#if HAVE_WCHAR_H
+# include <wchar.h>
+#endif
+
+/* Get iswprint(), iswblank(), wcwidth().  */
+#if HAVE_WCTYPE_H
+# include <wctype.h>
+#endif
+
 #include "system.h"
 #include "die.h"
 #include "error.h"
 #include "fadvise.h"
 #include "xdectoint.h"

+/* MB_LEN_MAX is incorrectly defined to be 1 in at least one GCC
+      installation; work around this configuration error.  */
+#if !defined MB_LEN_MAX || MB_LEN_MAX < 2
+# undef MB_LEN_MAX
+# define MB_LEN_MAX 16
+#endif
+
+/* Some systems, like BeOS, have multibyte encodings but lack mbstate_t.  */
+#if HAVE_MBRTOWC && defined mbstate_t
+# define mbrtowc(pwc, s, n, ps) (mbrtowc) (pwc, s, n, 0)
+#endif
+
 #define TAB_WIDTH 8

 /* The official name of this program (e.g., no 'g' prefix).  */
@@ -35,20 +57,41 @@

 #define AUTHORS proper_name ("David MacKenzie")

+#define FATAL_ERROR(Message)                                            \
+  do                                                                    \
+    {                                                                   \
+      error (0, 0, (Message));                                          \
+      usage (2);                                                        \
+    }                                                                   \
+  while (0)
+
+enum operating_mode
+{
+  /* Fold texts by columns that are at the given positions. */
+  column_mode,
+
+  /* Fold texts by bytes that are at the given positions. */
+  byte_mode,
+
+  /* Fold texts by characters that are at the given positions. */
+  character_mode,
+};
+
+/* The argument shows current mode. (Default: column_mode) */
+static enum operating_mode operating_mode;
+
 /* If nonzero, try to break on whitespace. */
 static bool break_spaces;

-/* If nonzero, count bytes, not column positions. */
-static bool count_bytes;
-
 /* If nonzero, at least one of the files we read was standard input. */
 static bool have_read_stdin;

-static char const shortopts[] = "bsw:0::1::2::3::4::5::6::7::8::9::";
+static char const shortopts[] = "bcsw:0::1::2::3::4::5::6::7::8::9::";

 static struct option const longopts[] =
 {
   {"bytes", no_argument, NULL, 'b'},
+  {"characters", no_argument, NULL, 'c'},
   {"spaces", no_argument, NULL, 's'},
   {"width", required_argument, NULL, 'w'},
   {GETOPT_HELP_OPTION_DECL},
@@ -76,6 +119,7 @@ Wrap input lines in each FILE, writing t

       fputs (_("\
   -b, --bytes         count bytes rather than columns\n\
+  -c, --characters    count characters rather than columns\n\
   -s, --spaces        break at spaces\n\
   -w, --width=WIDTH   use WIDTH columns instead of 80\n\
 "), stdout);
@@ -93,7 +137,7 @@ Wrap input lines in each FILE, writing t
 static size_t
 adjust_column (size_t column, char c)
 {
-  if (!count_bytes)
+  if (operating_mode != byte_mode)
     {
       if (c == '\b')
         {
@@ -116,30 +160,14 @@ adjust_column (size_t column, char c)
    to stdout, with maximum line length WIDTH.
    Return true if successful.  */

-static bool
-fold_file (char const *filename, size_t width)
+static void
+fold_text (FILE *istream, size_t width, int *saved_errno)
 {
-  FILE *istream;
   int c;
   size_t column = 0;		/* Screen column where next char will go. */
   size_t offset_out = 0;	/* Index in 'line_out' for next char. */
   static char *line_out = NULL;
   static size_t allocated_out = 0;
-  int saved_errno;
-
-  if (STREQ (filename, "-"))
-    {
-      istream = stdin;
-      have_read_stdin = true;
-    }
-  else
-    istream = fopen (filename, "r");
-
-  if (istream == NULL)
-    {
-      error (0, errno, "%s", quotef (filename));
-      return false;
-    }

   fadvise (istream, FADVISE_SEQUENTIAL);

@@ -169,6 +197,15 @@ fold_file (char const *filename, size_t
               bool found_blank = false;
               size_t logical_end = offset_out;

+              /* If LINE_OUT has no wide character,
+                 put a new wide character in LINE_OUT
+                 if column is bigger than width. */
+              if (offset_out == 0)
+                {
+                  line_out[offset_out++] = c;
+                  continue;
+                }
+
               /* Look for the last blank. */
               while (logical_end)
                 {
@@ -215,11 +252,221 @@ fold_file (char const *filename, size_t
       line_out[offset_out++] = c;
     }

-  saved_errno = errno;
+  *saved_errno = errno;

   if (offset_out)
     fwrite (line_out, sizeof (char), (size_t) offset_out, stdout);

+}
+
+#if HAVE_MBRTOWC
+static void
+fold_multibyte_text (FILE *istream, size_t width, int *saved_errno)
+{
+  char buf[MB_LEN_MAX + BUFSIZ];  /* For spooling a read byte sequence. */
+  size_t buflen = 0;        /* The length of the byte sequence in buf. */
+  char *bufpos = buf;         /* Next read position of BUF. */
+  wint_t wc;                /* A gotten wide character. */
+  size_t mblength;        /* The byte size of a multibyte character which shows
+                           as same character as WC. */
+  mbstate_t state, state_bak;        /* State of the stream. */
+  int convfail = 0;                /* 1, when conversion is failed. Otherwise 0. */
+
+  static char *line_out = NULL;
+  size_t offset_out = 0;        /* Index in `line_out' for next char. */
+  static size_t allocated_out = 0;
+
+  int increment;
+  size_t column = 0;
+
+  size_t last_blank_pos;
+  size_t last_blank_column;
+  int is_blank_seen;
+  int last_blank_increment = 0;
+  int is_bs_following_last_blank;
+  size_t bs_following_last_blank_num;
+  int is_cr_after_last_blank;
+
+#define CLEAR_FLAGS                                \
+   do                                                \
+     {                                                \
+        last_blank_pos = 0;                        \
+        last_blank_column = 0;                        \
+        is_blank_seen = 0;                        \
+        is_bs_following_last_blank = 0;                \
+        bs_following_last_blank_num = 0;        \
+        is_cr_after_last_blank = 0;                \
+     }                                                \
+   while (0)
+
+#define START_NEW_LINE                        \
+   do                                        \
+     {                                        \
+      putchar ('\n');                        \
+      column = 0;                        \
+      offset_out = 0;                        \
+      CLEAR_FLAGS;                        \
+    }                                        \
+   while (0)
+
+  CLEAR_FLAGS;
+  memset (&state, '\0', sizeof(mbstate_t));
+
+  for (;; bufpos += mblength, buflen -= mblength)
+    {
+      if (buflen < MB_LEN_MAX && !feof (istream) && !ferror (istream))
+        {
+          memmove (buf, bufpos, buflen);
+          buflen += fread (buf + buflen, sizeof(char), BUFSIZ, istream);
+          bufpos = buf;
+        }
+
+      if (buflen < 1)
+        break;
+
+      /* Get a wide character. */
+      state_bak = state;
+      mblength = mbrtowc ((wchar_t *)&wc, bufpos, buflen, &state);
+
+      switch (mblength)
+        {
+        case (size_t)-1:
+        case (size_t)-2:
+          convfail++;
+          state = state_bak;
+          /* Fall through. */
+
+        case 0:
+          mblength = 1;
+          break;
+        }
+
+rescan:
+      if (operating_mode == byte_mode)                        /* byte mode */
+        increment = mblength;
+      else if (operating_mode == character_mode)        /* character mode */
+        increment = 1;
+      else                                                /* column mode */
+        {
+          if (convfail)
+            increment = 1;
+          else
+            {
+              switch (wc)
+                {
+                case L'\n':
+                  fwrite (line_out, sizeof(char), offset_out, stdout);
+                  START_NEW_LINE;
+                  continue;
+
+                case L'\b':
+                  increment = (column > 0) ? -1 : 0;
+                  break;
+
+                case L'\r':
+                  increment = -1 * column;
+                  break;
+
+                case L'\t':
+                  increment = 8 - column % 8;
+                  break;
+
+                default:
+                  increment = wcwidth (wc);
+                  increment = (increment < 0) ? 0 : increment;
+                }
+            }
+        }
+
+      if (column + increment > width && break_spaces && last_blank_pos)
+        {
+          fwrite (line_out, sizeof(char), last_blank_pos, stdout);
+          putchar ('\n');
+
+          offset_out = offset_out - last_blank_pos;
+          column = column - last_blank_column + ((is_cr_after_last_blank)
+              ? last_blank_increment : bs_following_last_blank_num);
+          memmove (line_out, line_out + last_blank_pos, offset_out);
+          CLEAR_FLAGS;
+          goto rescan;
+        }
+
+      if (column + increment > width && column != 0)
+        {
+          fwrite (line_out, sizeof(char), offset_out, stdout);
+          START_NEW_LINE;
+          goto rescan;
+        }
+
+      if (allocated_out < offset_out + mblength)
+        {
+          line_out = X2REALLOC (line_out, &allocated_out);
+        }
+
+      memcpy (line_out + offset_out, bufpos, mblength);
+      offset_out += mblength;
+      column += increment;
+
+      if (is_blank_seen && !convfail && wc == L'\r')
+        is_cr_after_last_blank = 1;
+
+      if (is_bs_following_last_blank && !convfail && wc == L'\b')
+        ++bs_following_last_blank_num;
+      else
+        is_bs_following_last_blank = 0;
+
+      if (break_spaces && !convfail && iswblank (wc))
+        {
+          last_blank_pos = offset_out;
+          last_blank_column = column;
+          is_blank_seen = 1;
+          last_blank_increment = increment;
+          is_bs_following_last_blank = 1;
+          bs_following_last_blank_num = 0;
+          is_cr_after_last_blank = 0;
+        }
+    }
+
+  *saved_errno = errno;
+
+  if (offset_out)
+    fwrite (line_out, sizeof (char), (size_t) offset_out, stdout);
+
+}
+#endif
+
+/* Fold file FILENAME, or standard input if FILENAME is "-",
+   to stdout, with maximum line length WIDTH.
+   Return 0 if successful, 1 if an error occurs. */
+
+static bool
+fold_file (char const *filename, size_t width)
+{
+  FILE *istream;
+  int saved_errno;
+
+  if (STREQ (filename, "-"))
+    {
+      istream = stdin;
+      have_read_stdin = 1;
+    }
+  else
+    istream = fopen (filename, "r");
+
+  if (istream == NULL)
+    {
+      error (0, errno, "%s", filename);
+      return 1;
+    }
+
+  /* Define how ISTREAM is being folded. */
+#if HAVE_MBRTOWC
+  if (MB_CUR_MAX > 1)
+    fold_multibyte_text (istream, width, &saved_errno);
+  else
+#endif
+    fold_text (istream, width, &saved_errno);
+
   if (ferror (istream))
     {
       error (0, saved_errno, "%s", quotef (filename));
@@ -252,7 +499,8 @@ main (int argc, char **argv)

   atexit (close_stdout);

-  break_spaces = count_bytes = have_read_stdin = false;
+  operating_mode = column_mode;
+  break_spaces = have_read_stdin = false;

   while ((optc = getopt_long (argc, argv, shortopts, longopts, NULL)) != -1)
     {
@@ -261,7 +509,15 @@ main (int argc, char **argv)
       switch (optc)
         {
         case 'b':		/* Count bytes rather than columns. */
-          count_bytes = true;
+          if (operating_mode != column_mode)
+            FATAL_ERROR (_("only one way of folding may be specified"));
+          operating_mode = byte_mode;
+          break;
+
+        case 'c':
+          if (operating_mode != column_mode)
+            FATAL_ERROR (_("only one way of folding may be specified"));
+          operating_mode = character_mode;
           break;

         case 's':		/* Break at word boundaries. */
diff -Naurp coreutils-8.26-orig/src/join.c coreutils-8.26/src/join.c
--- coreutils-8.26-orig/src/join.c	2016-11-06 16:15:30.000000000 -0600
+++ coreutils-8.26/src/join.c	2016-12-02 19:15:23.520391480 -0600
@@ -22,19 +22,33 @@
 #include <sys/types.h>
 #include <getopt.h>

+/* Get mbstate_t, mbrtowc(), mbrtowc(), wcwidth().  */
+#if HAVE_WCHAR_H
+# include <wchar.h>
+#endif
+
+/* Get iswblank(), towupper.  */
+#if HAVE_WCTYPE_H
+# include <wctype.h>
+#endif
+
 #include "system.h"
 #include "die.h"
 #include "error.h"
 #include "fadvise.h"
 #include "hard-locale.h"
 #include "linebuffer.h"
-#include "memcasecmp.h"
 #include "quote.h"
 #include "stdio--.h"
 #include "xmemcoll.h"
 #include "xstrtol.h"
 #include "argmatch.h"

+/* Some systems, like BeOS, have multibyte encodings but lack mbstate_t.  */
+#if HAVE_MBRTOWC && defined mbstate_t
+# define mbrtowc(pwc, s, n, ps) (mbrtowc) (pwc, s, n, 0)
+#endif
+
 /* The official name of this program (e.g., no 'g' prefix).  */
 #define PROGRAM_NAME "join"

@@ -136,10 +150,12 @@ static struct outlist outlist_head;
 /* Last element in 'outlist', where a new element can be added.  */
 static struct outlist *outlist_end = &outlist_head;

-/* Tab character separating fields.  If negative, fields are separated
-   by any nonempty string of blanks, otherwise by exactly one
-   tab character whose value (when cast to unsigned char) equals TAB.  */
-static int tab = -1;
+/* Tab character separating fields.  If NULL, fields are separated
+   by any nonempty string of blanks.  */
+static char *tab = NULL;
+
+/* The number of bytes used for tab. */
+static size_t tablen = 0;

 /* If nonzero, check that the input is correctly ordered. */
 static enum
@@ -276,13 +292,14 @@ xfields (struct line *line)
   if (ptr == lim)
     return;

-  if (0 <= tab && tab != '\n')
+  if (tab != NULL)
     {
+      unsigned char t = tab[0];
       char *sep;
-      for (; (sep = memchr (ptr, tab, lim - ptr)) != NULL; ptr = sep + 1)
+      for (; (sep = memchr (ptr, t, lim - ptr)) != NULL; ptr = sep + 1)
         extract_field (line, ptr, sep - ptr);
     }
-  else if (tab < 0)
+   else
     {
       /* Skip leading blanks before the first field.  */
       while (field_sep (*ptr))
@@ -306,6 +323,147 @@ xfields (struct line *line)
   extract_field (line, ptr, lim - ptr);
 }

+#if HAVE_MBRTOWC
+static void
+xfields_multibyte (struct line *line)
+{
+  char *ptr = line->buf.buffer;
+  char const *lim = ptr + line->buf.length - 1;
+  wchar_t wc = 0;
+  size_t mblength = 1;
+  mbstate_t state, state_bak;
+
+  memset (&state, 0, sizeof (mbstate_t));
+
+  if (ptr >= lim)
+    return;
+
+  if (tab != NULL)
+    {
+      char *sep = ptr;
+      for (; ptr < lim; ptr = sep + mblength)
+	{
+	  sep = ptr;
+	  while (sep < lim)
+	    {
+	      state_bak = state;
+	      mblength = mbrtowc (&wc, sep, lim - sep + 1, &state);
+
+	      if (mblength == (size_t)-1 || mblength == (size_t)-2)
+		{
+		  mblength = 1;
+		  state = state_bak;
+		}
+	      mblength = (mblength < 1) ? 1 : mblength;
+
+	      if (mblength == tablen && !memcmp (sep, tab, mblength))
+		break;
+	      else
+		{
+		  sep += mblength;
+		  continue;
+		}
+	    }
+
+	  if (sep >= lim)
+	    break;
+
+	  extract_field (line, ptr, sep - ptr);
+	}
+    }
+  else
+    {
+      /* Skip leading blanks before the first field.  */
+      while(ptr < lim)
+      {
+        state_bak = state;
+        mblength = mbrtowc (&wc, ptr, lim - ptr + 1, &state);
+
+        if (mblength == (size_t)-1 || mblength == (size_t)-2)
+          {
+            mblength = 1;
+            state = state_bak;
+            break;
+          }
+        mblength = (mblength < 1) ? 1 : mblength;
+
+        if (!iswblank(wc) && wc != '\n')
+          break;
+        ptr += mblength;
+      }
+
+      do
+	{
+	  char *sep;
+	  state_bak = state;
+	  mblength = mbrtowc (&wc, ptr, lim - ptr + 1, &state);
+	  if (mblength == (size_t)-1 || mblength == (size_t)-2)
+	    {
+	      mblength = 1;
+	      state = state_bak;
+	      break;
+	    }
+	  mblength = (mblength < 1) ? 1 : mblength;
+
+	  sep = ptr + mblength;
+	  while (sep < lim)
+	    {
+	      state_bak = state;
+	      mblength = mbrtowc (&wc, sep, lim - sep + 1, &state);
+	      if (mblength == (size_t)-1 || mblength == (size_t)-2)
+		{
+		  mblength = 1;
+		  state = state_bak;
+		  break;
+		}
+	      mblength = (mblength < 1) ? 1 : mblength;
+
+	      if (iswblank (wc) || wc == '\n')
+		break;
+
+	      sep += mblength;
+	    }
+
+	  extract_field (line, ptr, sep - ptr);
+	  if (sep >= lim)
+	    return;
+
+	  state_bak = state;
+	  mblength = mbrtowc (&wc, sep, lim - sep + 1, &state);
+	  if (mblength == (size_t)-1 || mblength == (size_t)-2)
+	    {
+	      mblength = 1;
+	      state = state_bak;
+	      break;
+	    }
+	  mblength = (mblength < 1) ? 1 : mblength;
+
+	  ptr = sep + mblength;
+	  while (ptr < lim)
+	    {
+	      state_bak = state;
+	      mblength = mbrtowc (&wc, ptr, lim - ptr + 1, &state);
+	      if (mblength == (size_t)-1 || mblength == (size_t)-2)
+		{
+		  mblength = 1;
+		  state = state_bak;
+		  break;
+		}
+	      mblength = (mblength < 1) ? 1 : mblength;
+
+	      if (!iswblank (wc) && wc != '\n')
+		break;
+
+	      ptr += mblength;
+	    }
+	}
+      while (ptr < lim);
+    }
+
+  extract_field (line, ptr, lim - ptr);
+}
+#endif
+
 static void
 freeline (struct line *line)
 {
@@ -327,56 +485,133 @@ keycmp (struct line const *line1, struct
         size_t jf_1, size_t jf_2)
 {
   /* Start of field to compare in each file.  */
-  char *beg1;
-  char *beg2;
-
-  size_t len1;
-  size_t len2;		/* Length of fields to compare.  */
+  char *beg[2];
+  char *copy[2];
+  size_t len[2]; 	/* Length of fields to compare.  */
   int diff;
+  int i, j;
+  int mallocd = 0;

   if (jf_1 < line1->nfields)
     {
-      beg1 = line1->fields[jf_1].beg;
-      len1 = line1->fields[jf_1].len;
+      beg[0] = line1->fields[jf_1].beg;
+      len[0] = line1->fields[jf_1].len;
     }
   else
     {
-      beg1 = NULL;
-      len1 = 0;
+      beg[0] = NULL;
+      len[0] = 0;
     }

   if (jf_2 < line2->nfields)
     {
-      beg2 = line2->fields[jf_2].beg;
-      len2 = line2->fields[jf_2].len;
+      beg[1] = line2->fields[jf_2].beg;
+      len[1] = line2->fields[jf_2].len;
     }
   else
     {
-      beg2 = NULL;
-      len2 = 0;
+      beg[1] = NULL;
+      len[1] = 0;
     }

-  if (len1 == 0)
-    return len2 == 0 ? 0 : -1;
-  if (len2 == 0)
+  if (len[0] == 0)
+    return len[1] == 0 ? 0 : -1;
+  if (len[1] == 0)
     return 1;

   if (ignore_case)
     {
-      /* FIXME: ignore_case does not work with NLS (in particular,
-         with multibyte chars).  */
-      diff = memcasecmp (beg1, beg2, MIN (len1, len2));
+#ifdef HAVE_MBRTOWC
+      if (MB_CUR_MAX > 1)
+      {
+        size_t mblength;
+        wchar_t wc, uwc;
+        mbstate_t state, state_bak;
+
+        memset (&state, '\0', sizeof (mbstate_t));
+
+        for (i = 0; i < 2; i++)
+          {
+            mallocd = 1;
+            copy[i] = xmalloc (len[i] + 1);
+            memset (copy[i], '\0',len[i] + 1);
+
+            for (j = 0; j < MIN (len[0], len[1]);)
+              {
+                state_bak = state;
+                mblength = mbrtowc (&wc, beg[i] + j, len[i] - j, &state);
+
+                switch (mblength)
+                  {
+                  case (size_t) -1:
+                  case (size_t) -2:
+                    state = state_bak;
+                    /* Fall through */
+                  case 0:
+                    mblength = 1;
+                    break;
+
+                  default:
+                    uwc = towupper (wc);
+
+                    if (uwc != wc)
+                      {
+                        mbstate_t state_wc;
+                        size_t mblen;
+
+                        memset (&state_wc, '\0', sizeof (mbstate_t));
+                        mblen = wcrtomb (copy[i] + j, uwc, &state_wc);
+                        assert (mblen != (size_t)-1);
+                      }
+                    else
+                      memcpy (copy[i] + j, beg[i] + j, mblength);
+                  }
+                j += mblength;
+              }
+            copy[i][j] = '\0';
+          }
+      }
+      else
+#endif
+      {
+        for (i = 0; i < 2; i++)
+          {
+            mallocd = 1;
+            copy[i] = xmalloc (len[i] + 1);
+
+            for (j = 0; j < MIN (len[0], len[1]); j++)
+              copy[i][j] = toupper (beg[i][j]);
+
+            copy[i][j] = '\0';
+          }
+      }
     }
   else
     {
-      if (hard_LC_COLLATE)
-        return xmemcoll (beg1, len1, beg2, len2);
-      diff = memcmp (beg1, beg2, MIN (len1, len2));
+      copy[0] = beg[0];
+      copy[1] = beg[1];
     }

+  if (hard_LC_COLLATE)
+    {
+      diff = xmemcoll ((char *) copy[0], len[0], (char *) copy[1], len[1]);
+
+      if (mallocd)
+        for (i = 0; i < 2; i++)
+          free (copy[i]);
+
+      return diff;
+    }
+  diff = memcmp (copy[0], copy[1], MIN (len[0], len[1]));
+
+  if (mallocd)
+    for (i = 0; i < 2; i++)
+      free (copy[i]);
+
+
   if (diff)
     return diff;
-  return len1 < len2 ? -1 : len1 != len2;
+  return len[0] - len[1];
 }

 /* Check that successive input lines PREV and CURRENT from input file
@@ -468,6 +703,11 @@ get_line (FILE *fp, struct line **linep,
     }
   ++line_no[which - 1];

+#if HAVE_MBRTOWC
+  if (MB_CUR_MAX > 1)
+    xfields_multibyte (line);
+  else
+#endif
   xfields (line);

   if (prevline[which - 1])
@@ -567,21 +807,28 @@ prfield (size_t n, struct line const *li

 /* Output all the fields in line, other than the join field.  */

+#define PUT_TAB_CHAR							\
+  do									\
+    {									\
+      (tab != NULL) ?							\
+	fwrite(tab, sizeof(char), tablen, stdout) : putchar (' ');	\
+    }									\
+  while (0)
+
 static void
 prfields (struct line const *line, size_t join_field, size_t autocount)
 {
   size_t i;
   size_t nfields = autoformat ? autocount : line->nfields;
-  char output_separator = tab < 0 ? ' ' : tab;

   for (i = 0; i < join_field && i < nfields; ++i)
     {
-      putchar (output_separator);
+      PUT_TAB_CHAR;
       prfield (i, line);
     }
   for (i = join_field + 1; i < nfields; ++i)
     {
-      putchar (output_separator);
+      PUT_TAB_CHAR;
       prfield (i, line);
     }
 }
@@ -592,7 +839,6 @@ static void
 prjoin (struct line const *line1, struct line const *line2)
 {
   const struct outlist *outlist;
-  char output_separator = tab < 0 ? ' ' : tab;
   size_t field;
   struct line const *line;

@@ -626,7 +872,7 @@ prjoin (struct line const *line1, struct
           o = o->next;
           if (o == NULL)
             break;
-          putchar (output_separator);
+          PUT_TAB_CHAR;
         }
       putchar (eolchar);
     }
@@ -1104,20 +1350,43 @@ main (int argc, char **argv)

         case 't':
           {
-            unsigned char newtab = optarg[0];
+            char *newtab = NULL;
+            size_t newtablen;
+            newtab = xstrdup (optarg);
+#if HAVE_MBRTOWC
+            if (MB_CUR_MAX > 1)
+              {
+                mbstate_t state;
+
+                memset (&state, 0, sizeof (mbstate_t));
+                newtablen = mbrtowc (NULL, newtab,
+                                     strnlen (newtab, MB_LEN_MAX),
+                                     &state);
+                if (newtablen == (size_t) 0
+                    || newtablen == (size_t) -1
+                    || newtablen == (size_t) -2)
+                  newtablen = 1;
+              }
+            else
+#endif
+              newtablen = 1;
             if (! newtab)
-              newtab = '\n'; /* '' => process the whole line.  */
+              newtab = (char*)"\n"; /* '' => process the whole line.  */
             else if (optarg[1])
               {
-                if (STREQ (optarg, "\\0"))
-                  newtab = '\0';
-                else
-                  die (EXIT_FAILURE, 0, _("multi-character tab %s"),
-                       quote (optarg));
+                if (newtablen == 1 && newtab[1])
+                {
+                  if (STREQ (newtab, "\\0"))
+                     newtab[0] = '\0';
+                }
+              }
+            if (tab != NULL && strcmp (tab, newtab))
+              {
+                free (newtab);
+                die (EXIT_FAILURE, 0, _("incompatible tabs"));
               }
-            if (0 <= tab && tab != newtab)
-              die (EXIT_FAILURE, 0, _("incompatible tabs"));
             tab = newtab;
+            tablen = newtablen;
           }
           break;

diff -Naurp coreutils-8.26-orig/src/pr.c coreutils-8.26/src/pr.c
--- coreutils-8.26-orig/src/pr.c	2016-11-25 07:40:49.000000000 -0600
+++ coreutils-8.26/src/pr.c	2016-12-02 19:15:23.522391311 -0600
@@ -311,6 +311,24 @@

 #include <getopt.h>
 #include <sys/types.h>
+
+/* Get MB_LEN_MAX.  */
+#include <limits.h>
+/* MB_LEN_MAX is incorrectly defined to be 1 in at least one GCC
+   installation; work around this configuration error.  */
+#if !defined MB_LEN_MAX || MB_LEN_MAX == 1
+# define MB_LEN_MAX 16
+#endif
+
+/* Get MB_CUR_MAX.  */
+#include <stdlib.h>
+
+/* Solaris 2.5 has a bug: <wchar.h> must be included before <wctype.h>.  */
+/* Get mbstate_t, mbrtowc(), wcwidth().  */
+#if HAVE_WCHAR_H
+# include <wchar.h>
+#endif
+
 #include "system.h"
 #include "die.h"
 #include "error.h"
@@ -324,6 +342,18 @@
 #include "xstrtol.h"
 #include "xdectoint.h"

+/* Some systems, like BeOS, have multibyte encodings but lack mbstate_t.  */
+#if HAVE_MBRTOWC && defined mbstate_t
+# define mbrtowc(pwc, s, n, ps) (mbrtowc) (pwc, s, n, 0)
+#endif
+
+#ifndef HAVE_DECL_WCWIDTH
+"this configure-time declaration test was not run"
+#endif
+#if !HAVE_DECL_WCWIDTH
+extern int wcwidth ();
+#endif
+
 /* The official name of this program (e.g., no 'g' prefix).  */
 #define PROGRAM_NAME "pr"

@@ -416,7 +446,20 @@ struct COLUMN

 typedef struct COLUMN COLUMN;

-static int char_to_clump (char c);
+/* Funtion pointers to switch functions for single byte locale or for
+   multibyte locale. If multibyte functions do not exist in your sysytem,
+   these pointers always point the function for single byte locale. */
+static void (*print_char) (char c);
+static int (*char_to_clump) (char c);
+
+/* Functions for single byte locale. */
+static void print_char_single (char c);
+static int char_to_clump_single (char c);
+
+/* Functions for multibyte locale. */
+static void print_char_multi (char c);
+static int char_to_clump_multi (char c);
+
 static bool read_line (COLUMN *p);
 static bool print_page (void);
 static bool print_stored (COLUMN *p);
@@ -428,6 +471,7 @@ static void add_line_number (COLUMN *p);
 static void getoptnum (const char *n_str, int min, int *num,
                        const char *errfmt);
 static void getoptarg (char *arg, char switch_char, char *character,
+                       int *character_length, int *character_width,
                        int *number);
 static void print_files (int number_of_files, char **av);
 static void init_parameters (int number_of_files);
@@ -441,7 +485,6 @@ static void store_char (char c);
 static void pad_down (unsigned int lines);
 static void read_rest_of_line (COLUMN *p);
 static void skip_read (COLUMN *p, int column_number);
-static void print_char (char c);
 static void cleanup (void);
 static void print_sep_string (void);
 static void separator_string (const char *optarg_S);
@@ -453,7 +496,7 @@ static COLUMN *column_vector;
    we store the leftmost columns contiguously in buff.
    To print a line from buff, get the index of the first character
    from line_vector[i], and print up to line_vector[i + 1]. */
-static char *buff;
+static unsigned char *buff;

 /* Index of the position in buff where the next character
    will be stored. */
@@ -557,7 +600,7 @@ static int chars_per_column;
 static bool untabify_input = false;

 /* (-e) The input tab character. */
-static char input_tab_char = '\t';
+static char input_tab_char[MB_LEN_MAX] = "\t";

 /* (-e) Tabstops are at chars_per_tab, 2*chars_per_tab, 3*chars_per_tab, ...
    where the leftmost column is 1. */
@@ -567,7 +610,10 @@ static int chars_per_input_tab = 8;
 static bool tabify_output = false;

 /* (-i) The output tab character. */
-static char output_tab_char = '\t';
+static char output_tab_char[MB_LEN_MAX] = "\t";
+
+/* (-i) The byte length of output tab character. */
+static int output_tab_char_length = 1;

 /* (-i) The width of the output tab. */
 static int chars_per_output_tab = 8;
@@ -637,7 +683,13 @@ static int line_number;
 static bool numbered_lines = false;

 /* (-n) Character which follows each line number. */
-static char number_separator = '\t';
+static char number_separator[MB_LEN_MAX] = "\t";
+
+/* (-n) The byte length of the character which follows each line number. */
+static int number_separator_length = 1;
+
+/* (-n) The character width of the character which follows each line number. */
+static int number_separator_width = 0;

 /* (-n) line counting starts with 1st line of input file (not with 1st
    line of 1st page printed). */
@@ -690,6 +742,7 @@ static bool use_col_separator = false;
    -a|COLUMN|-m is a 'space' and with the -J option a 'tab'. */
 static char const *col_sep_string = "";
 static int col_sep_length = 0;
+static int col_sep_width = 0;
 static char *column_separator = (char *) " ";
 static char *line_separator = (char *) "\t";

@@ -851,6 +904,13 @@ separator_string (const char *optarg_S)
     integer_overflow ();
   col_sep_length = len;
   col_sep_string = optarg_S;
+
+#if HAVE_MBRTOWC
+  if (MB_CUR_MAX > 1)
+    col_sep_width = mbswidth (col_sep_string, 0);
+  else
+#endif
+    col_sep_width = col_sep_length;
 }

 int
@@ -875,6 +935,21 @@ main (int argc, char **argv)

   atexit (close_stdout);

+/* Define which functions are used, the ones for single byte locale or the ones
+   for multibyte locale. */
+#if HAVE_MBRTOWC
+  if (MB_CUR_MAX > 1)
+    {
+      print_char = print_char_multi;
+      char_to_clump = char_to_clump_multi;
+    }
+  else
+#endif
+    {
+      print_char = print_char_single;
+      char_to_clump = char_to_clump_single;
+    }
+
   n_files = 0;
   file_names = (argc > 1
                 ? xnmalloc (argc - 1, sizeof (char *))
@@ -951,8 +1026,12 @@ main (int argc, char **argv)
           break;
         case 'e':
           if (optarg)
-            getoptarg (optarg, 'e', &input_tab_char,
-                       &chars_per_input_tab);
+            {
+              int dummy_length, dummy_width;
+
+              getoptarg (optarg, 'e', input_tab_char, &dummy_length,
+                         &dummy_width, &chars_per_input_tab);
+            }
           /* Could check tab width > 0. */
           untabify_input = true;
           break;
@@ -965,8 +1044,12 @@ main (int argc, char **argv)
           break;
         case 'i':
           if (optarg)
-            getoptarg (optarg, 'i', &output_tab_char,
-                       &chars_per_output_tab);
+            {
+              int dummy_width;
+
+              getoptarg (optarg, 'i', output_tab_char, &output_tab_char_length,
+                         &dummy_width, &chars_per_output_tab);
+            }
           /* Could check tab width > 0. */
           tabify_output = true;
           break;
@@ -984,8 +1067,8 @@ main (int argc, char **argv)
         case 'n':
           numbered_lines = true;
           if (optarg)
-            getoptarg (optarg, 'n', &number_separator,
-                       &chars_per_number);
+            getoptarg (optarg, 'n', number_separator, &number_separator_length,
+                       &number_separator_width, &chars_per_number);
           break;
         case 'N':
           skip_count = false;
@@ -1010,6 +1093,7 @@ main (int argc, char **argv)
           /* Reset an additional input of -s, -S dominates -s */
           col_sep_string = "";
           col_sep_length = 0;
+          col_sep_width = 0;
           use_col_separator = true;
           if (optarg)
             separator_string (optarg);
@@ -1166,10 +1250,45 @@ getoptnum (const char *n_str, int min, i
    a number. */

 static void
-getoptarg (char *arg, char switch_char, char *character, int *number)
+getoptarg (char *arg, char switch_char, char *character, int *character_length,
+           int *character_width, int *number)
 {
   if (!ISDIGIT (*arg))
-    *character = *arg++;
+    {
+#ifdef HAVE_MBRTOWC
+      if (MB_CUR_MAX > 1)        /* for multibyte locale. */
+        {
+          wchar_t wc;
+          size_t mblength;
+          int width;
+          mbstate_t state = {'\0'};
+
+          mblength = mbrtowc (&wc, arg, strnlen(arg, MB_LEN_MAX), &state);
+
+          if (mblength == (size_t)-1 || mblength == (size_t)-2)
+            {
+              *character_length = 1;
+              *character_width = 1;
+            }
+          else
+            {
+              *character_length = (mblength < 1) ? 1 : mblength;
+              width = wcwidth (wc);
+              *character_width = (width < 0) ? 0 : width;
+            }
+
+          strncpy (character, arg, *character_length);
+          arg += *character_length;
+        }
+      else                        /* for single byte locale. */
+#endif
+        {
+          *character = *arg++;
+          *character_length = 1;
+          *character_width = 1;
+        }
+    }
+
   if (*arg)
     {
       long int tmp_long;
@@ -1191,6 +1310,11 @@ static void
 init_parameters (int number_of_files)
 {
   int chars_used_by_number = 0;
+  int mb_len = 1;
+#if HAVE_MBRTOWC
+  if (MB_CUR_MAX > 1)
+    mb_len = MB_LEN_MAX;
+#endif

   lines_per_body = lines_per_page - lines_per_header - lines_per_footer;
   if (lines_per_body <= 0)
@@ -1228,7 +1352,7 @@ init_parameters (int number_of_files)
           else
             col_sep_string = column_separator;

-          col_sep_length = 1;
+          col_sep_length = col_sep_width = 1;
           use_col_separator = true;
         }
       /* It's rather pointless to define a TAB separator with column
@@ -1258,11 +1382,11 @@ init_parameters (int number_of_files)
              + TAB_WIDTH (chars_per_input_tab, chars_per_number);   */

       /* Estimate chars_per_text without any margin and keep it constant. */
-      if (number_separator == '\t')
+      if (number_separator[0] == '\t')
         number_width = (chars_per_number
                         + TAB_WIDTH (chars_per_default_tab, chars_per_number));
       else
-        number_width = chars_per_number + 1;
+        number_width = chars_per_number + number_separator_width;

       /* The number is part of the column width unless we are
          printing files in parallel. */
@@ -1271,7 +1395,7 @@ init_parameters (int number_of_files)
     }

   int sep_chars, useful_chars;
-  if (INT_MULTIPLY_WRAPV (columns - 1, col_sep_length, &sep_chars))
+  if (INT_MULTIPLY_WRAPV (columns - 1, col_sep_width, &sep_chars))
     sep_chars = INT_MAX;
   if (INT_SUBTRACT_WRAPV (chars_per_line - chars_used_by_number, sep_chars,
                           &useful_chars))
@@ -1294,7 +1418,7 @@ init_parameters (int number_of_files)
      We've to use 8 as the lower limit, if we use chars_per_default_tab = 8
      to expand a tab which is not an input_tab-char. */
   free (clump_buff);
-  clump_buff = xmalloc (MAX (8, chars_per_input_tab));
+  clump_buff = xmalloc (mb_len * MAX (8, chars_per_input_tab));
 }

 /* Open the necessary files,
@@ -1402,7 +1526,7 @@ init_funcs (void)

   /* Enlarge p->start_position of first column to use the same form of
      padding_not_printed with all columns. */
-  h = h + col_sep_length;
+  h = h + col_sep_width;

   /* This loop takes care of all but the rightmost column. */

@@ -1436,7 +1560,7 @@ init_funcs (void)
         }
       else
         {
-          h = h_next + col_sep_length;
+          h = h_next + col_sep_width;
           h_next = h + chars_per_column;
         }
     }
@@ -1727,9 +1851,9 @@ static void
 align_column (COLUMN *p)
 {
   padding_not_printed = p->start_position;
-  if (col_sep_length < padding_not_printed)
+  if (col_sep_width < padding_not_printed)
     {
-      pad_across_to (padding_not_printed - col_sep_length);
+      pad_across_to (padding_not_printed - col_sep_width);
       padding_not_printed = ANYWHERE;
     }

@@ -2004,13 +2128,13 @@ store_char (char c)
       /* May be too generous. */
       buff = X2REALLOC (buff, &buff_allocated);
     }
-  buff[buff_current++] = c;
+  buff[buff_current++] = (unsigned char) c;
 }

 static void
 add_line_number (COLUMN *p)
 {
-  int i;
+  int i, j;
   char *s;
   int num_width;

@@ -2027,22 +2151,24 @@ add_line_number (COLUMN *p)
       /* Tabification is assumed for multiple columns, also for n-separators,
          but 'default n-separator = TAB' hasn't been given priority over
          equal column_width also specified by POSIX. */
-      if (number_separator == '\t')
+      if (number_separator[0] == '\t')
         {
           i = number_width - chars_per_number;
           while (i-- > 0)
             (p->char_func) (' ');
         }
       else
-        (p->char_func) (number_separator);
+        for (j = 0; j < number_separator_length; j++)
+          (p->char_func) (number_separator[j]);
     }
   else
     /* To comply with POSIX, we avoid any expansion of default TAB
        separator with a single column output. No column_width requirement
        has to be considered. */
     {
-      (p->char_func) (number_separator);
-      if (number_separator == '\t')
+      for (j = 0; j < number_separator_length; j++)
+        (p->char_func) (number_separator[j]);
+      if (number_separator[0] == '\t')
         output_position = POS_AFTER_TAB (chars_per_output_tab,
                           output_position);
     }
@@ -2203,7 +2329,7 @@ print_white_space (void)
   while (goal - h_old > 1
          && (h_new = POS_AFTER_TAB (chars_per_output_tab, h_old)) <= goal)
     {
-      putchar (output_tab_char);
+      fwrite (output_tab_char, sizeof(char), output_tab_char_length, stdout);
       h_old = h_new;
     }
   while (++h_old <= goal)
@@ -2223,6 +2349,7 @@ print_sep_string (void)
 {
   char const *s = col_sep_string;
   int l = col_sep_length;
+  int not_space_flag;

   if (separators_not_printed <= 0)
     {
@@ -2234,6 +2361,7 @@ print_sep_string (void)
     {
       for (; separators_not_printed > 0; --separators_not_printed)
         {
+          not_space_flag = 0;
           while (l-- > 0)
             {
               /* 3 types of sep_strings: spaces only, spaces and chars,
@@ -2247,12 +2375,15 @@ print_sep_string (void)
                 }
               else
                 {
+                  not_space_flag = 1;
                   if (spaces_not_printed > 0)
                     print_white_space ();
                   putchar (*s++);
-                  ++output_position;
                 }
             }
+          if (not_space_flag)
+            output_position += col_sep_width;
+
           /* sep_string ends with some spaces */
           if (spaces_not_printed > 0)
             print_white_space ();
@@ -2280,7 +2411,7 @@ print_clump (COLUMN *p, int n, char *clu
    required number of tabs and spaces. */

 static void
-print_char (char c)
+print_char_single (char c)
 {
   if (tabify_output)
     {
@@ -2304,6 +2435,74 @@ print_char (char c)
   putchar (c);
 }

+#ifdef HAVE_MBRTOWC
+static void
+print_char_multi (char c)
+{
+  static size_t mbc_pos = 0;
+  static char mbc[MB_LEN_MAX] = {'\0'};
+  static mbstate_t state = {'\0'};
+  mbstate_t state_bak;
+  wchar_t wc;
+  size_t mblength;
+  int width;
+
+  if (tabify_output)
+    {
+      state_bak = state;
+      mbc[mbc_pos++] = c;
+      mblength = mbrtowc (&wc, mbc, mbc_pos, &state);
+
+      while (mbc_pos > 0)
+        {
+          switch (mblength)
+            {
+            case (size_t)-2:
+              state = state_bak;
+              return;
+
+            case (size_t)-1:
+              state = state_bak;
+              ++output_position;
+              putchar (mbc[0]);
+              memmove (mbc, mbc + 1, MB_CUR_MAX - 1);
+              --mbc_pos;
+              break;
+
+            case 0:
+              mblength = 1;
+
+            default:
+              if (wc == L' ')
+                {
+                  memmove (mbc, mbc + mblength, MB_CUR_MAX - mblength);
+                  --mbc_pos;
+                  ++spaces_not_printed;
+                  return;
+                }
+              else if (spaces_not_printed > 0)
+                print_white_space ();
+
+              /* Nonprintables are assumed to have width 0, except L'\b'. */
+              if ((width = wcwidth (wc)) < 1)
+                {
+                  if (wc == L'\b')
+                    --output_position;
+                }
+              else
+                output_position += width;
+
+              fwrite (mbc, sizeof(char), mblength, stdout);
+              memmove (mbc, mbc + mblength, MB_CUR_MAX - mblength);
+              mbc_pos -= mblength;
+            }
+        }
+      return;
+    }
+  putchar (c);
+}
+#endif
+
 /* Skip to page PAGE before printing.
    PAGE may be larger than total number of pages. */

@@ -2483,9 +2682,9 @@ read_line (COLUMN *p)
           align_empty_cols = false;
         }

-      if (col_sep_length < padding_not_printed)
+      if (col_sep_width < padding_not_printed)
         {
-          pad_across_to (padding_not_printed - col_sep_length);
+          pad_across_to (padding_not_printed - col_sep_width);
           padding_not_printed = ANYWHERE;
         }

@@ -2555,7 +2754,7 @@ print_stored (COLUMN *p)
   int i;

   int line = p->current_line++;
-  char *first = &buff[line_vector[line]];
+  unsigned char *first = &buff[line_vector[line]];
   /* FIXME
      UMR: Uninitialized memory read:
      * This is occurring while in:
@@ -2567,7 +2766,7 @@ print_stored (COLUMN *p)
      xmalloc        [xmalloc.c:94]
      init_store_cols [pr.c:1648]
      */
-  char *last = &buff[line_vector[line + 1]];
+  unsigned char *last = &buff[line_vector[line + 1]];

   pad_vertically = true;

@@ -2586,9 +2785,9 @@ print_stored (COLUMN *p)
         }
     }

-  if (col_sep_length < padding_not_printed)
+  if (col_sep_width < padding_not_printed)
     {
-      pad_across_to (padding_not_printed - col_sep_length);
+      pad_across_to (padding_not_printed - col_sep_width);
       padding_not_printed = ANYWHERE;
     }

@@ -2601,8 +2800,8 @@ print_stored (COLUMN *p)
   if (spaces_not_printed == 0)
     {
       output_position = p->start_position + end_vector[line];
-      if (p->start_position - col_sep_length == chars_per_margin)
-        output_position -= col_sep_length;
+      if (p->start_position - col_sep_width == chars_per_margin)
+        output_position -= col_sep_width;
     }

   return true;
@@ -2621,7 +2820,7 @@ print_stored (COLUMN *p)
    number of characters is 1.) */

 static int
-char_to_clump (char c)
+char_to_clump_single (char c)
 {
   unsigned char uc = c;
   char *s = clump_buff;
@@ -2631,10 +2830,10 @@ char_to_clump (char c)
   int chars;
   int chars_per_c = 8;

-  if (c == input_tab_char)
+  if (c == input_tab_char[0])
     chars_per_c = chars_per_input_tab;

-  if (c == input_tab_char || c == '\t')
+  if (c == input_tab_char[0] || c == '\t')
     {
       width = TAB_WIDTH (chars_per_c, input_position);

@@ -2715,6 +2914,164 @@ char_to_clump (char c)
   return chars;
 }

+#ifdef HAVE_MBRTOWC
+static int
+char_to_clump_multi (char c)
+{
+  static size_t mbc_pos = 0;
+  static char mbc[MB_LEN_MAX] = {'\0'};
+  static mbstate_t state = {'\0'};
+  mbstate_t state_bak;
+  wchar_t wc;
+  size_t mblength;
+  int wc_width;
+  register char *s = clump_buff;
+  register int i, j;
+  char esc_buff[4];
+  int width;
+  int chars;
+  int chars_per_c = 8;
+
+  state_bak = state;
+  mbc[mbc_pos++] = c;
+  mblength = mbrtowc (&wc, mbc, mbc_pos, &state);
+
+  width = 0;
+  chars = 0;
+  while (mbc_pos > 0)
+    {
+      switch (mblength)
+        {
+        case (size_t)-2:
+          state = state_bak;
+          return 0;
+
+        case (size_t)-1:
+          state = state_bak;
+          mblength = 1;
+
+          if (use_esc_sequence || use_cntrl_prefix)
+            {
+              width = +4;
+              chars = +4;
+              *s++ = '\\';
+              sprintf (esc_buff, "%03o", (unsigned char) mbc[0]);
+              for (i = 0; i <= 2; ++i)
+                *s++ = (int) esc_buff[i];
+            }
+          else
+            {
+              width += 1;
+              chars += 1;
+              *s++ = mbc[0];
+            }
+          break;
+
+        case 0:
+          mblength = 1;
+                /* Fall through */
+
+        default:
+          if (memcmp (mbc, input_tab_char, mblength) == 0)
+            chars_per_c = chars_per_input_tab;
+
+          if (memcmp (mbc, input_tab_char, mblength) == 0 || c == '\t')
+            {
+              int  width_inc;
+
+              width_inc = TAB_WIDTH (chars_per_c, input_position);
+              width += width_inc;
+
+              if (untabify_input)
+                {
+                  for (i = width_inc; i; --i)
+                    *s++ = ' ';
+                  chars += width_inc;
+                }
+              else
+                {
+                  for (i = 0; i <  mblength; i++)
+                    *s++ = mbc[i];
+                  chars += mblength;
+                }
+            }
+          else if ((wc_width = wcwidth (wc)) < 1)
+            {
+              if (use_esc_sequence)
+                {
+                  for (i = 0; i < mblength; i++)
+                    {
+                      width += 4;
+                      chars += 4;
+                      *s++ = '\\';
+                      sprintf (esc_buff, "%03o", (unsigned char) mbc[i]);
+                      for (j = 0; j <= 2; ++j)
+                        *s++ = (int) esc_buff[j];
+                    }
+                }
+              else if (use_cntrl_prefix)
+                {
+                  if (wc < 0200)
+                    {
+                      width += 2;
+                      chars += 2;
+                      *s++ = '^';
+                      *s++ = wc ^ 0100;
+                    }
+                  else
+                    {
+                      for (i = 0; i < mblength; i++)
+                        {
+                          width += 4;
+                          chars += 4;
+                          *s++ = '\\';
+                          sprintf (esc_buff, "%03o", (unsigned char) mbc[i]);
+                          for (j = 0; j <= 2; ++j)
+                            *s++ = (int) esc_buff[j];
+                        }
+                    }
+                }
+              else if (wc == L'\b')
+                {
+                  width += -1;
+                  chars += 1;
+                  *s++ = c;
+                }
+              else
+                {
+                  width += 0;
+                  chars += mblength;
+                  for (i = 0; i < mblength; i++)
+                    *s++ = mbc[i];
+                }
+            }
+          else
+            {
+              width += wc_width;
+              chars += mblength;
+              for (i = 0; i < mblength; i++)
+                *s++ = mbc[i];
+            }
+        }
+      memmove (mbc, mbc + mblength, MB_CUR_MAX - mblength);
+      mbc_pos -= mblength;
+    }
+
+  /* Too many backspaces must put us in position 0 -- never negative. */
+  if (width < 0 && input_position == 0)
+    {
+      chars = 0;
+      input_position = 0;
+    }
+  else if (width < 0 && input_position <= -width)
+    input_position = 0;
+  else
+   input_position += width;
+
+  return chars;
+}
+#endif
+
 /* We've just printed some files and need to clean up things before
    looking for more options and printing the next batch of files.

diff -Naurp coreutils-8.26-orig/src/sort.c coreutils-8.26/src/sort.c
--- coreutils-8.26-orig/src/sort.c	2016-11-06 16:15:30.000000000 -0600
+++ coreutils-8.26/src/sort.c	2016-12-02 19:15:23.525391058 -0600
@@ -29,6 +29,14 @@
 #include <sys/wait.h>
 #include <signal.h>
 #include <assert.h>
+#if HAVE_WCHAR_H
+# include <wchar.h>
+#endif
+/* Get isw* functions. */
+#if HAVE_WCTYPE_H
+# include <wctype.h>
+#endif
+
 #include "system.h"
 #include "argmatch.h"
 #include "die.h"
@@ -165,14 +173,39 @@ static int decimal_point;
 /* Thousands separator; if -1, then there isn't one.  */
 static int thousands_sep;

+/* True if -f is specified.  */
+static bool folding;
+
 /* Nonzero if the corresponding locales are hard.  */
 static bool hard_LC_COLLATE;
-#if HAVE_NL_LANGINFO
+#if HAVE_LANGINFO_CODESET
 static bool hard_LC_TIME;
 #endif

 #define NONZERO(x) ((x) != 0)

+/* get a multibyte character's byte length. */
+#define GET_BYTELEN_OF_CHAR(LIM, PTR, MBLENGTH, STATE)                        \
+  do                                                                        \
+    {                                                                        \
+      wchar_t wc;                                                        \
+      mbstate_t state_bak;                                                \
+                                                                        \
+      state_bak = STATE;                                                \
+      mblength = mbrtowc (&wc, PTR, LIM - PTR, &STATE);                        \
+                                                                        \
+      switch (MBLENGTH)                                                        \
+        {                                                                \
+        case (size_t)-1:                                                \
+        case (size_t)-2:                                                \
+          STATE = state_bak;                                                \
+                /* Fall through. */                                        \
+        case 0:                                                                \
+          MBLENGTH = 1;                                                        \
+      }                                                                        \
+    }                                                                        \
+  while (0)
+
 /* The kind of blanks for '-b' to skip in various options. */
 enum blanktype { bl_start, bl_end, bl_both };

@@ -346,13 +379,11 @@ static bool reverse;
    they were read if all keys compare equal.  */
 static bool stable;

-/* If TAB has this value, blanks separate fields.  */
-enum { TAB_DEFAULT = CHAR_MAX + 1 };
-
-/* Tab character separating fields.  If TAB_DEFAULT, then fields are
+/* Tab character separating fields.  If tab_length is 0, then fields are
    separated by the empty string between a non-blank character and a blank
    character. */
-static int tab = TAB_DEFAULT;
+static char tab[MB_LEN_MAX + 1];
+static size_t tab_length = 0;

 /* Flag to remove consecutive duplicate lines from the output.
    Only the last of a sequence of equal lines will be output. */
@@ -811,6 +842,46 @@ reap_all (void)
     reap (-1);
 }

+/* Function pointers. */
+static void
+(*inittables) (void);
+static char *
+(*begfield) (const struct line*, const struct keyfield *);
+static char *
+(*limfield) (const struct line*, const struct keyfield *);
+static void
+(*skipblanks) (char **ptr, char *lim);
+static int
+(*getmonth) (char const *, size_t, char **);
+static int
+(*keycompare) (const struct line *, const struct line *);
+static int
+(*numcompare) (const char *, const char *);
+
+/* Test for white space multibyte character.
+   Set LENGTH the byte length of investigated multibyte character. */
+#if HAVE_MBRTOWC
+static int
+ismbblank (const char *str, size_t len, size_t *length)
+{
+  size_t mblength;
+  wchar_t wc;
+  mbstate_t state;
+
+  memset (&state, '\0', sizeof(mbstate_t));
+  mblength = mbrtowc (&wc, str, len, &state);
+
+  if (mblength == (size_t)-1 || mblength == (size_t)-2)
+    {
+      *length = 1;
+      return 0;
+    }
+
+  *length = (mblength < 1) ? 1 : mblength;
+  return iswblank (wc) || wc == '\n';
+}
+#endif
+
 /* Clean up any remaining temporary files.  */

 static void
@@ -1255,7 +1326,7 @@ zaptemp (char const *name)
   free (node);
 }

-#if HAVE_NL_LANGINFO
+#if HAVE_LANGINFO_CODESET

 static int
 struct_month_cmp (void const *m1, void const *m2)
@@ -1270,7 +1341,7 @@ struct_month_cmp (void const *m1, void c
 /* Initialize the character class tables. */

 static void
-inittables (void)
+inittables_uni (void)
 {
   size_t i;

@@ -1282,7 +1353,7 @@ inittables (void)
       fold_toupper[i] = toupper (i);
     }

-#if HAVE_NL_LANGINFO
+#if HAVE_LANGINFO_CODESET
   /* If we're not in the "C" locale, read different names for months.  */
   if (hard_LC_TIME)
     {
@@ -1364,6 +1435,84 @@ specify_nmerge (int oi, char c, char con
     xstrtol_fatal (e, oi, c, long_options, s);
 }

+#if HAVE_MBRTOWC
+static void
+inittables_mb (void)
+{
+  int i, j, k, l;
+  char *name, *s, *lc_time, *lc_ctype;
+  size_t s_len, mblength;
+  char mbc[MB_LEN_MAX];
+  wchar_t wc, pwc;
+  mbstate_t state_mb, state_wc;
+
+  lc_time = setlocale (LC_TIME, "");
+  if (lc_time)
+    lc_time = xstrdup (lc_time);
+
+  lc_ctype = setlocale (LC_CTYPE, "");
+  if (lc_ctype)
+    lc_ctype = xstrdup (lc_ctype);
+
+  if (lc_time && lc_ctype)
+    /* temporarily set LC_CTYPE to match LC_TIME, so that we can convert
+     * the names of months to upper case */
+    setlocale (LC_CTYPE, lc_time);
+
+  for (i = 0; i < MONTHS_PER_YEAR; i++)
+    {
+      s = (char *) nl_langinfo (ABMON_1 + i);
+      s_len = strlen (s);
+      monthtab[i].name = name = (char *) xmalloc (s_len + 1);
+      monthtab[i].val = i + 1;
+
+      memset (&state_mb, '\0', sizeof (mbstate_t));
+      memset (&state_wc, '\0', sizeof (mbstate_t));
+
+      for (j = 0; j < s_len;)
+        {
+          if (!ismbblank (s + j, s_len - j, &mblength))
+            break;
+          j += mblength;
+        }
+
+      for (k = 0; j < s_len;)
+        {
+          mblength = mbrtowc (&wc, (s + j), (s_len - j), &state_mb);
+          assert (mblength != (size_t)-1 && mblength != (size_t)-2);
+          if (mblength == 0)
+            break;
+
+          pwc = towupper (wc);
+          if (pwc == wc)
+            {
+              memcpy (mbc, s + j, mblength);
+              j += mblength;
+            }
+          else
+            {
+              j += mblength;
+              mblength = wcrtomb (mbc, pwc, &state_wc);
+              assert (mblength != (size_t)0 && mblength != (size_t)-1);
+            }
+
+          for (l = 0; l < mblength; l++)
+            name[k++] = mbc[l];
+        }
+      name[k] = '\0';
+    }
+  qsort ((void *) monthtab, MONTHS_PER_YEAR,
+      sizeof (struct month), struct_month_cmp);
+
+  if (lc_time && lc_ctype)
+    /* restore the original locales */
+    setlocale (LC_CTYPE, lc_ctype);
+
+  free (lc_ctype);
+  free (lc_time);
+}
+#endif
+
 /* Specify the amount of main memory to use when sorting.  */
 static void
 specify_sort_size (int oi, char c, char const *s)
@@ -1597,7 +1746,7 @@ buffer_linelim (struct buffer const *buf
    by KEY in LINE. */

 static char *
-begfield (struct line const *line, struct keyfield const *key)
+begfield_uni (const struct line *line, const struct keyfield *key)
 {
   char *ptr = line->text, *lim = ptr + line->length - 1;
   size_t sword = key->sword;
@@ -1606,10 +1755,10 @@ begfield (struct line const *line, struc
   /* The leading field separator itself is included in a field when -t
      is absent.  */

-  if (tab != TAB_DEFAULT)
+  if (tab_length)
     while (ptr < lim && sword--)
       {
-        while (ptr < lim && *ptr != tab)
+        while (ptr < lim && *ptr != tab[0])
           ++ptr;
         if (ptr < lim)
           ++ptr;
@@ -1635,11 +1784,70 @@ begfield (struct line const *line, struc
   return ptr;
 }

+#if HAVE_MBRTOWC
+static char *
+begfield_mb (const struct line *line, const struct keyfield *key)
+{
+  int i;
+  char *ptr = line->text, *lim = ptr + line->length - 1;
+  size_t sword = key->sword;
+  size_t schar = key->schar;
+  size_t mblength;
+  mbstate_t state;
+
+  memset (&state, '\0', sizeof(mbstate_t));
+
+  if (tab_length)
+    while (ptr < lim && sword--)
+      {
+        while (ptr < lim && memcmp (ptr, tab, tab_length) != 0)
+          {
+            GET_BYTELEN_OF_CHAR (lim, ptr, mblength, state);
+            ptr += mblength;
+          }
+        if (ptr < lim)
+          {
+            GET_BYTELEN_OF_CHAR (lim, ptr, mblength, state);
+            ptr += mblength;
+          }
+      }
+  else
+    while (ptr < lim && sword--)
+      {
+        while (ptr < lim && ismbblank (ptr, lim - ptr, &mblength))
+          ptr += mblength;
+        if (ptr < lim)
+          {
+            GET_BYTELEN_OF_CHAR (lim, ptr, mblength, state);
+            ptr += mblength;
+          }
+        while (ptr < lim && !ismbblank (ptr, lim - ptr, &mblength))
+          ptr += mblength;
+      }
+
+  if (key->skipsblanks)
+    while (ptr < lim && ismbblank (ptr, lim - ptr, &mblength))
+      ptr += mblength;
+
+  for (i = 0; i < schar; i++)
+    {
+      GET_BYTELEN_OF_CHAR (lim, ptr, mblength, state);
+
+      if (ptr + mblength > lim)
+        break;
+      else
+        ptr += mblength;
+    }
+
+  return ptr;
+}
+#endif
+
 /* Return the limit of (a pointer to the first character after) the field
    in LINE specified by KEY. */

 static char *
-limfield (struct line const *line, struct keyfield const *key)
+limfield_uni (const struct line *line, const struct keyfield *key)
 {
   char *ptr = line->text, *lim = ptr + line->length - 1;
   size_t eword = key->eword, echar = key->echar;
@@ -1654,10 +1862,10 @@ limfield (struct line const *line, struc
      'beginning' is the first character following the delimiting TAB.
      Otherwise, leave PTR pointing at the first 'blank' character after
      the preceding field.  */
-  if (tab != TAB_DEFAULT)
+  if (tab_length)
     while (ptr < lim && eword--)
       {
-        while (ptr < lim && *ptr != tab)
+        while (ptr < lim && *ptr != tab[0])
           ++ptr;
         if (ptr < lim && (eword || echar))
           ++ptr;
@@ -1703,10 +1911,10 @@ limfield (struct line const *line, struc
      */

   /* Make LIM point to the end of (one byte past) the current field.  */
-  if (tab != TAB_DEFAULT)
+  if (tab_length)
     {
       char *newlim;
-      newlim = memchr (ptr, tab, lim - ptr);
+      newlim = memchr (ptr, tab[0], lim - ptr);
       if (newlim)
         lim = newlim;
     }
@@ -1737,6 +1945,130 @@ limfield (struct line const *line, struc
   return ptr;
 }

+#if HAVE_MBRTOWC
+static char *
+limfield_mb (const struct line *line, const struct keyfield *key)
+{
+  char *ptr = line->text, *lim = ptr + line->length - 1;
+  size_t eword = key->eword, echar = key->echar;
+  int i;
+  size_t mblength;
+  mbstate_t state;
+
+  if (echar == 0)
+    eword++; /* skip all of end field. */
+
+  memset (&state, '\0', sizeof(mbstate_t));
+
+  if (tab_length)
+    while (ptr < lim && eword--)
+      {
+        while (ptr < lim && memcmp (ptr, tab, tab_length) != 0)
+          {
+            GET_BYTELEN_OF_CHAR (lim, ptr, mblength, state);
+            ptr += mblength;
+          }
+        if (ptr < lim && (eword | echar))
+          {
+            GET_BYTELEN_OF_CHAR (lim, ptr, mblength, state);
+            ptr += mblength;
+          }
+      }
+  else
+    while (ptr < lim && eword--)
+      {
+        while (ptr < lim && ismbblank (ptr, lim - ptr, &mblength))
+          ptr += mblength;
+        if (ptr < lim)
+          {
+            GET_BYTELEN_OF_CHAR (lim, ptr, mblength, state);
+            ptr += mblength;
+          }
+        while (ptr < lim && !ismbblank (ptr, lim - ptr, &mblength))
+          ptr += mblength;
+      }
+
+
+# ifdef POSIX_UNSPECIFIED
+  /* Make LIM point to the end of (one byte past) the current field.  */
+  if (tab_length)
+    {
+      char *newlim, *p;
+
+      newlim = NULL;
+      for (p = ptr; p < lim;)
+         {
+          if (memcmp (p, tab, tab_length) == 0)
+            {
+              newlim = p;
+              break;
+            }
+
+          GET_BYTELEN_OF_CHAR (lim, ptr, mblength, state);
+          p += mblength;
+        }
+    }
+  else
+    {
+      char *newlim;
+      newlim = ptr;
+
+      while (newlim < lim && ismbblank (newlim, lim - newlim, &mblength))
+        newlim += mblength;
+      if (ptr < lim)
+        {
+          GET_BYTELEN_OF_CHAR (lim, ptr, mblength, state);
+          ptr += mblength;
+        }
+      while (newlim < lim && !ismbblank (newlim, lim - newlim, &mblength))
+        newlim += mblength;
+      lim = newlim;
+    }
+# endif
+
+  if (echar != 0)
+  {
+    /* If we're skipping leading blanks, don't start counting characters
+     *      until after skipping past any leading blanks.  */
+    if (key->skipeblanks)
+      while (ptr < lim && ismbblank (ptr, lim - ptr, &mblength))
+        ptr += mblength;
+
+    memset (&state, '\0', sizeof(mbstate_t));
+
+    /* Advance PTR by ECHAR (if possible), but no further than LIM.  */
+    for (i = 0; i < echar; i++)
+     {
+        GET_BYTELEN_OF_CHAR (lim, ptr, mblength, state);
+
+        if (ptr + mblength > lim)
+          break;
+        else
+          ptr += mblength;
+      }
+  }
+
+  return ptr;
+}
+#endif
+
+static void
+skipblanks_uni (char **ptr, char *lim)
+{
+  while (*ptr < lim && blanks[to_uchar (**ptr)])
+    ++(*ptr);
+}
+
+#if HAVE_MBRTOWC
+static void
+skipblanks_mb (char **ptr, char *lim)
+{
+  size_t mblength;
+  while (*ptr < lim && ismbblank (*ptr, lim - *ptr, &mblength))
+    (*ptr) += mblength;
+}
+#endif
+
 /* Fill BUF reading from FP, moving buf->left bytes from the end
    of buf->buf to the beginning first.  If EOF is reached and the
    file wasn't terminated by a newline, supply one.  Set up BUF's line
@@ -1823,8 +2155,22 @@ fillbuf (struct buffer *buf, FILE *fp, c
                   else
                     {
                       if (key->skipsblanks)
-                        while (blanks[to_uchar (*line_start)])
-                          line_start++;
+                        {
+#if HAVE_MBRTOWC
+                          if (MB_CUR_MAX > 1)
+                            {
+                              size_t mblength;
+                              while (line_start < line->keylim &&
+                                     ismbblank (line_start,
+                                                line->keylim - line_start,
+                                                &mblength))
+                                line_start += mblength;
+                            }
+                          else
+#endif
+                          while (blanks[to_uchar (*line_start)])
+                            line_start++;
+                        }
                       line->keybeg = line_start;
                     }
                 }
@@ -1958,12 +2304,10 @@ find_unit_order (char const *number)
        <none/unknown> < K/k < M < G < T < P < E < Z < Y  */

 static int
-human_numcompare (char const *a, char const *b)
+human_numcompare (char *a, char *b)
 {
-  while (blanks[to_uchar (*a)])
-    a++;
-  while (blanks[to_uchar (*b)])
-    b++;
+  skipblanks(&a, a + strlen(a));
+  skipblanks(&b, b + strlen(b));

   int diff = find_unit_order (a) - find_unit_order (b);
   return (diff ? diff : strnumcmp (a, b, decimal_point, thousands_sep));
@@ -1974,7 +2318,7 @@ human_numcompare (char const *a, char co
    hideously fast. */

 static int
-numcompare (char const *a, char const *b)
+numcompare_uni (const char *a, const char *b)
 {
   while (blanks[to_uchar (*a)])
     a++;
@@ -1984,6 +2328,25 @@ numcompare (char const *a, char const *b
   return strnumcmp (a, b, decimal_point, thousands_sep);
 }

+#if HAVE_MBRTOWC
+static int
+numcompare_mb (const char *a, const char *b)
+{
+  size_t mblength, len;
+  len = strlen (a); /* okay for UTF-8 */
+  while (*a && ismbblank (a, len > MB_CUR_MAX ? MB_CUR_MAX : len, &mblength))
+    {
+      a += mblength;
+      len -= mblength;
+    }
+  len = strlen (b); /* okay for UTF-8 */
+  while (*b && ismbblank (b, len > MB_CUR_MAX ? MB_CUR_MAX : len, &mblength))
+    b += mblength;
+
+  return strnumcmp (a, b, decimal_point, thousands_sep);
+}
+#endif /* HAV_EMBRTOWC */
+
 /* Work around a problem whereby the long double value returned by glibc's
    strtold ("NaN", ...) contains uninitialized bits: clear all bytes of
    A and B before calling strtold.  FIXME: remove this function once
@@ -2034,7 +2397,7 @@ general_numcompare (char const *sa, char
    Return 0 if the name in S is not recognized.  */

 static int
-getmonth (char const *month, char **ea)
+getmonth_uni (char const *month, size_t len, char **ea)
 {
   size_t lo = 0;
   size_t hi = MONTHS_PER_YEAR;
@@ -2310,15 +2673,14 @@ debug_key (struct line const *line, stru
           char saved = *lim;
           *lim = '\0';

-          while (blanks[to_uchar (*beg)])
-            beg++;
+          skipblanks (&beg, lim);

           char *tighter_lim = beg;

           if (lim < beg)
             tighter_lim = lim;
           else if (key->month)
-            getmonth (beg, &tighter_lim);
+            getmonth (beg, lim-beg, &tighter_lim);
           else if (key->general_numeric)
             ignore_value (strtold (beg, &tighter_lim));
           else if (key->numeric || key->human_numeric)
@@ -2452,7 +2814,7 @@ key_warnings (struct keyfield const *gke
       /* Warn about significant leading blanks.  */
       bool implicit_skip = key_numeric (key) || key->month;
       bool line_offset = key->eword == 0 && key->echar != 0; /* -k1.x,1.y  */
-      if (!zero_width && !gkey_only && tab == TAB_DEFAULT && !line_offset
+      if (!zero_width && !gkey_only && !tab_length && !line_offset
           && ((!key->skipsblanks && !implicit_skip)
               || (!key->skipsblanks && key->schar)
               || (!key->skipeblanks && key->echar)))
@@ -2510,11 +2872,87 @@ key_warnings (struct keyfield const *gke
     error (0, 0, _("option '-r' only applies to last-resort comparison"));
 }

+#if HAVE_MBRTOWC
+static int
+getmonth_mb (const char *s, size_t len, char **ea)
+{
+  char *month;
+  register size_t i;
+  register int lo = 0, hi = MONTHS_PER_YEAR, result;
+  char *tmp;
+  size_t wclength, mblength;
+  const char *pp;
+  const wchar_t *wpp;
+  wchar_t *month_wcs;
+  mbstate_t state;
+
+  while (len > 0 && ismbblank (s, len, &mblength))
+    {
+      s += mblength;
+      len -= mblength;
+    }
+
+  if (len == 0)
+    return 0;
+
+  if (SIZE_MAX - len < 1)
+    xalloc_die ();
+
+  month = (char *) xnmalloc (len + 1, MB_CUR_MAX);
+
+  pp = tmp = (char *) xnmalloc (len + 1, MB_CUR_MAX);
+  memcpy (tmp, s, len);
+  tmp[len] = '\0';
+  wpp = month_wcs = (wchar_t *) xnmalloc (len + 1, sizeof (wchar_t));
+  memset (&state, '\0', sizeof (mbstate_t));
+
+  wclength = mbsrtowcs (month_wcs, &pp, len + 1, &state);
+  if (wclength == (size_t)-1 || pp != NULL)
+    error (SORT_FAILURE, 0, _("Invalid multibyte input %s."), quote(s));
+
+  for (i = 0; i < wclength; i++)
+    {
+      month_wcs[i] = towupper(month_wcs[i]);
+      if (iswblank (month_wcs[i]))
+        {
+          month_wcs[i] = L'\0';
+          break;
+        }
+    }
+
+  mblength = wcsrtombs (month, &wpp, (len + 1) * MB_CUR_MAX, &state);
+  assert (mblength != (-1) && wpp == NULL);
+
+  do
+    {
+      int ix = (lo + hi) / 2;
+
+      if (strncmp (month, monthtab[ix].name, strlen (monthtab[ix].name)) < 0)
+        hi = ix;
+      else
+        lo = ix;
+    }
+  while (hi - lo > 1);
+
+  result = (!strncmp (month, monthtab[lo].name, strlen (monthtab[lo].name))
+      ? monthtab[lo].val : 0);
+
+  if (ea && result)
+     *ea = (char*) s + strlen (monthtab[lo].name);
+
+  free (month);
+  free (tmp);
+  free (month_wcs);
+
+  return result;
+}
+#endif
+
 /* Compare two lines A and B trying every key in sequence until there
    are no more keys or a difference is found. */

 static int
-keycompare (struct line const *a, struct line const *b)
+keycompare_uni (const struct line *a, const struct line *b)
 {
   struct keyfield *key = keylist;

@@ -2599,7 +3037,7 @@ keycompare (struct line const *a, struct
           else if (key->human_numeric)
             diff = human_numcompare (ta, tb);
           else if (key->month)
-            diff = getmonth (ta, NULL) - getmonth (tb, NULL);
+            diff = getmonth (ta, tlena, NULL) - getmonth (tb, tlenb, NULL);
           else if (key->random)
             diff = compare_random (ta, tlena, tb, tlenb);
           else if (key->version)
@@ -2715,6 +3153,211 @@ keycompare (struct line const *a, struct
   return key->reverse ? -diff : diff;
 }

+#if HAVE_MBRTOWC
+static int
+keycompare_mb (const struct line *a, const struct line *b)
+{
+  struct keyfield *key = keylist;
+
+  /* For the first iteration only, the key positions have been
+     precomputed for us. */
+  char *texta = a->keybeg;
+  char *textb = b->keybeg;
+  char *lima = a->keylim;
+  char *limb = b->keylim;
+
+  size_t mblength_a, mblength_b;
+  wchar_t wc_a, wc_b;
+  mbstate_t state_a, state_b;
+
+  int diff = 0;
+
+  memset (&state_a, '\0', sizeof(mbstate_t));
+  memset (&state_b, '\0', sizeof(mbstate_t));
+  /* Ignore keys with start after end.  */
+  if (a->keybeg - a->keylim > 0)
+    return 0;
+
+
+              /* Ignore and/or translate chars before comparing.  */
+# define IGNORE_CHARS(NEW_LEN, LEN, TEXT, COPY, WC, MBLENGTH, STATE)        \
+  do                                                                        \
+    {                                                                        \
+      wchar_t uwc;                                                        \
+      char mbc[MB_LEN_MAX];                                                \
+      mbstate_t state_wc;                                                \
+                                                                        \
+      for (NEW_LEN = i = 0; i < LEN;)                                        \
+        {                                                                \
+          mbstate_t state_bak;                                                \
+                                                                        \
+          state_bak = STATE;                                                \
+          MBLENGTH = mbrtowc (&WC, TEXT + i, LEN - i, &STATE);                \
+                                                                        \
+          if (MBLENGTH == (size_t)-2 || MBLENGTH == (size_t)-1                \
+              || MBLENGTH == 0)                                                \
+            {                                                                \
+              if (MBLENGTH == (size_t)-2 || MBLENGTH == (size_t)-1)        \
+                STATE = state_bak;                                        \
+              if (!ignore)                                                \
+                COPY[NEW_LEN++] = TEXT[i];                                \
+              i++;                                                         \
+              continue;                                                        \
+            }                                                                \
+                                                                        \
+          if (ignore)                                                        \
+            {                                                                \
+              if ((ignore == nonprinting && !iswprint (WC))                \
+                   || (ignore == nondictionary                                \
+                       && !iswalnum (WC) && !iswblank (WC)))                \
+                {                                                        \
+                  i += MBLENGTH;                                        \
+                  continue;                                                \
+                }                                                        \
+            }                                                                \
+                                                                        \
+          if (translate)                                                \
+            {                                                                \
+                                                                        \
+              uwc = towupper(WC);                                        \
+              if (WC == uwc)                                                \
+                {                                                        \
+                  memcpy (mbc, TEXT + i, MBLENGTH);                        \
+                  i += MBLENGTH;                                        \
+                }                                                        \
+              else                                                        \
+                {                                                        \
+                  i += MBLENGTH;                                        \
+                  WC = uwc;                                                \
+                  memset (&state_wc, '\0', sizeof (mbstate_t));                \
+                                                                        \
+                  MBLENGTH = wcrtomb (mbc, WC, &state_wc);                \
+                  assert (MBLENGTH != (size_t)-1 && MBLENGTH != 0);        \
+                }                                                        \
+                                                                        \
+              for (j = 0; j < MBLENGTH; j++)                                \
+                COPY[NEW_LEN++] = mbc[j];                                \
+            }                                                                \
+          else                                                                \
+            for (j = 0; j < MBLENGTH; j++)                                \
+              COPY[NEW_LEN++] = TEXT[i++];                                \
+        }                                                                \
+      COPY[NEW_LEN] = '\0';                                                \
+    }                                                                        \
+  while (0)
+
+      /* Actually compare the fields. */
+
+  for (;;)
+    {
+      /* Find the lengths. */
+      size_t lena = lima <= texta ? 0 : lima - texta;
+      size_t lenb = limb <= textb ? 0 : limb - textb;
+
+      char enda IF_LINT (= 0);
+      char endb IF_LINT (= 0);
+
+      char const *translate = key->translate;
+      bool const *ignore = key->ignore;
+
+      if (ignore || translate)
+        {
+          if (SIZE_MAX - lenb - 2 < lena)
+            xalloc_die ();
+          char *copy_a = (char *) xnmalloc (lena + lenb + 2, MB_CUR_MAX);
+          char *copy_b = copy_a + lena * MB_CUR_MAX + 1;
+          size_t new_len_a, new_len_b;
+          size_t i, j;
+
+          IGNORE_CHARS (new_len_a, lena, texta, copy_a,
+                        wc_a, mblength_a, state_a);
+          IGNORE_CHARS (new_len_b, lenb, textb, copy_b,
+                        wc_b, mblength_b, state_b);
+          texta = copy_a; textb = copy_b;
+          lena = new_len_a; lenb = new_len_b;
+        }
+      else
+        {
+          /* Use the keys in-place, temporarily null-terminated.  */
+          enda = texta[lena]; texta[lena] = '\0';
+          endb = textb[lenb]; textb[lenb] = '\0';
+        }
+
+      if (key->random)
+        diff = compare_random (texta, lena, textb, lenb);
+      else if (key->numeric | key->general_numeric | key->human_numeric)
+        {
+          char savea = *lima, saveb = *limb;
+
+          *lima = *limb = '\0';
+          diff = (key->numeric ? numcompare (texta, textb)
+                  : key->general_numeric ? general_numcompare (texta, textb)
+                  : human_numcompare (texta, textb));
+          *lima = savea, *limb = saveb;
+        }
+      else if (key->version)
+        diff = filevercmp (texta, textb);
+      else if (key->month)
+        diff = getmonth (texta, lena, NULL) - getmonth (textb, lenb, NULL);
+      else if (lena == 0)
+        diff = - NONZERO (lenb);
+      else if (lenb == 0)
+        diff = 1;
+      else if (hard_LC_COLLATE && !folding)
+        {
+          diff = xmemcoll0 (texta, lena + 1, textb, lenb + 1);
+        }
+      else
+        {
+          diff = memcmp (texta, textb, MIN (lena, lenb));
+          if (diff == 0)
+            diff = lena < lenb ? -1 : lena != lenb;
+        }
+
+      if (ignore || translate)
+        free (texta);
+      else
+        {
+          texta[lena] = enda;
+          textb[lenb] = endb;
+        }
+
+      if (diff)
+        goto not_equal;
+
+      key = key->next;
+      if (! key)
+        break;
+
+      /* Find the beginning and limit of the next field.  */
+      if (key->eword != -1)
+        lima = limfield (a, key), limb = limfield (b, key);
+      else
+        lima = a->text + a->length - 1, limb = b->text + b->length - 1;
+
+      if (key->sword != -1)
+        texta = begfield (a, key), textb = begfield (b, key);
+      else
+        {
+          texta = a->text, textb = b->text;
+          if (key->skipsblanks)
+            {
+              while (texta < lima && ismbblank (texta, lima - texta, &mblength_a))
+                texta += mblength_a;
+              while (textb < limb && ismbblank (textb, limb - textb, &mblength_b))
+                textb += mblength_b;
+            }
+        }
+    }
+
+not_equal:
+  if (key && key->reverse)
+    return -diff;
+  else
+    return diff;
+}
+#endif
+
 /* Compare two lines A and B, returning negative, zero, or positive
    depending on whether A compares less than, equal to, or greater than B. */

@@ -2742,7 +3385,7 @@ compare (struct line const *a, struct li
     diff = - NONZERO (blen);
   else if (blen == 0)
     diff = 1;
-  else if (hard_LC_COLLATE)
+  else if (hard_LC_COLLATE && !folding)
     {
       /* Note xmemcoll0 is a performance enhancement as
          it will not unconditionally write '\0' after the
@@ -4139,6 +4782,7 @@ set_ordering (char const *s, struct keyf
           break;
         case 'f':
           key->translate = fold_toupper;
+          folding = true;
           break;
         case 'g':
           key->general_numeric = true;
@@ -4218,7 +4862,7 @@ main (int argc, char **argv)
   initialize_exit_failure (SORT_FAILURE);

   hard_LC_COLLATE = hard_locale (LC_COLLATE);
-#if HAVE_NL_LANGINFO
+#if HAVE_LANGINFO_CODESET
   hard_LC_TIME = hard_locale (LC_TIME);
 #endif

@@ -4239,6 +4883,29 @@ main (int argc, char **argv)
       thousands_sep = -1;
   }

+#if HAVE_MBRTOWC
+  if (MB_CUR_MAX > 1)
+    {
+      inittables = inittables_mb;
+      begfield = begfield_mb;
+      limfield = limfield_mb;
+      skipblanks = skipblanks_mb;
+      getmonth = getmonth_mb;
+      keycompare = keycompare_mb;
+      numcompare = numcompare_mb;
+    }
+  else
+#endif
+    {
+      inittables = inittables_uni;
+      begfield = begfield_uni;
+      limfield = limfield_uni;
+      skipblanks = skipblanks_uni;
+      getmonth = getmonth_uni;
+      keycompare = keycompare_uni;
+      numcompare = numcompare_uni;
+    }
+
   have_read_stdin = false;
   inittables ();

@@ -4513,13 +5180,34 @@ main (int argc, char **argv)

         case 't':
           {
-            char newtab = optarg[0];
-            if (! newtab)
+            char newtab[MB_LEN_MAX + 1];
+            size_t newtab_length = 1;
+            strncpy (newtab, optarg, MB_LEN_MAX);
+            if (! newtab[0])
               die (SORT_FAILURE, 0, _("empty tab"));
-            if (optarg[1])
+#if HAVE_MBRTOWC
+            if (MB_CUR_MAX > 1)
+              {
+                wchar_t wc;
+                mbstate_t state;
+
+                memset (&state, '\0', sizeof (mbstate_t));
+                newtab_length = mbrtowc (&wc, newtab, strnlen (newtab,
+                                                               MB_LEN_MAX),
+                                         &state);
+                switch (newtab_length)
+                  {
+                  case (size_t) -1:
+                  case (size_t) -2:
+                  case 0:
+                    newtab_length = 1;
+                  }
+              }
+#endif
+            if (newtab_length == 1 && optarg[1])
               {
                 if (STREQ (optarg, "\\0"))
-                  newtab = '\0';
+                  newtab[0] = '\0';
                 else
                   {
                     /* Provoke with 'sort -txx'.  Complain about
@@ -4530,9 +5218,11 @@ main (int argc, char **argv)
                          quote (optarg));
                   }
               }
-            if (tab != TAB_DEFAULT && tab != newtab)
+            if (tab_length && (tab_length != newtab_length
+                        || memcmp (tab, newtab, tab_length) != 0))
               die (SORT_FAILURE, 0, _("incompatible tabs"));
-            tab = newtab;
+            memcpy (tab, newtab, newtab_length);
+            tab_length = newtab_length;
           }
           break;

@@ -4770,12 +5460,10 @@ main (int argc, char **argv)
       sort (files, nfiles, outfile, nthreads);
     }

-#ifdef lint
   if (files_from)
     readtokens0_free (&tok);
   else
     free (files);
-#endif

   if (have_read_stdin && fclose (stdin) == EOF)
     sort_die (_("close failed"), "-");
diff -Naurp coreutils-8.26-orig/src/unexpand.c coreutils-8.26/src/unexpand.c
--- coreutils-8.26-orig/src/unexpand.c	2016-11-06 16:15:30.000000000 -0600
+++ coreutils-8.26/src/unexpand.c	2016-12-02 19:15:23.525391058 -0600
@@ -38,6 +38,9 @@
 #include <stdio.h>
 #include <getopt.h>
 #include <sys/types.h>
+
+#include <mbfile.h>
+
 #include "system.h"
 #include "die.h"
 #include "xstrndup.h"
@@ -107,24 +110,47 @@ unexpand (void)
 {
   /* Input stream.  */
   FILE *fp = next_file (NULL);
+  mb_file_t mbf;

   /* The array of pending blanks.  In non-POSIX locales, blanks can
      include characters other than spaces, so the blanks must be
      stored, not merely counted.  */
-  char *pending_blank;
+  mbf_char_t *pending_blank;
+  /* True if the starting locale is utf8.  */
+  bool using_utf_locale;
+
+  /* True if the first file contains BOM header.  */
+  bool found_bom;
+  using_utf_locale=check_utf_locale();

   if (!fp)
     return;
+  mbf_init (mbf, fp);
+  found_bom=check_bom(fp,&mbf);

+  if (using_utf_locale == false && found_bom == true)
+  {
+    /*try using some predefined locale */
+
+    if (set_utf_locale () != 0)
+    {
+      error (EXIT_FAILURE, errno, _("cannot set UTF-8 locale"));
+    }
+  }
   /* The worst case is a non-blank character, then one blank, then a
      tab stop, then MAX_COLUMN_WIDTH - 1 blanks, then a non-blank; so
      allocate MAX_COLUMN_WIDTH bytes to store the blanks.  */
-  pending_blank = xmalloc (max_column_width);
+  pending_blank = xmalloc (max_column_width * sizeof (mbf_char_t));
+
+  if (found_bom == true)
+  {
+    print_bom();
+  }

   while (true)
     {
       /* Input character, or EOF.  */
-      int c;
+      mbf_char_t c;

       /* If true, perform translations.  */
       bool convert = true;
@@ -158,12 +184,44 @@ unexpand (void)

       do
         {
-          while ((c = getc (fp)) < 0 && (fp = next_file (fp)))
-            continue;
+          while (true) {
+            mbf_getc (c, mbf);
+            if ((mb_iseof (c)) && (fp = next_file (fp)))
+              {
+                mbf_init (mbf, fp);
+                if (fp!=NULL)
+                {
+                  if (check_bom(fp,&mbf)==true)
+                  {
+                    /*Not the first file - check BOM header*/
+                    if (using_utf_locale==false && found_bom==false)
+                    {
+                      /*BOM header in subsequent file but not in the first one. */
+                      error (EXIT_FAILURE, errno, _("combination of files with and without BOM header"));
+                    }
+                  }
+                  else
+                  {
+                    if(using_utf_locale==false && found_bom==true)
+                    {
+                      /*First file conatined BOM header - locale was switched to UTF
+                      /*all subsequent files should contain BOM. */
+                      error (EXIT_FAILURE, errno, _("combination of files with and without BOM header"));
+                    }
+                  }
+                }
+                continue;
+              }
+            else
+              {
+                break;
+              }
+            }
+

           if (convert)
             {
-              bool blank = !! isblank (c);
+              bool blank = mb_isblank (c);

               if (blank)
                 {
@@ -180,16 +238,16 @@ unexpand (void)
                       if (next_tab_column < column)
                         die (EXIT_FAILURE, 0, _("input line is too long"));

-                      if (c == '\t')
+                      if (mb_iseq (c, '\t'))
                         {
                           column = next_tab_column;

                           if (pending)
-                            pending_blank[0] = '\t';
+                            mb_setascii (&pending_blank[0], '\t');
                         }
                       else
                         {
-                          column++;
+                          column += mb_width (c);

                           if (! (prev_blank && column == next_tab_column))
                             {
@@ -197,13 +255,14 @@ unexpand (void)
                                  will be replaced by tabs.  */
                               if (column == next_tab_column)
                                 one_blank_before_tab_stop = true;
-                              pending_blank[pending++] = c;
+                              mb_copy (&pending_blank[pending++], &c);
                               prev_blank = true;
                               continue;
                             }

                           /* Replace the pending blanks by a tab or two.  */
-                          pending_blank[0] = c = '\t';
+                          mb_setascii (&c, '\t');
+                          mb_setascii (&pending_blank[0], '\t');
                         }

                       /* Discard pending blanks, unless it was a single
@@ -211,7 +270,7 @@ unexpand (void)
                       pending = one_blank_before_tab_stop;
                     }
                 }
-              else if (c == '\b')
+              else if (mb_iseq (c, '\b'))
                 {
                   /* Go back one column, and force recalculation of the
                      next tab stop.  */
@@ -219,9 +278,9 @@ unexpand (void)
                   next_tab_column = column;
                   tab_index -= !!tab_index;
                 }
-              else
+              else if (!mb_iseq (c, '\n'))
                 {
-                  column++;
+                  column += mb_width (c);
                   if (!column)
                     die (EXIT_FAILURE, 0, _("input line is too long"));
                 }
@@ -229,8 +288,11 @@ unexpand (void)
               if (pending)
                 {
                   if (pending > 1 && one_blank_before_tab_stop)
-                    pending_blank[0] = '\t';
-                  if (fwrite (pending_blank, 1, pending, stdout) != pending)
+                    mb_setascii (&pending_blank[0], '\t');
+
+                  for (int n = 0; n < pending; ++n)
+                    mb_putc (pending_blank[n], stdout);
+                  if (ferror (stdout))
                     die (EXIT_FAILURE, errno, _("write error"));
                   pending = 0;
                   one_blank_before_tab_stop = false;
@@ -240,16 +302,17 @@ unexpand (void)
               convert &= convert_entire_line || blank;
             }

-          if (c < 0)
+          if (mb_iseof (c))
             {
               free (pending_blank);
               return;
             }

-          if (putchar (c) < 0)
+          mb_putc (c, stdout);
+          if (ferror (stdout))
             die (EXIT_FAILURE, errno, _("write error"));
         }
-      while (c != '\n');
+      while (!mb_iseq (c, '\n'));
     }
 }

diff -Naurp coreutils-8.26-orig/src/uniq.c coreutils-8.26/src/uniq.c
--- coreutils-8.26-orig/src/uniq.c	2016-11-06 16:15:30.000000000 -0600
+++ coreutils-8.26/src/uniq.c	2016-12-02 19:15:23.526390974 -0600
@@ -21,6 +21,17 @@
 #include <getopt.h>
 #include <sys/types.h>

+/* Get mbstate_t, mbrtowc(). */
+#if HAVE_WCHAR_H
+# include <wchar.h>
+#endif
+
+/* Get isw* functions. */
+#if HAVE_WCTYPE_H
+# include <wctype.h>
+#endif
+#include <assert.h>
+
 #include "system.h"
 #include "argmatch.h"
 #include "linebuffer.h"
@@ -32,9 +43,21 @@
 #include "stdio--.h"
 #include "xmemcoll.h"
 #include "xstrtol.h"
-#include "memcasecmp.h"
+#include "xmemcoll.h"
 #include "quote.h"

+/* MB_LEN_MAX is incorrectly defined to be 1 in at least one GCC
+   installation; work around this configuration error.  */
+#if !defined MB_LEN_MAX || MB_LEN_MAX < 2
+# define MB_LEN_MAX 16
+#endif
+
+/* Some systems, like BeOS, have multibyte encodings but lack mbstate_t.  */
+#if HAVE_MBRTOWC && defined mbstate_t
+# define mbrtowc(pwc, s, n, ps) (mbrtowc) (pwc, s, n, 0)
+#endif
+
+
 /* The official name of this program (e.g., no 'g' prefix).  */
 #define PROGRAM_NAME "uniq"

@@ -144,6 +167,10 @@ enum
   GROUP_OPTION = CHAR_MAX + 1
 };

+/* Function pointers. */
+static char *
+(*find_field) (struct linebuffer *line);
+
 static struct option const longopts[] =
 {
   {"count", no_argument, NULL, 'c'},
@@ -260,7 +287,7 @@ size_opt (char const *opt, char const *m
    return a pointer to the beginning of the line's field to be compared. */

 static char * _GL_ATTRIBUTE_PURE
-find_field (struct linebuffer const *line)
+find_field_uni (struct linebuffer *line)
 {
   size_t count;
   char const *lp = line->buffer;
@@ -280,6 +307,83 @@ find_field (struct linebuffer const *lin
   return line->buffer + i;
 }

+#if HAVE_MBRTOWC
+
+# define MBCHAR_TO_WCHAR(WC, MBLENGTH, LP, POS, SIZE, STATEP, CONVFAIL)  \
+  do                                                                        \
+    {                                                                        \
+      mbstate_t state_bak;                                                \
+                                                                        \
+      CONVFAIL = 0;                                                        \
+      state_bak = *STATEP;                                                \
+                                                                        \
+      MBLENGTH = mbrtowc (&WC, LP + POS, SIZE - POS, STATEP);                \
+                                                                        \
+      switch (MBLENGTH)                                                        \
+        {                                                                \
+        case (size_t)-2:                                                \
+        case (size_t)-1:                                                \
+          *STATEP = state_bak;                                                \
+          CONVFAIL++;                                                        \
+          /* Fall through */                                                \
+        case 0:                                                                \
+          MBLENGTH = 1;                                                        \
+        }                                                                \
+    }                                                                        \
+  while (0)
+
+static char *
+find_field_multi (struct linebuffer *line)
+{
+  size_t count;
+  char *lp = line->buffer;
+  size_t size = line->length - 1;
+  size_t pos;
+  size_t mblength;
+  wchar_t wc;
+  mbstate_t *statep;
+  int convfail = 0;
+
+  pos = 0;
+  statep = &(line->state);
+
+  /* skip fields. */
+  for (count = 0; count < skip_fields && pos < size; count++)
+    {
+      while (pos < size)
+        {
+          MBCHAR_TO_WCHAR (wc, mblength, lp, pos, size, statep, convfail);
+
+          if (convfail || !(iswblank (wc) || wc == '\n'))
+            {
+              pos += mblength;
+              break;
+            }
+          pos += mblength;
+        }
+
+      while (pos < size)
+        {
+          MBCHAR_TO_WCHAR (wc, mblength, lp, pos, size, statep, convfail);
+
+          if (!convfail && (iswblank (wc) || wc == '\n'))
+            break;
+
+          pos += mblength;
+        }
+    }
+
+  /* skip fields. */
+  for (count = 0; count < skip_chars && pos < size; count++)
+    {
+      MBCHAR_TO_WCHAR (wc, mblength, lp, pos, size, statep, convfail);
+      pos += mblength;
+    }
+
+  return lp + pos;
+}
+#endif
+
 /* Return false if two strings OLD and NEW match, true if not.
    OLD and NEW point not to the beginnings of the lines
    but rather to the beginnings of the fields to compare.
@@ -288,6 +392,8 @@ find_field (struct linebuffer const *lin
 static bool
 different (char *old, char *new, size_t oldlen, size_t newlen)
 {
+  char *copy_old, *copy_new;
+
   if (check_chars < oldlen)
     oldlen = check_chars;
   if (check_chars < newlen)
@@ -295,14 +401,103 @@ different (char *old, char *new, size_t

   if (ignore_case)
     {
-      /* FIXME: This should invoke strcoll somehow.  */
-      return oldlen != newlen || memcasecmp (old, new, oldlen);
+      size_t i;
+
+      copy_old = xmalloc (oldlen + 1);
+      copy_new = xmalloc (oldlen + 1);
+
+      for (i = 0; i < oldlen; i++)
+        {
+          copy_old[i] = toupper (old[i]);
+          copy_new[i] = toupper (new[i]);
+        }
+      bool rc = xmemcoll (copy_old, oldlen, copy_new, newlen);
+      free (copy_old);
+      free (copy_new);
+      return rc;
     }
-  else if (hard_LC_COLLATE)
-    return xmemcoll (old, oldlen, new, newlen) != 0;
   else
-    return oldlen != newlen || memcmp (old, new, oldlen);
+    {
+      copy_old = (char *)old;
+      copy_new = (char *)new;
+    }
+
+  return xmemcoll (copy_old, oldlen, copy_new, newlen);
+
+}
+
+#if HAVE_MBRTOWC
+static int
+different_multi (const char *old, const char *new, size_t oldlen, size_t newlen, mbstate_t oldstate, mbstate_t newstate)
+{
+  size_t i, j, chars;
+  const char *str[2];
+  char *copy[2];
+  size_t len[2];
+  mbstate_t state[2];
+  size_t mblength;
+  wchar_t wc, uwc;
+  mbstate_t state_bak;
+
+  str[0] = old;
+  str[1] = new;
+  len[0] = oldlen;
+  len[1] = newlen;
+  state[0] = oldstate;
+  state[1] = newstate;
+
+  for (i = 0; i < 2; i++)
+    {
+      copy[i] = xmalloc (len[i] + 1);
+      memset (copy[i], '\0', len[i] + 1);
+
+      for (j = 0, chars = 0; j < len[i] && chars < check_chars; chars++)
+        {
+          state_bak = state[i];
+          mblength = mbrtowc (&wc, str[i] + j, len[i] - j, &(state[i]));
+
+          switch (mblength)
+            {
+            case (size_t)-1:
+            case (size_t)-2:
+              state[i] = state_bak;
+              /* Fall through */
+            case 0:
+              mblength = 1;
+              break;
+
+            default:
+              if (ignore_case)
+                {
+                  uwc = towupper (wc);
+
+                  if (uwc != wc)
+                    {
+                      mbstate_t state_wc;
+                      size_t mblen;
+
+                      memset (&state_wc, '\0', sizeof(mbstate_t));
+                      mblen = wcrtomb (copy[i] + j, uwc, &state_wc);
+                      assert (mblen != (size_t)-1);
+                    }
+                  else
+                    memcpy (copy[i] + j, str[i] + j, mblength);
+                }
+              else
+                memcpy (copy[i] + j, str[i] + j, mblength);
+            }
+          j += mblength;
+        }
+      copy[i][j] = '\0';
+      len[i] = j;
+    }
+  int rc = xmemcoll (copy[0], len[0], copy[1], len[1]);
+  free (copy[0]);
+  free (copy[1]);
+  return rc;
+
 }
+#endif

 /* Output the line in linebuffer LINE to standard output
    provided that the switches say it should be output.
@@ -367,19 +562,38 @@ check_file (const char *infile, const ch
       char *prevfield IF_LINT ( = NULL);
       size_t prevlen IF_LINT ( = 0);
       bool first_group_printed = false;
+#if HAVE_MBRTOWC
+      mbstate_t prevstate;
+
+      memset (&prevstate, '\0', sizeof (mbstate_t));
+#endif

       while (!feof (stdin))
         {
           char *thisfield;
           size_t thislen;
           bool new_group;
+#if HAVE_MBRTOWC
+          mbstate_t thisstate;
+#endif

           if (readlinebuffer_delim (thisline, stdin, delimiter) == 0)
             break;

           thisfield = find_field (thisline);
           thislen = thisline->length - 1 - (thisfield - thisline->buffer);
+#if HAVE_MBRTOWC
+          if (MB_CUR_MAX > 1)
+            {
+              thisstate = thisline->state;

+              new_group = (prevline->length == 0
+                           || different_multi (thisfield, prevfield,
+                                               thislen, prevlen,
+                                               thisstate, prevstate));
+            }
+          else
+#endif
           new_group = (prevline->length == 0
                        || different (thisfield, prevfield, thislen, prevlen));

@@ -397,6 +611,10 @@ check_file (const char *infile, const ch
               SWAP_LINES (prevline, thisline);
               prevfield = thisfield;
               prevlen = thislen;
+#if HAVE_MBRTOWC
+              if (MB_CUR_MAX > 1)
+                prevstate = thisstate;
+#endif
               first_group_printed = true;
             }
         }
@@ -409,17 +627,26 @@ check_file (const char *infile, const ch
       size_t prevlen;
       uintmax_t match_count = 0;
       bool first_delimiter = true;
+#if HAVE_MBRTOWC
+      mbstate_t prevstate;
+#endif

       if (readlinebuffer_delim (prevline, stdin, delimiter) == 0)
         goto closefiles;
       prevfield = find_field (prevline);
       prevlen = prevline->length - 1 - (prevfield - prevline->buffer);
+#if HAVE_MBRTOWC
+      prevstate = prevline->state;
+#endif

       while (!feof (stdin))
         {
           bool match;
           char *thisfield;
           size_t thislen;
+#if HAVE_MBRTOWC
+          mbstate_t thisstate = thisline->state;
+#endif
           if (readlinebuffer_delim (thisline, stdin, delimiter) == 0)
             {
               if (ferror (stdin))
@@ -428,6 +655,14 @@ check_file (const char *infile, const ch
             }
           thisfield = find_field (thisline);
           thislen = thisline->length - 1 - (thisfield - thisline->buffer);
+#if HAVE_MBRTOWC
+          if (MB_CUR_MAX > 1)
+            {
+              match = !different_multi (thisfield, prevfield,
+                                thislen, prevlen, thisstate, prevstate);
+            }
+          else
+#endif
           match = !different (thisfield, prevfield, thislen, prevlen);
           match_count += match;

@@ -460,6 +695,9 @@ check_file (const char *infile, const ch
               SWAP_LINES (prevline, thisline);
               prevfield = thisfield;
               prevlen = thislen;
+#if HAVE_MBRTOWC
+              prevstate = thisstate;
+#endif
               if (!match)
                 match_count = 0;
             }
@@ -506,6 +744,19 @@ main (int argc, char **argv)

   atexit (close_stdout);

+#if HAVE_MBRTOWC
+  if (MB_CUR_MAX > 1)
+    {
+      find_field = find_field_multi;
+    }
+  else
+#endif
+    {
+      find_field = find_field_uni;
+    }
+
+
+
   skip_chars = 0;
   skip_fields = 0;
   check_chars = SIZE_MAX;
diff -Naurp coreutils-8.26-orig/tests/expand/mb.sh coreutils-8.26/tests/expand/mb.sh
--- coreutils-8.26-orig/tests/expand/mb.sh	1969-12-31 18:00:00.000000000 -0600
+++ coreutils-8.26/tests/expand/mb.sh	2016-12-02 19:15:23.526390974 -0600
@@ -0,0 +1,183 @@
+#!/bin/sh
+
+# Copyright (C) 2012-2015 Free Software Foundation, Inc.
+
+# This program is free software: you can redistribute it and/or modify
+# it under the terms of the GNU General Public License as published by
+# the Free Software Foundation, either version 3 of the License, or
+# (at your option) any later version.
+
+# This program is distributed in the hope that it will be useful,
+# but WITHOUT ANY WARRANTY; without even the implied warranty of
+# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
+# GNU General Public License for more details.
+
+# You should have received a copy of the GNU General Public License
+# along with this program.  If not, see <http://www.gnu.org/licenses/>.
+
+. "${srcdir=.}/tests/init.sh"; path_prepend_ ./src
+print_ver_ expand
+
+export LC_ALL=en_US.UTF-8
+
+#input containing multibyte characters
+cat <<\EOF > in || framework_failure_
+1234567812345678123456781
+.       .       .       .
+a	b	c	d
+.       .       .       .
+Ã¤	Ã¶	Ã¼	ÃŸ
+.       .       .       .
+EOF
+env printf '   Ã¤Ã¶Ã¼\t.    Ã¶Ã¼Ã¤.   \tÃ¤ xx\n' >> in || framework_failure_
+
+cat <<\EOF > exp || framework_failure_
+1234567812345678123456781
+.       .       .       .
+a       b       c       d
+.       .       .       .
+Ã¤       Ã¶       Ã¼       ÃŸ
+.       .       .       .
+   Ã¤Ã¶Ã¼  .    Ã¶Ã¼Ã¤.       Ã¤ xx
+EOF
+
+expand < in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+#multiple files as an input
+cat <<\EOF >> exp || framework_failure_
+1234567812345678123456781
+.       .       .       .
+a       b       c       d
+.       .       .       .
+Ã¤       Ã¶       Ã¼       ÃŸ
+.       .       .       .
+   Ã¤Ã¶Ã¼  .    Ã¶Ã¼Ã¤.       Ã¤ xx
+EOF
+
+expand ./in ./in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+#test characters with display widths != 1
+env printf '12345678
+e\t|ascii(1)
+\u00E9\t|composed(1)
+e\u0301\t|decomposed(1)
+\u3000\t|ideo-space(2)
+\uFF0D\t|full-hypen(2)
+' > in || framework_failure_
+
+env printf '12345678
+e       |ascii(1)
+\u00E9       |composed(1)
+e\u0301       |decomposed(1)
+\u3000      |ideo-space(2)
+\uFF0D      |full-hypen(2)
+' > exp || framework_failure_
+
+expand < in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+#shouldn't fail with "input line too long"
+#when a line starts with a control character
+env printf '\n' > in || framework_failure_
+
+expand < in > out || fail=1
+compare in out > /dev/null 2>&1 || fail=1
+
+#non-Unicode characters interspersed between Unicode ones
+env printf '12345678
+\t\xFF|
+\xFF\t|
+\t\xFFÃ¤|
+Ã¤\xFF\t|
+\tÃ¤\xFF|
+\xFF\tÃ¤|
+Ã¤bcdef\xFF\t|
+' > in || framework_failure_
+
+env printf '12345678
+        \xFF|
+\xFF       |
+        \xFFÃ¤|
+Ã¤\xFF      |
+        Ã¤\xFF|
+\xFF       Ã¤|
+Ã¤bcdef\xFF |
+' > exp || framework_failure_
+
+expand < in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+
+
+#BOM header test 1
+printf "\xEF\xBB\xBF" > in; cat <<\EOF >> in || framework_failure_
+1234567812345678123456781
+.       .       .       .
+a	b	c	d
+.       .       .       .
+Ã¤	Ã¶	Ã¼	ÃŸ
+.       .       .       .
+EOF
+env printf '   Ã¤Ã¶Ã¼\t.    Ã¶Ã¼Ã¤.   \tÃ¤ xx\n' >> in || framework_failure_
+
+printf "\xEF\xBB\xBF" > exp; cat <<\EOF >> exp || framework_failure_
+1234567812345678123456781
+.       .       .       .
+a       b       c       d
+.       .       .       .
+Ã¤       Ã¶       Ã¼       ÃŸ
+.       .       .       .
+   Ã¤Ã¶Ã¼  .    Ã¶Ã¼Ã¤.       Ã¤ xx
+EOF
+
+
+expand < in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+LANG=C expand < in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+LC_ALL=C expand < in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+
+printf '\xEF\xBB\xBF' > in1; cat <<\EOF >> in1 || framework_failure_
+1234567812345678123456781
+.       .       .       .
+a	b	c	d
+.       .       .       .
+Ã¤	Ã¶	Ã¼	ÃŸ
+.       .       .       .
+EOF
+env printf '   Ã¤Ã¶Ã¼\t.    Ã¶Ã¼Ã¤.   \tÃ¤ xx\n' >> in1 || framework_failure_
+
+
+printf '\xEF\xBB\xBF' > exp; cat <<\EOF >> exp || framework_failure_
+1234567812345678123456781
+.       .       .       .
+a       b       c       d
+.       .       .       .
+Ã¤       Ã¶       Ã¼       ÃŸ
+.       .       .       .
+   Ã¤Ã¶Ã¼  .    Ã¶Ã¼Ã¤.       Ã¤ xx
+1234567812345678123456781
+.       .       .       .
+a       b       c       d
+.       .       .       .
+Ã¤       Ã¶       Ã¼       ÃŸ
+.       .       .       .
+   Ã¤Ã¶Ã¼  .    Ã¶Ã¼Ã¤.       Ã¤ xx
+EOF
+
+expand in1 in1 > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+LANG=C expand in1 in1  > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+LC_ALL=C expand in1 in1 > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+exit $fail
diff -Naurp coreutils-8.26-orig/tests/i18n/sort.sh coreutils-8.26/tests/i18n/sort.sh
--- coreutils-8.26-orig/tests/i18n/sort.sh	1969-12-31 18:00:00.000000000 -0600
+++ coreutils-8.26/tests/i18n/sort.sh	2016-12-02 19:15:23.527390889 -0600
@@ -0,0 +1,29 @@
+#!/bin/sh
+# Verify sort's multi-byte support.
+
+. "${srcdir=.}/tests/init.sh"; path_prepend_ ./src
+print_ver_ sort
+
+export LC_ALL=en_US.UTF-8
+locale -k LC_CTYPE | grep -q "charmap.*UTF-8" \
+  || skip_ "No UTF-8 locale available"
+
+# Enable heap consistency checkng on older systems
+export MALLOC_CHECK_=2
+
+
+# check buffer overflow issue due to
+# expanding multi-byte representation due to case conversion
+# https://bugzilla.suse.com/show_bug.cgi?id=928749
+cat <<EOF > exp
+.
+É‘
+EOF
+cat <<EOF | sort -f > out || fail=1
+.
+É‘
+EOF
+compare exp out || { fail=1; cat out; }
+
+
+Exit $fail
diff -Naurp coreutils-8.26-orig/tests/local.mk coreutils-8.26/tests/local.mk
--- coreutils-8.26-orig/tests/local.mk	2016-11-22 14:04:32.000000000 -0600
+++ coreutils-8.26/tests/local.mk	2016-12-02 19:15:23.527390889 -0600
@@ -350,6 +350,8 @@ all_tests =					\
   tests/misc/sort-discrim.sh			\
   tests/misc/sort-files0-from.pl		\
   tests/misc/sort-float.sh			\
+  tests/misc/sort-mb-tests.sh			\
+  tests/i18n/sort.sh				\
   tests/misc/sort-h-thousands-sep.sh		\
   tests/misc/sort-merge.pl			\
   tests/misc/sort-merge-fdlimit.sh		\
@@ -542,6 +544,7 @@ all_tests =					\
   tests/du/threshold.sh				\
   tests/du/trailing-slash.sh			\
   tests/du/two-args.sh				\
+  tests/expand/mb.sh				\
   tests/id/gnu-zero-uids.sh			\
   tests/id/no-context.sh			\
   tests/id/context.sh				\
@@ -682,6 +685,7 @@ all_tests =					\
   tests/touch/read-only.sh			\
   tests/touch/relative.sh			\
   tests/touch/trailing-slash.sh			\
+  tests/unexpand/mb.sh				\
   $(all_root_tests)

 # See tests/factor/create-test.sh.
diff -Naurp coreutils-8.26-orig/tests/misc/cut.pl coreutils-8.26/tests/misc/cut.pl
--- coreutils-8.26-orig/tests/misc/cut.pl	2016-03-16 07:21:24.000000000 -0500
+++ coreutils-8.26/tests/misc/cut.pl	2016-12-02 19:15:23.527390889 -0600
@@ -23,9 +23,11 @@ use strict;
 # Turn off localization of executable's output.
 @ENV{qw(LANGUAGE LANG LC_ALL)} = ('C') x 3;

-my $mb_locale = $ENV{LOCALE_FR_UTF8};
+my $mb_locale;
+# uncommented enable multibyte paths
+$mb_locale = $ENV{LOCALE_FR_UTF8};
 ! defined $mb_locale || $mb_locale eq 'none'
-  and $mb_locale = 'C';
+ and $mb_locale = 'C';

 my $prog = 'cut';
 my $try = "Try '$prog --help' for more information.\n";
@@ -240,6 +242,7 @@ if ($mb_locale ne 'C')
         my @new_t = @$t;
         my $test_name = shift @new_t;

+        next if ($test_name =~ "newline-[12][0-9]");
         push @new, ["$test_name-mb", @new_t, {ENV => "LC_ALL=$mb_locale"}];
       }
     push @Tests, @new;
diff -Naurp coreutils-8.26-orig/tests/misc/expand.pl coreutils-8.26/tests/misc/expand.pl
--- coreutils-8.26-orig/tests/misc/expand.pl	2016-11-06 16:15:30.000000000 -0600
+++ coreutils-8.26/tests/misc/expand.pl	2016-12-02 19:15:23.528390805 -0600
@@ -27,6 +27,15 @@ my $prog = 'expand';
 # Turn off localization of executable's output.
 @ENV{qw(LANGUAGE LANG LC_ALL)} = ('C') x 3;

+#comment out next line to disable multibyte tests
+my $mb_locale = $ENV{LOCALE_FR_UTF8};
+! defined $mb_locale || $mb_locale eq 'none'
+ and $mb_locale = 'C';
+
+my $prog = 'expand';
+my $try = "Try \`$prog --help' for more information.\n";
+my $inval = "$prog: invalid byte, character or field list\n$try";
+
 my @Tests =
   (
    ['t1', '--tabs=3',     {IN=>"a\tb"}, {OUT=>"a  b"}],
@@ -140,6 +149,8 @@ my @Tests =


    # Test errors
+   # FIXME: The following tests contain â€˜quotingâ€™ specific to LC_MESSAGES
+   # So we force LC_MESSAGES=C to make them pass.
    ['e1', '--tabs="a"', {IN=>''}, {OUT=>''}, {EXIT=>1},
     {ERR => "$prog: tab size contains invalid character(s): 'a'\n"}],
    ['e2', "-t $UINTMAX_OFLOW", {IN=>''}, {OUT=>''}, {EXIT=>1},
@@ -150,6 +161,37 @@ my @Tests =
     {ERR => "$prog: tab sizes must be ascending\n"}],
   );

+if ($mb_locale ne 'C')
+  {
+    # Duplicate each test vector, appending "-mb" to the test name and
+    # inserting {ENV => "LC_ALL=$mb_locale"} in the copy, so that we
+    # provide coverage for the distro-added multi-byte code paths.
+    my @new;
+    foreach my $t (@Tests)
+      {
+        my @new_t = @$t;
+        my $test_name = shift @new_t;
+
+        # Depending on whether expand is multi-byte-patched,
+        # it emits different diagnostics:
+        #   non-MB: invalid byte or field list
+        #   MB:     invalid byte, character or field list
+        # Adjust the expected error output accordingly.
+        if (grep {ref $_ eq 'HASH' && exists $_->{ERR} && $_->{ERR} eq $inval}
+            (@new_t))
+          {
+            my $sub = {ERR_SUBST => 's/, character//'};
+            push @new_t, $sub;
+            push @$t, $sub;
+          }
+        push @new, ["$test_name-mb", @new_t, {ENV => "LANG=$mb_locale LC_MESSAGES=C"}];
+      }
+    push @Tests, @new;
+  }
+
+
+@Tests = triple_test \@Tests;
+
 my $save_temps = $ENV{DEBUG};
 my $verbose = $ENV{VERBOSE};

diff -Naurp coreutils-8.26-orig/tests/misc/fold.pl coreutils-8.26/tests/misc/fold.pl
--- coreutils-8.26-orig/tests/misc/fold.pl	2016-03-16 07:21:24.000000000 -0500
+++ coreutils-8.26/tests/misc/fold.pl	2016-12-02 19:15:23.528390805 -0600
@@ -20,9 +20,18 @@ use strict;

 (my $program_name = $0) =~ s|.*/||;

+my $prog = 'fold';
+my $try = "Try \`$prog --help' for more information.\n";
+my $inval = "$prog: invalid byte, character or field list\n$try";
+
 # Turn off localization of executable's output.
 @ENV{qw(LANGUAGE LANG LC_ALL)} = ('C') x 3;

+# uncommented to enable multibyte paths
+my $mb_locale = $ENV{LOCALE_FR_UTF8};
+! defined $mb_locale || $mb_locale eq 'none'
+ and $mb_locale = 'C';
+
 my @Tests =
   (
    ['s1', '-w2 -s', {IN=>"a\t"}, {OUT=>"a\n\t"}],
@@ -31,9 +40,48 @@ my @Tests =
    ['s4', '-w4 -s', {IN=>"abc ef\n"}, {OUT=>"abc \nef\n"}],
   );

+# Add _POSIX2_VERSION=199209 to the environment of each test
+# that uses an old-style option like +1.
+if ($mb_locale ne 'C')
+  {
+    # Duplicate each test vector, appending "-mb" to the test name and
+    # inserting {ENV => "LC_ALL=$mb_locale"} in the copy, so that we
+    # provide coverage for the distro-added multi-byte code paths.
+    my @new;
+    foreach my $t (@Tests)
+      {
+        my @new_t = @$t;
+        my $test_name = shift @new_t;
+
+        # Depending on whether fold is multi-byte-patched,
+        # it emits different diagnostics:
+        #   non-MB: invalid byte or field list
+        #   MB:     invalid byte, character or field list
+        # Adjust the expected error output accordingly.
+        if (grep {ref $_ eq 'HASH' && exists $_->{ERR} && $_->{ERR} eq $inval}
+            (@new_t))
+          {
+            my $sub = {ERR_SUBST => 's/, character//'};
+            push @new_t, $sub;
+            push @$t, $sub;
+          }
+        push @new, ["$test_name-mb", @new_t, {ENV => "LC_ALL=$mb_locale"}];
+      }
+    push @Tests, @new;
+  }
+
+@Tests = triple_test \@Tests;
+
+# Remember that triple_test creates from each test with exactly one "IN"
+# file two more tests (.p and .r suffix on name) corresponding to reading
+# input from a file and from a pipe.  The pipe-reading test would fail
+# due to a race condition about 1 in 20 times.
+# Remove the IN_PIPE version of the "output-is-input" test above.
+# The others aren't susceptible because they have three inputs each.
+@Tests = grep {$_->[0] ne 'output-is-input.p'} @Tests;
+
 my $save_temps = $ENV{DEBUG};
 my $verbose = $ENV{VERBOSE};

-my $prog = 'fold';
 my $fail = run_tests ($program_name, $prog, \@Tests, $save_temps, $verbose);
 exit $fail;
diff -Naurp coreutils-8.26-orig/tests/misc/join.pl coreutils-8.26/tests/misc/join.pl
--- coreutils-8.26-orig/tests/misc/join.pl	2016-03-16 07:21:24.000000000 -0500
+++ coreutils-8.26/tests/misc/join.pl	2016-12-02 19:15:23.528390805 -0600
@@ -25,6 +25,15 @@ my $limits = getlimits ();

 my $prog = 'join';

+my $try = "Try \`$prog --help' for more information.\n";
+my $inval = "$prog: invalid byte, character or field list\n$try";
+
+my $mb_locale;
+#Comment out next line to disable multibyte tests
+$mb_locale = $ENV{LOCALE_FR_UTF8};
+! defined $mb_locale || $mb_locale eq 'none'
+  and $mb_locale = 'C';
+
 my $delim = chr 0247;
 sub t_subst ($)
 {
@@ -329,8 +338,49 @@ foreach my $t (@tv)
     push @Tests, $new_ent;
   }

+# Add _POSIX2_VERSION=199209 to the environment of each test
+# that uses an old-style option like +1.
+if ($mb_locale ne 'C')
+  {
+    # Duplicate each test vector, appending "-mb" to the test name and
+    # inserting {ENV => "LC_ALL=$mb_locale"} in the copy, so that we
+    # provide coverage for the distro-added multi-byte code paths.
+    my @new;
+    foreach my $t (@Tests)
+      {
+        my @new_t = @$t;
+        my $test_name = shift @new_t;
+
+        # Depending on whether join is multi-byte-patched,
+        # it emits different diagnostics:
+        #   non-MB: invalid byte or field list
+        #   MB:     invalid byte, character or field list
+        # Adjust the expected error output accordingly.
+        if (grep {ref $_ eq 'HASH' && exists $_->{ERR} && $_->{ERR} eq $inval}
+            (@new_t))
+          {
+            my $sub = {ERR_SUBST => 's/, character//'};
+            push @new_t, $sub;
+            push @$t, $sub;
+          }
+        #Adjust the output some error messages including test_name for mb
+        if (grep {ref $_ eq 'HASH' && exists $_->{ERR}}
+             (@new_t))
+          {
+            my $sub2 = {ERR_SUBST => "s/$test_name-mb/$test_name/"};
+            push @new_t, $sub2;
+            push @$t, $sub2;
+          }
+        push @new, ["$test_name-mb", @new_t, {ENV => "LC_ALL=$mb_locale"}];
+      }
+    push @Tests, @new;
+  }
+
 @Tests = triple_test \@Tests;

+#skip invalid-j-mb test, it is failing because of the format
+@Tests = grep {$_->[0] ne 'invalid-j-mb'} @Tests;
+
 my $save_temps = $ENV{DEBUG};
 my $verbose = $ENV{VERBOSE};

diff -Naurp coreutils-8.26-orig/tests/misc/sort-mb-tests.sh coreutils-8.26/tests/misc/sort-mb-tests.sh
--- coreutils-8.26-orig/tests/misc/sort-mb-tests.sh	1969-12-31 18:00:00.000000000 -0600
+++ coreutils-8.26/tests/misc/sort-mb-tests.sh	2016-12-02 19:15:23.528390805 -0600
@@ -0,0 +1,45 @@
+#!/bin/sh
+# Verify sort's multi-byte support.
+
+. "${srcdir=.}/tests/init.sh"; path_prepend_ ./src
+print_ver_ sort
+
+export LC_ALL=en_US.UTF-8
+locale -k LC_CTYPE | grep -q "charmap.*UTF-8" \
+  || skip_ "No UTF-8 locale available"
+
+
+cat <<EOF > exp
+Bananaï¼ 5
+Appleï¼ 10
+Citrusï¼ 20
+Cherryï¼ 30
+EOF
+
+cat <<EOF | sort -t ï¼  -k2 -n > out || fail=1
+Appleï¼ 10
+Bananaï¼ 5
+Citrusï¼ 20
+Cherryï¼ 30
+EOF
+
+compare exp out || { fail=1; cat out; }
+
+
+cat <<EOF > exp
+Citrusï¼ ï¼¡ï¼¡20ï¼ ï¼ 5
+Cherryï¼ ï¼¡ï¼¡30ï¼ ï¼ 10
+Appleï¼ ï¼¡ï¼¡10ï¼ ï¼ 20
+Bananaï¼ ï¼¡ï¼¡5ï¼ ï¼ 30
+EOF
+
+cat <<EOF | sort -t ï¼  -k4 -n > out || fail=1
+Appleï¼ ï¼¡ï¼¡10ï¼ ï¼ 20
+Bananaï¼ ï¼¡ï¼¡5ï¼ ï¼ 30
+Citrusï¼ ï¼¡ï¼¡20ï¼ ï¼ 5
+Cherryï¼ ï¼¡ï¼¡30ï¼ ï¼ 10
+EOF
+
+compare exp out || { fail=1; cat out; }
+
+Exit $fail
diff -Naurp coreutils-8.26-orig/tests/misc/sort-merge.pl coreutils-8.26/tests/misc/sort-merge.pl
--- coreutils-8.26-orig/tests/misc/sort-merge.pl	2016-03-16 07:21:24.000000000 -0500
+++ coreutils-8.26/tests/misc/sort-merge.pl	2016-12-02 19:15:23.529390720 -0600
@@ -26,6 +26,15 @@ my $prog = 'sort';
 # Turn off localization of executable's output.
 @ENV{qw(LANGUAGE LANG LC_ALL)} = ('C') x 3;

+my $mb_locale;
+# uncommented according to upstream commit enabling multibyte paths
+$mb_locale = $ENV{LOCALE_FR_UTF8};
+! defined $mb_locale || $mb_locale eq 'none'
+ and $mb_locale = 'C';
+
+my $try = "Try \`$prog --help' for more information.\n";
+my $inval = "$prog: invalid byte, character or field list\n$try";
+
 # three empty files and one that says 'foo'
 my @inputs = (+(map{{IN=> {"empty$_"=> ''}}}1..3), {IN=> {foo=> "foo\n"}});

@@ -77,6 +86,39 @@ my @Tests =
         {OUT=>$big_input}],
     );

+# Add _POSIX2_VERSION=199209 to the environment of each test
+# that uses an old-style option like +1.
+if ($mb_locale ne 'C')
+  {
+    # Duplicate each test vector, appending "-mb" to the test name and
+    # inserting {ENV => "LC_ALL=$mb_locale"} in the copy, so that we
+    # provide coverage for the distro-added multi-byte code paths.
+    my @new;
+    foreach my $t (@Tests)
+      {
+        my @new_t = @$t;
+        my $test_name = shift @new_t;
+
+        # Depending on whether sort is multi-byte-patched,
+        # it emits different diagnostics:
+        #   non-MB: invalid byte or field list
+        #   MB:     invalid byte, character or field list
+        # Adjust the expected error output accordingly.
+        if (grep {ref $_ eq 'HASH' && exists $_->{ERR} && $_->{ERR} eq $inval}
+            (@new_t))
+          {
+            my $sub = {ERR_SUBST => 's/, character//'};
+            push @new_t, $sub;
+            push @$t, $sub;
+          }
+        next if ($test_name =~ "nmerge-.");
+        push @new, ["$test_name-mb", @new_t, {ENV => "LC_ALL=$mb_locale"}];
+      }
+    push @Tests, @new;
+  }
+
+@Tests = triple_test \@Tests;
+
 my $save_temps = $ENV{DEBUG};
 my $verbose = $ENV{VERBOSE};

diff -Naurp coreutils-8.26-orig/tests/misc/sort.pl coreutils-8.26/tests/misc/sort.pl
--- coreutils-8.26-orig/tests/misc/sort.pl	2016-03-16 07:21:24.000000000 -0500
+++ coreutils-8.26/tests/misc/sort.pl	2016-12-02 19:15:23.529390720 -0600
@@ -24,10 +24,15 @@ my $prog = 'sort';
 # Turn off localization of executable's output.
 @ENV{qw(LANGUAGE LANG LC_ALL)} = ('C') x 3;

-my $mb_locale = $ENV{LOCALE_FR_UTF8};
+my $mb_locale;
+#Comment out next line to disable multibyte tests
+$mb_locale = $ENV{LOCALE_FR_UTF8};
 ! defined $mb_locale || $mb_locale eq 'none'
   and $mb_locale = 'C';

+my $try = "Try \`$prog --help' for more information.\n";
+my $inval = "$prog: invalid byte, character or field list\n$try";
+
 # Since each test is run with a file name and with redirected stdin,
 # the name in the diagnostic is either the file name or "-".
 # Normalize each diagnostic to use '-'.
@@ -424,6 +429,38 @@ foreach my $t (@Tests)
       }
   }

+if ($mb_locale ne 'C')
+   {
+    # Duplicate each test vector, appending "-mb" to the test name and
+    # inserting {ENV => "LC_ALL=$mb_locale"} in the copy, so that we
+    # provide coverage for the distro-added multi-byte code paths.
+    my @new;
+    foreach my $t (@Tests)
+       {
+        my @new_t = @$t;
+        my $test_name = shift @new_t;
+
+        # Depending on whether sort is multi-byte-patched,
+        # it emits different diagnostics:
+        #   non-MB: invalid byte or field list
+        #   MB:     invalid byte, character or field list
+        # Adjust the expected error output accordingly.
+        if (grep {ref $_ eq 'HASH' && exists $_->{ERR} && $_->{ERR} eq $inval}
+            (@new_t))
+          {
+            my $sub = {ERR_SUBST => 's/, character//'};
+            push @new_t, $sub;
+            push @$t, $sub;
+          }
+        #disable several failing tests until investigation, disable all tests with envvars set
+        next if (grep {ref $_ eq 'HASH' && exists $_->{ENV}} (@new_t));
+        next if ($test_name =~ "18g" or $test_name =~ "sort-numeric" or $test_name =~ "08[ab]" or $test_name =~ "03[def]" or $test_name =~ "h4" or $test_name =~ "n1" or $test_name =~ "2[01]a");
+        next if ($test_name =~ "11[ab]"); # avoid FP: expected result differs to MB result due to collation rules.
+        push @new, ["$test_name-mb", @new_t, {ENV => "LC_ALL=$mb_locale"}];
+       }
+    push @Tests, @new;
+   }
+
 @Tests = triple_test \@Tests;

 # Remember that triple_test creates from each test with exactly one "IN"
@@ -433,6 +470,7 @@ foreach my $t (@Tests)
 # Remove the IN_PIPE version of the "output-is-input" test above.
 # The others aren't susceptible because they have three inputs each.
 @Tests = grep {$_->[0] ne 'output-is-input.p'} @Tests;
+@Tests = grep {$_->[0] ne 'output-is-input-mb.p'} @Tests;

 my $save_temps = $ENV{DEBUG};
 my $verbose = $ENV{VERBOSE};
diff -Naurp coreutils-8.26-orig/tests/misc/unexpand.pl coreutils-8.26/tests/misc/unexpand.pl
--- coreutils-8.26-orig/tests/misc/unexpand.pl	2016-11-06 16:15:30.000000000 -0600
+++ coreutils-8.26/tests/misc/unexpand.pl	2016-12-02 19:15:23.530390636 -0600
@@ -27,6 +27,14 @@ my $limits = getlimits ();

 my $prog = 'unexpand';

+# comment out next line to disable multibyte tests
+my $mb_locale = $ENV{LOCALE_FR_UTF8};
+! defined $mb_locale || $mb_locale eq 'none'
+ and $mb_locale = 'C';
+
+my $try = "Try \`$prog --help' for more information.\n";
+my $inval = "$prog: invalid byte, character or field list\n$try";
+
 my @Tests =
     (
      ['a1', {IN=> ' 'x 1 ."y\n"}, {OUT=> ' 'x 1 ."y\n"}],
@@ -128,6 +136,37 @@ my @Tests =
      ['ts2', '-t5,8', {IN=>"x\t \t y\n"},    {OUT=>"x\t\t y\n"}],
     );

+if ($mb_locale ne 'C')
+  {
+    # Duplicate each test vector, appending "-mb" to the test name and
+    # inserting {ENV => "LC_ALL=$mb_locale"} in the copy, so that we
+    # provide coverage for the distro-added multi-byte code paths.
+    my @new;
+    foreach my $t (@Tests)
+      {
+        my @new_t = @$t;
+        my $test_name = shift @new_t;
+
+        # Depending on whether unexpand is multi-byte-patched,
+        # it emits different diagnostics:
+        #   non-MB: invalid byte or field list
+        #   MB:     invalid byte, character or field list
+        # Adjust the expected error output accordingly.
+        if (grep {ref $_ eq 'HASH' && exists $_->{ERR} && $_->{ERR} eq $inval}
+            (@new_t))
+          {
+            my $sub = {ERR_SUBST => 's/, character//'};
+            push @new_t, $sub;
+            push @$t, $sub;
+          }
+        next if ($test_name =~ 'b-1');
+        push @new, ["$test_name-mb", @new_t, {ENV => "LC_ALL=$mb_locale"}];
+      }
+    push @Tests, @new;
+  }
+
+@Tests = triple_test \@Tests;
+
 my $save_temps = $ENV{DEBUG};
 my $verbose = $ENV{VERBOSE};

diff -Naurp coreutils-8.26-orig/tests/misc/uniq.pl coreutils-8.26/tests/misc/uniq.pl
--- coreutils-8.26-orig/tests/misc/uniq.pl	2016-03-16 07:21:24.000000000 -0500
+++ coreutils-8.26/tests/misc/uniq.pl	2016-12-02 19:15:23.530390636 -0600
@@ -23,9 +23,17 @@ my $limits = getlimits ();
 my $prog = 'uniq';
 my $try = "Try '$prog --help' for more information.\n";

+my $inval = "$prog: invalid byte, character or field list\n$try";
+
 # Turn off localization of executable's output.
 @ENV{qw(LANGUAGE LANG LC_ALL)} = ('C') x 3;

+my $mb_locale;
+#Comment out next line to disable multibyte tests
+$mb_locale = $ENV{LOCALE_FR_UTF8};
+! defined $mb_locale || $mb_locale eq 'none'
+  and $mb_locale = 'C';
+
 # When possible, create a "-z"-testing variant of each test.
 sub add_z_variants($)
 {
@@ -262,6 +270,53 @@ foreach my $t (@Tests)
       and push @$t, {ENV=>'_POSIX2_VERSION=199209'};
   }

+if ($mb_locale ne 'C')
+  {
+    # Duplicate each test vector, appending "-mb" to the test name and
+    # inserting {ENV => "LC_ALL=$mb_locale"} in the copy, so that we
+    # provide coverage for the distro-added multi-byte code paths.
+    my @new;
+    foreach my $t (@Tests)
+      {
+        my @new_t = @$t;
+        my $test_name = shift @new_t;
+
+        # Depending on whether uniq is multi-byte-patched,
+        # it emits different diagnostics:
+        #   non-MB: invalid byte or field list
+        #   MB:     invalid byte, character or field list
+        # Adjust the expected error output accordingly.
+        if (grep {ref $_ eq 'HASH' && exists $_->{ERR} && $_->{ERR} eq $inval}
+            (@new_t))
+          {
+            my $sub = {ERR_SUBST => 's/, character//'};
+            push @new_t, $sub;
+            push @$t, $sub;
+          }
+        # In test #145, replace the each â€˜...â€™ by '...'.
+        if ($test_name =~ "145")
+          {
+            my $sub = { ERR_SUBST => "s/â€˜([^â€™]+)â€™/'\$1'/g"};
+            push @new_t, $sub;
+            push @$t, $sub;
+          }
+        next if (   $test_name =~ "schar"
+                 or $test_name =~ "^obs-plus"
+                 or $test_name =~ "119");
+        push @new, ["$test_name-mb", @new_t, {ENV => "LC_ALL=$mb_locale"}];
+      }
+    push @Tests, @new;
+   }
+
+# Remember that triple_test creates from each test with exactly one "IN"
+# file two more tests (.p and .r suffix on name) corresponding to reading
+# input from a file and from a pipe.  The pipe-reading test would fail
+# due to a race condition about 1 in 20 times.
+# Remove the IN_PIPE version of the "output-is-input" test above.
+# The others aren't susceptible because they have three inputs each.
+
+@Tests = grep {$_->[0] ne 'output-is-input.p'} @Tests;
+
 @Tests = add_z_variants \@Tests;
 @Tests = triple_test \@Tests;

diff -Naurp coreutils-8.26-orig/tests/pr/pr-tests.pl coreutils-8.26/tests/pr/pr-tests.pl
--- coreutils-8.26-orig/tests/pr/pr-tests.pl	2016-11-25 08:01:44.000000000 -0600
+++ coreutils-8.26/tests/pr/pr-tests.pl	2016-12-02 19:15:23.530390636 -0600
@@ -24,6 +24,15 @@ use strict;
 my $prog = 'pr';
 my $normalize_strerror = "s/': .*/'/";

+my $mb_locale;
+#Uncomment the following line to enable multibyte tests
+$mb_locale = $ENV{LOCALE_FR_UTF8};
+! defined $mb_locale || $mb_locale eq 'none'
+  and $mb_locale = 'C';
+
+my $try = "Try \`$prog --help' for more information.\n";
+my $inval = "$prog: invalid byte, character or field list\n$try";
+
 my @tv = (

 # -b option is no longer an official option. But it's still working to
@@ -474,8 +483,48 @@ push @Tests,
     {IN=>{2=>"a\n"}},
      {OUT=>"a\t\t\t\t  \t\t\ta\n"} ];

+# Add _POSIX2_VERSION=199209 to the environment of each test
+# that uses an old-style option like +1.
+if ($mb_locale ne 'C')
+  {
+    # Duplicate each test vector, appending "-mb" to the test name and
+    # inserting {ENV => "LC_ALL=$mb_locale"} in the copy, so that we
+    # provide coverage for the distro-added multi-byte code paths.
+    my @new;
+    foreach my $t (@Tests)
+      {
+        my @new_t = @$t;
+        my $test_name = shift @new_t;
+
+        # Depending on whether pr is multi-byte-patched,
+        # it emits different diagnostics:
+        #   non-MB: invalid byte or field list
+        #   MB:     invalid byte, character or field list
+        # Adjust the expected error output accordingly.
+        if (grep {ref $_ eq 'HASH' && exists $_->{ERR} && $_->{ERR} eq $inval}
+            (@new_t))
+          {
+            my $sub = {ERR_SUBST => 's/, character//'};
+            push @new_t, $sub;
+            push @$t, $sub;
+          }
+        #temporarily skip some failing tests
+        next if ($test_name =~ "col-0" or $test_name =~ "col-inval" or $test_name =~ "asan1");
+        push @new, ["$test_name-mb", @new_t, {ENV => "LC_ALL=$mb_locale"}];
+      }
+    push @Tests, @new;
+  }
+
 @Tests = triple_test \@Tests;

+# Remember that triple_test creates from each test with exactly one "IN"
+# file two more tests (.p and .r suffix on name) corresponding to reading
+# input from a file and from a pipe.  The pipe-reading test would fail
+# due to a race condition about 1 in 20 times.
+# Remove the IN_PIPE version of the "output-is-input" test above.
+# The others aren't susceptible because they have three inputs each.
+@Tests = grep {$_->[0] ne 'output-is-input.p'} @Tests;
+
 my $save_temps = $ENV{DEBUG};
 my $verbose = $ENV{VERBOSE};

diff -Naurp coreutils-8.26-orig/tests/unexpand/mb.sh coreutils-8.26/tests/unexpand/mb.sh
--- coreutils-8.26-orig/tests/unexpand/mb.sh	1969-12-31 18:00:00.000000000 -0600
+++ coreutils-8.26/tests/unexpand/mb.sh	2016-12-02 19:15:23.531390552 -0600
@@ -0,0 +1,172 @@
+#!/bin/sh
+
+# Copyright (C) 2012-2015 Free Software Foundation, Inc.
+
+# This program is free software: you can redistribute it and/or modify
+# it under the terms of the GNU General Public License as published by
+# the Free Software Foundation, either version 3 of the License, or
+# (at your option) any later version.
+
+# This program is distributed in the hope that it will be useful,
+# but WITHOUT ANY WARRANTY; without even the implied warranty of
+# MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
+# GNU General Public License for more details.
+
+# You should have received a copy of the GNU General Public License
+# along with this program.  If not, see <http://www.gnu.org/licenses/>.
+
+. "${srcdir=.}/tests/init.sh"; path_prepend_ ./src
+print_ver_ unexpand
+
+export LC_ALL=en_US.UTF-8
+
+#input containing multibyte characters
+cat > in <<\EOF
+1234567812345678123456781
+.       .       .       .
+a       b       c       d
+.       .       .       .
+Ã¤       Ã¶       Ã¼       ÃŸ
+.       .       .       .
+   Ã¤Ã¶Ã¼  .    Ã¶Ã¼Ã¤.       Ã¤ xx
+EOF
+
+cat > exp <<\EOF
+1234567812345678123456781
+.	.	.	.
+a	b	c	d
+.	.	.	.
+Ã¤	Ã¶	Ã¼	ÃŸ
+.	.	.	.
+   Ã¤Ã¶Ã¼	.    Ã¶Ã¼Ã¤.	Ã¤ xx
+EOF
+
+unexpand -a < in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+
+#multiple files as an input
+cat >> exp <<\EOF
+1234567812345678123456781
+.	.	.	.
+a	b	c	d
+.	.	.	.
+Ã¤	Ã¶	Ã¼	ÃŸ
+.	.	.	.
+   Ã¤Ã¶Ã¼	.    Ã¶Ã¼Ã¤.	Ã¤ xx
+EOF
+
+
+unexpand -a ./in ./in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+#test characters with a display width larger than 1
+
+env printf '12345678
+e       |ascii(1)
+\u00E9       |composed(1)
+e\u0301       |decomposed(1)
+\u3000      |ideo-space(2)
+\uFF0D      |full-hypen(2)
+' > in || framework_failure_
+
+env printf '12345678
+e\t|ascii(1)
+\u00E9\t|composed(1)
+e\u0301\t|decomposed(1)
+\u3000\t|ideo-space(2)
+\uFF0D\t|full-hypen(2)
+' > exp || framework_failure_
+
+unexpand -a < in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+#test input where a blank of width > 1 is not being substituted
+in="$(LC_ALL=en_US.UTF-8 printf ' \u3000  Ã¶       Ã¼       ÃŸ')"
+exp=' ã€€  Ã¶	     Ã¼	     ÃŸ'
+
+unexpand -a < in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+#non-Unicode characters interspersed between Unicode ones
+env printf '12345678
+        \xFF|
+\xFF       |
+        \xFFÃ¤|
+Ã¤\xFF      |
+        Ã¤\xFF|
+\xFF       Ã¤|
+Ã¤bcdef\xFF |
+' > in || framework_failure_
+
+env printf '12345678
+\t\xFF|
+\xFF\t|
+\t\xFFÃ¤|
+Ã¤\xFF\t|
+\tÃ¤\xFF|
+\xFF\tÃ¤|
+Ã¤bcdef\xFF\t|
+' > exp || framework_failure_
+
+unexpand -a < in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+#BOM header test 1
+printf "\xEF\xBB\xBF" > in; cat <<\EOF >> in || framework_failure_
+1234567812345678123456781
+.       .       .       .
+a       b       c       d
+.       .       .       .
+Ã¤       Ã¶       Ã¼       ÃŸ
+.       .       .       .
+   Ã¤Ã¶Ã¼  .    Ã¶Ã¼Ã¤.       Ã¤ xx
+EOF
+env printf '   Ã¤Ã¶Ã¼\t.    Ã¶Ã¼Ã¤.   \tÃ¤ xx\n' >> in || framework_failure_
+
+printf "\xEF\xBB\xBF" > exp; cat <<\EOF >> exp || framework_failure_
+1234567812345678123456781
+.	.	.	.
+a	b	c	d
+.	.	.	.
+Ã¤	Ã¶	Ã¼	ÃŸ
+.	.	.	.
+   Ã¤Ã¶Ã¼	.    Ã¶Ã¼Ã¤.	Ã¤ xx
+EOF
+
+unexpand < in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+LANG=C unexpand < in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+LC_ALL=C unexpand < in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+
+printf "\xEF\xBB\xBF" > exp; cat <<\EOF >> exp || framework_failure_
+1234567812345678123456781
+.	.	.	.
+a	b	c	d
+.	.	.	.
+Ã¤	Ã¶	Ã¼	ÃŸ
+.	.	.	.
+   Ã¤Ã¶Ã¼	.    Ã¶Ã¼Ã¤.	Ã¤ xx
+1234567812345678123456781
+.	.	.	.
+a	b	c	d
+.	.	.	.
+Ã¤	Ã¶	Ã¼	ÃŸ
+.	.	.	.
+   Ã¤Ã¶Ã¼	.    Ã¶Ã¼Ã¤.	Ã¤ xx
+EOF
+
+
+unexpand in in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+LANG=C unexpand in in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
+
+LC_ALL=C unexpand in in > out || fail=1
+compare exp out > /dev/null 2>&1 || fail=1
'''
        self.apply_patch(self.directory, text)
