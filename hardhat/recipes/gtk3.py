import os
from .base import GnuRecipe
from hardhat.util import patch


class Gtk3Recipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(Gtk3Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'e7e3aaf54a54dd1c1ca0588939254abe' \
                      '31329e0bcd280a12290d5306b41ea03f'

        self.name = 'gtk3'
        self.version = '3.20.4'
        short_version = '.'.join(self.version.split('.')[:2])
        self.depends = ['atk', 'atk-bridge', 'gdk-pixbuf', 'glib',
                        'libepoxy', 'libxkbcommon', 'pango',
                        'wayland', 'wayland-protocols',
                        'xorg-libs']
        self.url = 'http://ftp.gnome.org/pub/gnome/sources/gtk+/' \
                   '%s/gtk+-$version.tar.xz' % (short_version)
        self.configure_args += ['--with-x',
                                '--enable-xkb',
                                '--enable-xrandr',
                                '--enable-wayland-backend',
                                '--enable-x11-backend']

    def patch(self):
        self.log_dir('patch', self.directory, 'disable pk-gtk-module')

        src = 'g_str_equal (name, "atk-bridge"))'
        dst = 'g_str_equal (name, "pk-gtk-module") ||\n' \
              '      g_str_equal (name, "atk-bridge"))'

        filename = os.path.join(self.directory, 'gtk', 'gtkmodules.c')
        patch(filename, src, dst)

        text = r'''
@@ -, +, @@
 gtk/gtkiconhelper.c | 9 ++++++++-
 1 file changed, 8 insertions(+), 1 deletion(-)
--- a/gtk/gtkiconhelper.c
+++ a/gtk/gtkiconhelper.c
@@ -896,7 +896,14 @@ _gtk_icon_helper_draw (GtkIconHelper *self,

   if (self->priv->rendered_surface != NULL)
     {
-      gtk_css_style_render_icon_surface (gtk_css_node_get_style (gtk_css_gadget_get_node (GTK_CSS_GADGET (self))),
+      GtkCssNode *node;
+
+      /* Avoid calling gtk_css_node_get_style() because it can
+       * invalidate the style which we don't want while trying
+       * to render the current style.
+       */
+      node = gtk_css_gadget_get_node (GTK_CSS_GADGET (self));
+      gtk_css_style_render_icon_surface (node->style,
                                          cr,
                                          self->priv->rendered_surface,
                                          x, y);
'''
        self.apply_patch(self.directory, text)
