import os
from .base import PythonGnuRecipe
from hardhat.util import patch


class PyGObjectRecipe(PythonGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PyGObjectRecipe, self).__init__(*args, **kwargs)

        self.depends = ['glib', 'gobject-introspection', 'gtk3']
        self.pydepends = ['pycairo']
        self.name = 'pygobject'
        # versions with an odd minor version number (second number) are
        # developmental versions and may show deprecation warnings
        # for instance in 'ipython --pylab'
        self.version = '3.20.1'
        short_version = '.'.join(self.version.split('.')[:2])
        self.sha256 = '3d261005d6fed6a92ac4c25f28379255' \
                      '2f7dad865d1b7e0c03c2b84c04dbd745'

        self.url = 'http://ftp.gnome.org/pub/GNOME/sources/$name/' \
                   '%s/$name-$version.tar.xz' % short_version

    def configure(self):
        self.configure_args += ['--with-python=%s' % self.python]
        super(PyGObjectRecipe, self).configure()


class PyGObject2Recipe(PythonGnuRecipe):
    def __init__(self, *args, **kwargs):
        super(PyGObject2Recipe, self).__init__(*args, **kwargs)
        self.sha256 = 'fb8a1d4f665130a125011659bd347c73' \
                      '39c944232163dbb9a34fd0686577adb8'
        self.pythons = ['python2']
        self.depends = ['glib', 'gobject-introspection', 'gtk3']
        self.pydepends = ['pycairo']
        self.name = 'pygobject2'
        # versions with an odd minor version number (second number) are
        # developmental versions and may show deprecation warnings
        # for instance in 'ipython --pylab'
        self.version = '2.28.6'
        self.url = 'http://ftp.gnome.org/pub/GNOME/sources/pygobject/' \
                   '%s/pygobject-$version.tar.xz' % self.short_version

    def configure(self):
        self.configure_args += ['--with-python=%s' % self.python]
        super(PyGObject2Recipe, self).configure()

    def patch(self):
        text = r'''
Submitted By:            Andrew Benton <andy at benton dot eu dot com> (gobject-introspection) and Armin K. <krejzi at email dot com>, after thomas kaedin (git)
Date:                    2012-03-29 (gobject-introspection) and 2014-03-04 (git)
Initial Package Version: 2.28.6
Upstream Status:         not submitted (gobject-introspection) and committed (git)
Origin:                  Andrew Benton (gobject-introspection) and upstream (git)
Description:             Fixes compiling with recent versions of gobject-introspection; and upstream fixes

diff -Naur pygobject-2.28.6.orig/configure.ac pygobject-2.28.6/configure.ac
--- pygobject-2.28.6.orig/configure.ac	2011-06-13 13:33:56.000000000 -0300
+++ pygobject-2.28.6/configure.ac	2014-03-04 18:36:07.947079909 -0300
@@ -85,7 +85,7 @@
 AM_PROG_CC_STDC
 AM_PROG_CC_C_O

-# check that we have the minimum version of python necisary to build
+# check that we have the minimum version of python necessary to build
 JD_PATH_PYTHON(python_min_ver)

 # check if we are building for python 3
@@ -236,7 +236,7 @@
 AC_ARG_ENABLE(introspection,
   AC_HELP_STRING([--enable-introspection], [Use introspection information]),
   enable_introspection=$enableval,
-  enable_introspection=yes)
+  enable_introspection=no)
 if test "$enable_introspection" != no; then
     AC_DEFINE(ENABLE_INTROSPECTION,1,Use introspection information)
     PKG_CHECK_MODULES(GI,
@@ -262,6 +262,9 @@
 AC_SUBST(INTROSPECTION_SCANNER)
 AC_SUBST(INTROSPECTION_COMPILER)

+dnl Do not install codegen for Python 3.
+AM_CONDITIONAL(ENABLE_CODEGEN, test $build_py3k = false)
+
 dnl add required cflags ...
 if test "x$GCC" = "xyes"; then
   JH_ADD_CFLAG([-Wall])
@@ -281,8 +284,6 @@
   Makefile
   pygobject-2.0.pc
   pygobject-2.0-uninstalled.pc
-  codegen/Makefile
-  codegen/pygobject-codegen-2.0
   docs/Makefile
   docs/reference/entities.docbook
   docs/xsl/fixxref.py
@@ -295,6 +296,13 @@
   examples/Makefile
   tests/Makefile
   PKG-INFO)
+
+if test $build_py3k = false; then
+  AC_CONFIG_FILES(
+    codegen/Makefile
+    codegen/pygobject-codegen-2.0)
+fi
+
 AC_OUTPUT

 echo
diff -Naur pygobject-2.28.6.orig/gi/module.py pygobject-2.28.6/gi/module.py
--- pygobject-2.28.6.orig/gi/module.py	2011-06-13 13:30:25.000000000 -0300
+++ pygobject-2.28.6/gi/module.py	2014-03-04 18:36:07.947079909 -0300
@@ -24,7 +24,11 @@

 import os
 import gobject
-import string
+try:
+    maketrans = ''.maketrans
+except AttributeError:
+    # fallback for Python 2
+    from string import maketrans

 import gi
 from .overrides import registry
diff -Naur pygobject-2.28.6.orig/gi/overrides/Gtk.py pygobject-2.28.6/gi/overrides/Gtk.py
--- pygobject-2.28.6.orig/gi/overrides/Gtk.py	2011-06-13 13:33:49.000000000 -0300
+++ pygobject-2.28.6/gi/overrides/Gtk.py	2014-03-04 18:36:07.949079863 -0300
@@ -35,6 +35,18 @@
 Gtk = modules['Gtk']._introspection_module
 __all__ = []

+if Gtk._version == '2.0':
+    import warnings
+    warn_msg = "You have imported the Gtk 2.0 module.  Because Gtk 2.0 \
+was not designed for use with introspection some of the \
+interfaces and API will fail.  As such this is not supported \
+by the pygobject development team and we encourage you to \
+port your app to Gtk 3 or greater. PyGTK is the recomended \
+python module to use with Gtk 2.0"
+
+    warnings.warn(warn_msg, RuntimeWarning)
+
+
 class Widget(Gtk.Widget):

     def translate_coordinates(self, dest_widget, src_x, src_y):
@@ -401,16 +413,22 @@
     def __init__(self,
                  parent=None,
                  flags=0,
-                 type=Gtk.MessageType.INFO,
+                 message_type=Gtk.MessageType.INFO,
                  buttons=Gtk.ButtonsType.NONE,
                  message_format=None,
                  **kwds):

         if message_format != None:
             kwds['text'] = message_format
+
+        if 'type' in kwds:
+            import warnings
+            warnings.warn("The use of the keyword type as a parameter of the Gtk.MessageDialog constructor has been depricated. Please use message_type instead.", DeprecationWarning)
+            message_type = kwds['type']
+
         Gtk.MessageDialog.__init__(self,
                                    _buttons_property=buttons,
-                                   message_type=type,
+                                   message_type=message_type,
                                    **kwds)
         Dialog.__init__(self, parent=parent, flags=flags)

@@ -619,12 +637,18 @@
     def forward_search(self, string, flags, limit):
         success, match_start, match_end = super(TextIter, self).forward_search(string,
             flags, limit)
-        return (match_start, match_end,)
+        if success:
+            return (match_start, match_end)
+        else:
+            return None

     def backward_search(self, string, flags, limit):
         success, match_start, match_end = super(TextIter, self).backward_search(string,
             flags, limit)
-        return (match_start, match_end,)
+        if success:
+            return (match_start, match_end)
+        else:
+            return None

     def begins_tag(self, tag=None):
         return super(TextIter, self).begins_tag(tag)
diff -Naur pygobject-2.28.6.orig/gi/pygi-foreign-cairo.c pygobject-2.28.6/gi/pygi-foreign-cairo.c
--- pygobject-2.28.6.orig/gi/pygi-foreign-cairo.c	2011-06-13 13:33:49.000000000 -0300
+++ pygobject-2.28.6/gi/pygi-foreign-cairo.c	2014-03-04 18:36:07.949079863 -0300
@@ -30,7 +30,7 @@
 #include <pycairo/py3cairo.h>
 #endif

-Pycairo_CAPI_t *Pycairo_CAPI;
+static Pycairo_CAPI_t *Pycairo_CAPI;

 #include "pygi-foreign.h"

@@ -114,10 +114,15 @@
     Py_RETURN_NONE;
 }

-static PyMethodDef _gi_cairo_functions[] = {};
+static PyMethodDef _gi_cairo_functions[] = {0,};
 PYGLIB_MODULE_START(_gi_cairo, "_gi_cairo")
 {
+#if PY_VERSION_HEX < 0x03000000
     Pycairo_IMPORT;
+#else
+    Pycairo_CAPI = (Pycairo_CAPI_t*) PyCObject_Import("cairo", "CAPI");
+#endif
+
     if (Pycairo_CAPI == NULL)
         return PYGLIB_MODULE_ERROR_RETURN;

diff -Naur pygobject-2.28.6.orig/gi/pygi-info.c pygobject-2.28.6/gi/pygi-info.c
--- pygobject-2.28.6.orig/gi/pygi-info.c	2011-06-13 13:30:25.000000000 -0300
+++ pygobject-2.28.6/gi/pygi-info.c	2014-03-04 18:35:32.473899924 -0300
@@ -162,9 +162,6 @@
         case GI_INFO_TYPE_CONSTANT:
             type = &PyGIConstantInfo_Type;
             break;
-        case GI_INFO_TYPE_ERROR_DOMAIN:
-            type = &PyGIErrorDomainInfo_Type;
-            break;
         case GI_INFO_TYPE_UNION:
             type = &PyGIUnionInfo_Type;
             break;
@@ -481,7 +478,6 @@
                 case GI_INFO_TYPE_INVALID:
                 case GI_INFO_TYPE_FUNCTION:
                 case GI_INFO_TYPE_CONSTANT:
-                case GI_INFO_TYPE_ERROR_DOMAIN:
                 case GI_INFO_TYPE_VALUE:
                 case GI_INFO_TYPE_SIGNAL:
                 case GI_INFO_TYPE_PROPERTY:
@@ -860,7 +856,6 @@
                     case GI_INFO_TYPE_INVALID:
                     case GI_INFO_TYPE_FUNCTION:
                     case GI_INFO_TYPE_CONSTANT:
-                    case GI_INFO_TYPE_ERROR_DOMAIN:
                     case GI_INFO_TYPE_VALUE:
                     case GI_INFO_TYPE_SIGNAL:
                     case GI_INFO_TYPE_PROPERTY:
diff -Naur pygobject-2.28.6.orig/gio/gio-types.defs pygobject-2.28.6/gio/gio-types.defs
--- pygobject-2.28.6.orig/gio/gio-types.defs	2011-06-13 13:33:49.000000000 -0300
+++ pygobject-2.28.6/gio/gio-types.defs	2014-03-04 18:36:07.950079840 -0300
@@ -526,7 +526,7 @@
   )
 )

-(define-enum MountMountFlags
+(define-flags MountMountFlags
   (in-module "gio")
   (c-name "GMountMountFlags")
   (gtype-id "G_TYPE_MOUNT_MOUNT_FLAGS")
@@ -545,7 +545,7 @@
   )
 )

-(define-enum DriveStartFlags
+(define-flags DriveStartFlags
   (in-module "gio")
   (c-name "GDriveStartFlags")
   (gtype-id "G_TYPE_DRIVE_START_FLAGS")
@@ -770,7 +770,7 @@
   )
 )

-(define-enum SocketMsgFlags
+(define-flags SocketMsgFlags
   (in-module "gio")
   (c-name "GSocketMsgFlags")
   (gtype-id "G_TYPE_SOCKET_MSG_FLAGS")
diff -Naur pygobject-2.28.6.orig/gobject/gobjectmodule.c pygobject-2.28.6/gobject/gobjectmodule.c
--- pygobject-2.28.6.orig/gobject/gobjectmodule.c	2011-06-13 13:33:49.000000000 -0300
+++ pygobject-2.28.6/gobject/gobjectmodule.c	2014-03-04 18:36:07.952079793 -0300
@@ -312,13 +312,6 @@
     pyglib_gil_state_release(state);
 }

-static void
-pyg_object_class_init(GObjectClass *class, PyObject *py_class)
-{
-    class->set_property = pyg_object_set_property;
-    class->get_property = pyg_object_get_property;
-}
-
 typedef struct _PyGSignalAccumulatorData {
     PyObject *callable;
     PyObject *user_data;
@@ -484,15 +477,14 @@
 }

 static PyObject *
-add_signals (GType instance_type, PyObject *signals)
+add_signals (GObjectClass *klass, PyObject *signals)
 {
     gboolean ret = TRUE;
-    GObjectClass *oclass;
     Py_ssize_t pos = 0;
     PyObject *key, *value, *overridden_signals = NULL;
+    GType instance_type = G_OBJECT_CLASS_TYPE (klass);

     overridden_signals = PyDict_New();
-    oclass = g_type_class_ref(instance_type);
     while (PyDict_Next(signals, &pos, &key, &value)) {
 	const gchar *signal_name;
         gchar *signal_name_canon, *c;
@@ -530,7 +522,6 @@
 	if (!ret)
 	    break;
     }
-    g_type_class_unref(oclass);
     if (ret)
         return overridden_signals;
     else {
@@ -800,14 +791,12 @@
 }

 static gboolean
-add_properties (GType instance_type, PyObject *properties)
+add_properties (GObjectClass *klass, PyObject *properties)
 {
     gboolean ret = TRUE;
-    GObjectClass *oclass;
     Py_ssize_t pos = 0;
     PyObject *key, *value;

-    oclass = g_type_class_ref(instance_type);
     while (PyDict_Next(properties, &pos, &key, &value)) {
 	const gchar *prop_name;
 	GType prop_type;
@@ -873,7 +862,7 @@
 	Py_DECREF(slice);

 	if (pspec) {
-	    g_object_class_install_property(oclass, 1, pspec);
+	    g_object_class_install_property(klass, 1, pspec);
 	} else {
             PyObject *type, *value, *traceback;
 	    ret = FALSE;
@@ -883,7 +872,7 @@
                 g_snprintf(msg, 256,
 			   "%s (while registering property '%s' for GType '%s')",
                PYGLIB_PyUnicode_AsString(value),
-			   prop_name, g_type_name(instance_type));
+			   prop_name, G_OBJECT_CLASS_NAME(klass));
                 Py_DECREF(value);
                 value = PYGLIB_PyUnicode_FromString(msg);
             }
@@ -892,11 +881,63 @@
 	}
     }

-    g_type_class_unref(oclass);
     return ret;
 }

 static void
+pyg_object_class_init(GObjectClass *class, PyObject *py_class)
+{
+    PyObject *gproperties, *gsignals, *overridden_signals;
+    PyObject *class_dict = ((PyTypeObject*) py_class)->tp_dict;
+
+    class->set_property = pyg_object_set_property;
+    class->get_property = pyg_object_get_property;
+
+    /* install signals */
+    /* we look this up in the instance dictionary, so we don't
+     * accidentally get a parent type's __gsignals__ attribute. */
+    gsignals = PyDict_GetItemString(class_dict, "__gsignals__");
+    if (gsignals) {
+	if (!PyDict_Check(gsignals)) {
+	    PyErr_SetString(PyExc_TypeError,
+			    "__gsignals__ attribute not a dict!");
+	    return;
+	}
+	if (!(overridden_signals = add_signals(class, gsignals))) {
+	    return;
+	}
+        if (PyDict_SetItemString(class_dict, "__gsignals__",
+				 overridden_signals)) {
+            return;
+        }
+        Py_DECREF(overridden_signals);
+
+        PyDict_DelItemString(class_dict, "__gsignals__");
+    } else {
+	PyErr_Clear();
+    }
+
+    /* install properties */
+    /* we look this up in the instance dictionary, so we don't
+     * accidentally get a parent type's __gproperties__ attribute. */
+    gproperties = PyDict_GetItemString(class_dict, "__gproperties__");
+    if (gproperties) {
+	if (!PyDict_Check(gproperties)) {
+	    PyErr_SetString(PyExc_TypeError,
+			    "__gproperties__ attribute not a dict!");
+	    return;
+	}
+	if (!add_properties(class, gproperties)) {
+	    return;
+	}
+	PyDict_DelItemString(class_dict, "__gproperties__");
+	/* Borrowed reference. Py_DECREF(gproperties); */
+    } else {
+	PyErr_Clear();
+    }
+}
+
+static void
 pyg_register_class_init(GType gtype, PyGClassInitFunc class_init)
 {
     GSList *list;
@@ -1068,7 +1109,7 @@
  */
 static void
 pyg_type_add_interfaces(PyTypeObject *class, GType instance_type,
-                        PyObject *bases, gboolean new_interfaces,
+                        PyObject *bases,
                         GType *parent_interfaces, guint n_parent_interfaces)
 {
     int i;
@@ -1082,7 +1123,6 @@
         guint k;
         PyObject *base = PyTuple_GET_ITEM(bases, i);
         GType itype;
-        gboolean is_new = TRUE;
         const GInterfaceInfo *iinfo;
         GInterfaceInfo iinfo_copy;

@@ -1099,16 +1139,6 @@
         if (!G_TYPE_IS_INTERFACE(itype))
             continue;

-        for (k = 0; k < n_parent_interfaces; ++k) {
-            if (parent_interfaces[k] == itype) {
-                is_new = FALSE;
-                break;
-            }
-        }
-
-        if ((new_interfaces && !is_new) || (!new_interfaces && is_new))
-            continue;
-
         iinfo = pyg_lookup_interface_info(itype);
         if (!iinfo) {
             gchar *error;
@@ -1129,7 +1159,7 @@
 int
 pyg_type_register(PyTypeObject *class, const char *type_name)
 {
-    PyObject *gtype, *gsignals, *gproperties, *overridden_signals;
+    PyObject *gtype;
     GType parent_type, instance_type;
     GType *parent_interfaces;
     guint n_parent_interfaces;
@@ -1216,88 +1246,22 @@
     }

     /*
-     * Note: Interfaces to be implemented are searched twice.  First
-     * we register interfaces that are already implemented by a parent
-     * type.  The second time, the remaining interfaces are
-     * registered, i.e. the ones that are not implemented by a parent
-     * type.  In between these two loops, properties and signals are
-     * registered.  It has to be done this way, in two steps,
-     * otherwise glib will complain.  If registering all interfaces
-     * always before properties, you get an error like:
-     *
-     *    ../gobject:121: Warning: Object class
-     *    test_interface+MyObject doesn't implement property
-     *    'some-property' from interface 'TestInterface'
-     *
-     * If, on the other hand, you register interfaces after
-     * registering the properties, you get something like:
-     *
-     *     ../gobject:121: Warning: cannot add interface type
-     *    `TestInterface' to type `test_interface+MyUnknown', since
-     *    type `test_interface+MyUnknown' already conforms to
-     *    interface
-     *
-     * This looks like a GLib quirk, but no bug has been filed
-     * upstream.  However we have a unit test for this particular
-     * problem, which can be found in test_interfaces.py, class
-     * TestInterfaceImpl.
+     * Note, all interfaces need to be registered before the first
+     * g_type_class_ref(), see bug #686149.
      *
      * See also comment above pyg_type_add_interfaces().
      */
-    pyg_type_add_interfaces(class, instance_type, class->tp_bases, FALSE,
+    pyg_type_add_interfaces(class, instance_type, class->tp_bases,
                             parent_interfaces, n_parent_interfaces);

-    /* we look this up in the instance dictionary, so we don't
-     * accidentally get a parent type's __gsignals__ attribute. */
-    gsignals = PyDict_GetItemString(class->tp_dict, "__gsignals__");
-    if (gsignals) {
-	if (!PyDict_Check(gsignals)) {
-	    PyErr_SetString(PyExc_TypeError,
-			    "__gsignals__ attribute not a dict!");
-            g_free(parent_interfaces);
-	    return -1;
-	}
-	if (!(overridden_signals = add_signals(instance_type, gsignals))) {
-            g_free(parent_interfaces);
-	    return -1;
-	}
-        if (PyDict_SetItemString(class->tp_dict, "__gsignals__",
-				 overridden_signals)) {
-            g_free(parent_interfaces);
-            return -1;
-        }
-        Py_DECREF(overridden_signals);
-    } else {
-	PyErr_Clear();
-    }

-    /* we look this up in the instance dictionary, so we don't
-     * accidentally get a parent type's __gsignals__ attribute. */
-    gproperties = PyDict_GetItemString(class->tp_dict, "__gproperties__");
-    if (gproperties) {
-	if (!PyDict_Check(gproperties)) {
-	    PyErr_SetString(PyExc_TypeError,
-			    "__gproperties__ attribute not a dict!");
-            g_free(parent_interfaces);
-	    return -1;
-	}
-	if (!add_properties(instance_type, gproperties)) {
-            g_free(parent_interfaces);
-	    return -1;
-	}
-	PyDict_DelItemString(class->tp_dict, "__gproperties__");
-	/* Borrowed reference. Py_DECREF(gproperties); */
-    } else {
-	PyErr_Clear();
+    gclass = g_type_class_ref(instance_type);
+    if (PyErr_Occurred() != NULL) {
+        g_type_class_unref(gclass);
+        g_free(parent_interfaces);
+        return -1;
     }

-    /* Register new interfaces, that are _not_ already defined by
-     * the parent type.  FIXME: See above.
-     */
-    pyg_type_add_interfaces(class, instance_type, class->tp_bases, TRUE,
-                            parent_interfaces, n_parent_interfaces);
-
-    gclass = g_type_class_ref(instance_type);
     if (pyg_run_class_init(instance_type, gclass, class)) {
         g_type_class_unref(gclass);
         g_free(parent_interfaces);
@@ -1306,9 +1270,8 @@
     g_type_class_unref(gclass);
     g_free(parent_interfaces);

-    if (gsignals)
-        PyDict_DelItemString(class->tp_dict, "__gsignals__");
-
+    if (PyErr_Occurred() != NULL)
+        return -1;
     return 0;
 }

diff -Naur pygobject-2.28.6.orig/gobject/propertyhelper.py pygobject-2.28.6/gobject/propertyhelper.py
--- pygobject-2.28.6.orig/gobject/propertyhelper.py	2011-06-13 13:30:25.000000000 -0300
+++ pygobject-2.28.6/gobject/propertyhelper.py	2014-03-04 18:36:07.953079770 -0300
@@ -188,14 +188,16 @@
             return TYPE_STRING
         elif type_ == object:
             return TYPE_PYOBJECT
-        elif isinstance(type_, type) and issubclass(type_, _gobject.GObject):
+        elif (isinstance(type_, type) and
+              issubclass(type_, (_gobject.GObject,
+                                 _gobject.GEnum))):
             return type_.__gtype__
         elif type_ in [TYPE_NONE, TYPE_INTERFACE, TYPE_CHAR, TYPE_UCHAR,
-                      TYPE_INT, TYPE_UINT, TYPE_BOOLEAN, TYPE_LONG,
-                      TYPE_ULONG, TYPE_INT64, TYPE_UINT64, TYPE_ENUM,
-                      TYPE_FLAGS, TYPE_FLOAT, TYPE_DOUBLE, TYPE_POINTER,
-                      TYPE_BOXED, TYPE_PARAM, TYPE_OBJECT, TYPE_STRING,
-                      TYPE_PYOBJECT]:
+                       TYPE_INT, TYPE_UINT, TYPE_BOOLEAN, TYPE_LONG,
+                       TYPE_ULONG, TYPE_INT64, TYPE_UINT64,
+                       TYPE_FLOAT, TYPE_DOUBLE, TYPE_POINTER,
+                       TYPE_BOXED, TYPE_PARAM, TYPE_OBJECT, TYPE_STRING,
+                       TYPE_PYOBJECT]:
             return type_
         else:
             raise TypeError("Unsupported type: %r" % (type_,))
@@ -224,6 +226,12 @@
         elif ptype == TYPE_PYOBJECT:
             if default is not None:
                 raise TypeError("object types does not have default values")
+        elif gobject.type_is_a(ptype, TYPE_ENUM):
+            if default is None:
+                raise TypeError("enum properties needs a default value")
+            elif not gobject.type_is_a(default, ptype):
+                raise TypeError("enum value %s must be an instance of %r" %
+                                (default, ptype))

     def _get_minimum(self):
         ptype = self.type
@@ -291,7 +299,8 @@
         if ptype in [TYPE_INT, TYPE_UINT, TYPE_LONG, TYPE_ULONG,
                      TYPE_INT64, TYPE_UINT64, TYPE_FLOAT, TYPE_DOUBLE]:
             args = self._get_minimum(), self._get_maximum(), self.default
-        elif ptype == TYPE_STRING or ptype == TYPE_BOOLEAN:
+        elif (ptype == TYPE_STRING or ptype == TYPE_BOOLEAN or
+              ptype.is_a(TYPE_ENUM)):
             args = (self.default,)
         elif ptype == TYPE_PYOBJECT:
             args = ()
diff -Naur pygobject-2.28.6.orig/gobject/pygobject.c pygobject-2.28.6/gobject/pygobject.c
--- pygobject-2.28.6.orig/gobject/pygobject.c	2011-06-13 13:33:49.000000000 -0300
+++ pygobject-2.28.6/gobject/pygobject.c	2014-03-04 18:36:07.954079747 -0300
@@ -991,7 +991,9 @@
 PyObject *
 pygobject_new_sunk(GObject *obj)
 {
-    g_object_set_qdata (obj, pygobject_ref_sunk_key, GINT_TO_POINTER (1));
+    if (obj)
+       g_object_set_qdata (obj, pygobject_ref_sunk_key, GINT_TO_POINTER (1));
+
     return pygobject_new_full(obj, TRUE, NULL);
 }

diff -Naur pygobject-2.28.6.orig/Makefile.am pygobject-2.28.6/Makefile.am
--- pygobject-2.28.6.orig/Makefile.am	2011-06-13 13:33:49.000000000 -0300
+++ pygobject-2.28.6/Makefile.am	2014-03-04 18:36:07.954079747 -0300
@@ -1,7 +1,11 @@
 ACLOCAL_AMFLAGS = -I m4
 AUTOMAKE_OPTIONS = 1.7

-SUBDIRS = docs codegen glib gobject gio examples
+SUBDIRS = docs glib gobject gio examples
+
+if ENABLE_CODEGEN
+SUBDIRS += codegen
+endif

 if ENABLE_INTROSPECTION
 SUBDIRS += gi
diff -Naur pygobject-2.28.6.orig/tests/Makefile.am pygobject-2.28.6/tests/Makefile.am
--- pygobject-2.28.6.orig/tests/Makefile.am	2011-06-13 13:33:49.000000000 -0300
+++ pygobject-2.28.6/tests/Makefile.am	2014-03-04 18:36:07.955079724 -0300
@@ -104,6 +104,7 @@
 	test-floating.h \
 	test-thread.h \
 	test-unknown.h \
+	te_ST@nouppera \
 	org.gnome.test.gschema.xml

 EXTRA_DIST += $(TEST_FILES_STATIC) $(TEST_FILES_GI) $(TEST_FILES_GIO)
diff -Naur pygobject-2.28.6.orig/tests/test_gdbus.py pygobject-2.28.6/tests/test_gdbus.py
--- pygobject-2.28.6.orig/tests/test_gdbus.py	2011-06-13 13:33:49.000000000 -0300
+++ pygobject-2.28.6/tests/test_gdbus.py	2014-03-04 18:36:07.956079701 -0300
@@ -67,8 +67,10 @@

     def test_native_calls_async(self):
         def call_done(obj, result, user_data):
-            user_data['result'] = obj.call_finish(result)
-            user_data['main_loop'].quit()
+            try:
+                user_data['result'] = obj.call_finish(result)
+            finally:
+                user_data['main_loop'].quit()

         main_loop = gobject.MainLoop()
         data = {'main_loop': main_loop}
diff -Naur pygobject-2.28.6.orig/tests/test_properties.py pygobject-2.28.6/tests/test_properties.py
--- pygobject-2.28.6.orig/tests/test_properties.py	2011-06-13 13:30:25.000000000 -0300
+++ pygobject-2.28.6/tests/test_properties.py	2014-03-04 18:36:07.956079701 -0300
@@ -14,6 +14,8 @@
      G_MININT, G_MAXINT, G_MAXUINT, G_MINLONG, G_MAXLONG, \
      G_MAXULONG

+from gi.repository import Gio
+
 if sys.version_info < (3, 0):
     TEST_UTF8 = "\xe2\x99\xa5"
     UNICODE_UTF8 = unicode(TEST_UTF8, 'UTF-8')
@@ -34,6 +36,9 @@
     uint64 = gobject.property(
         type=TYPE_UINT64, flags=PARAM_READWRITE|PARAM_CONSTRUCT)

+    enum = gobject.property(
+        type=Gio.SocketType, default=Gio.SocketType.STREAM)
+
 class TestProperties(unittest.TestCase):
     def testGetSet(self):
         obj = PropertyObject()
@@ -61,8 +66,9 @@
                 self.failUnless(pspec.name in ['normal',
                                                'construct',
                                                'construct-only',
-                                               'uint64'])
-            self.assertEqual(len(obj), 4)
+                                               'uint64',
+                                               'enum'])
+            self.assertEqual(len(obj), 5)

     def testNormal(self):
         obj = new(PropertyObject, normal="123")
@@ -127,6 +133,34 @@
             (etype, ex) = sys.exc_info()[2:]
             self.fail(str(ex))

+    def testEnum(self):
+        obj = new(PropertyObject)
+        self.assertEqual(obj.props.enum, Gio.SocketType.STREAM)
+        self.assertEqual(obj.enum, Gio.SocketType.STREAM)
+        obj.enum = Gio.SocketType.DATAGRAM
+        self.assertEqual(obj.props.enum, Gio.SocketType.DATAGRAM)
+        self.assertEqual(obj.enum, Gio.SocketType.DATAGRAM)
+        obj.props.enum = Gio.SocketType.STREAM
+        self.assertEqual(obj.props.enum, Gio.SocketType.STREAM)
+        self.assertEqual(obj.enum, Gio.SocketType.STREAM)
+        obj.props.enum = 2
+        self.assertEqual(obj.props.enum, Gio.SocketType.DATAGRAM)
+        self.assertEqual(obj.enum, Gio.SocketType.DATAGRAM)
+        obj.enum = 1
+        self.assertEqual(obj.props.enum, Gio.SocketType.STREAM)
+        self.assertEqual(obj.enum, Gio.SocketType.STREAM)
+
+        self.assertRaises(TypeError, setattr, obj, 'enum', 'foo')
+        self.assertRaises(TypeError, setattr, obj, 'enum', object())
+
+        self.assertRaises(TypeError, gobject.property, type=Gio.SocketType)
+        self.assertRaises(TypeError, gobject.property, type=Gio.SocketType,
+                          default=Gio.SocketProtocol.TCP)
+        self.assertRaises(TypeError, gobject.property, type=Gio.SocketType,
+                          default=object())
+        self.assertRaises(TypeError, gobject.property, type=Gio.SocketType,
+                          default=1)
+
     def testRange(self):
         # kiwi code
         def max(c):
@@ -270,8 +304,6 @@
         # self.assertRaises(TypeError, gobject.property, type=bool, default=0)
         self.assertRaises(TypeError, gobject.property, type=bool, default='ciao mamma')
         self.assertRaises(TypeError, gobject.property, type=bool)
-        self.assertRaises(TypeError, gobject.property, type=GEnum)
-        self.assertRaises(TypeError, gobject.property, type=GEnum, default=0)
         self.assertRaises(TypeError, gobject.property, type=object, default=0)
         self.assertRaises(TypeError, gobject.property, type=complex)
         self.assertRaises(TypeError, gobject.property, flags=-10)
'''
        self.apply_patch(self.directory, text)
        filename = os.path.join(self.directory, 'gi', 'module.py')
        src = 'string.maketrans'
        dst = 'maketrans'
        patch(filename, src, dst)
