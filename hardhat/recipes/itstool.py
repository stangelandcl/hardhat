from .base import GnuRecipe


class ItsToolRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(ItsToolRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '97c208b51da33e0b553e830b92655f8d' \
                      'eb9132f8fbe9a646771f95c33226eb60'
        self.name = 'itstool'
        self.version = '2.0.4'
        self.depends = ['docbook-xml', 'libxml2', 'python2']
        self.url = 'http://files.itstool.org/itstool/itstool-$version.tar.bz2'

    def patch(self):
        text = r'''
Submitted by:            DJ Lucas (dj_AT_linuxfromscratch_DOT_org)
Date:                    2017-10-26
Initial Package Version: 2.0.4
Upstream Status:         Comitted
Origin:                  https://github.com/itstool/itstool/commit/9b84c007a73e8275ca45762f1bfa3ab7c3a852e2
Description:             Fixes memory exhaustion when freeing XML docs.


diff -Naur a/itstool.in b/itstool.in
--- a/itstool.in
+++ a/itstool.in
@@ -477,6 +477,7 @@ class Document (object):
         if load_dtd:
             ctxt.loadSubset(1)
         if keep_entities:
+            ctxt.loadSubset(1)
             ctxt.ctxtUseOptions(libxml2.XML_PARSE_DTDLOAD)
             ctxt.replaceEntities(0)
         else:
@@ -1043,6 +1044,7 @@ class Document (object):
         if self._load_dtd:
             ctxt.loadSubset(1)
         if self._keep_entities:
+            ctxt.loadSubset(1)
             ctxt.ctxtUseOptions(libxml2.XML_PARSE_DTDLOAD)
             ctxt.replaceEntities(0)
         else:
@@ -1069,7 +1071,9 @@ class Document (object):
                     ph_node = msg.get_placeholder(child.name).node
                     if self.has_child_elements(ph_node):
                         self.merge_translations(translations, None, ph_node, strict=strict)
-                        child.replaceNode(ph_node)
+                        newnode = ph_node.copyNode(1)
+                        newnode.setTreeDoc(self._doc)
+                        child.replaceNode(newnode)
                     else:
                         repl = self.get_translated(ph_node, translations, strict=strict, lang=lang)
                         child.replaceNode(repl)
@@ -1084,10 +1088,15 @@ class Document (object):
                     (lang + ' ') if lang is not None else '',
                     msgstr.encode('utf-8')))
                 self._xml_err = ''
+                ctxt.doc().freeDoc()
                 return node
         retnode = node.copyNode(2)
+        retnode.setTreeDoc(self._doc)
         for child in xml_child_iter(trnode):
-            retnode.addChild(child.copyNode(1))
+            newnode = child.copyNode(1)
+            newnode.setTreeDoc(self._doc)
+            retnode.addChild(newnode)
+
         ctxt.doc().freeDoc()
         return retnode
'''
        self.apply_patch(self.directory, text)
