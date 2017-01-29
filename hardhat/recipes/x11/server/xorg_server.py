import os
from hardhat.recipes.base import GnuRecipe


class XOrgServerRecipe(GnuRecipe):
    def __init__(self, *args, **kwargs):
        super(XOrgServerRecipe, self).__init__(*args, **kwargs)
        self.sha256 = '79ae2cf39d3f6c4a91201d8dad549d1d' \
                      '774b3420073c5a70d390040aa965a7fb'
        self.name = 'xorg-server'
        self.version = '1.19.1'
        self.depends = ['libepoxy', 'libunwind', 'nettle', 'openssl', 'pixman',
                        'wayland', 'wayland-protocols',
                        'xkeyboard-config', 'xorg-apps']
        self.url = 'http://ftp.x.org/pub/individual/xserver/' \
                   'xorg-server-$version.tar.bz2'

        self.configure_args += [
            '--sysconfdir=%s/etc' % self.prefix_dir,
            '--enable-glamor',
            #'--enable-install-setuid',
            '--enable-suid-wrapper',
            #'--with-xkb-output=/var/lib/xkb'
            ]
        self.sudo = True
        self.configure_strip_cross_compile()
        self.environment['CFLAGS'] += ' -Wno-error=array-bounds'

    def install(self):
        self.log_dir('install', self.directory, 'removing old libexec/Xorg')
        file = os.path.join(self.prefix_dir, 'libexec', 'Xorg')
        if os.path.exists(file):
            os.remove(file)

        self.log_dir('install', self.directory, 'removing old libexec/Xorg')
        file = os.path.join(self.prefix_dir, 'libexec', 'Xorg.wrap')
        if os.path.exists(file):
            os.remove(file)

        super(XOrgServerRecipe, self).install()

        exe = '%s/bin/Xorg' % self.prefix_dir
        self.log_dir('install', self.directory, 'chown root Xorg')
        self.run_sudo(['chown', 'root', exe])
        self.log_dir('install', self.directory, 'setuid Xorg')
        self.run_sudo(['chmod', '+s', exe])
        self.run_exe(args, self.directory, self.environment)

        exe = '%s/libexec/Xorg.wrap' % self.prefix_dir
        self.log_dir('install', self.directory, 'chown root Xorg.wrap')
        self.run_sudo(['chown', 'root', exe])
        self.run_exe(args, self.directory, self.environment)
        self.log_dir('install', self.directory, 'setuid Xorg.wrap')
        self.run_sudo(['chmod', '+s', exe])
        self.run_exe(args, self.directory, self.environment)

        exe = '%s/libexec/Xorg' % self.prefix_dir
        self.log_dir('install', self.directory, 'chown root libexec/Xorg')
        self.run_sudo(['chown', 'root', exe])
        self.log_dir('install', self.directory, 'setuid libexec/Xorg')
        self.run_sudo(['chmod', '+s', exe])

    def patch(self):
        patch = r'''
Submitted By:            Armin K. <krejzi at email dot com>
Date:                    2012-12-30
Initial Package Version: 1.13.1
Upstream Status:         Not submitted.
Origin:                  Upstream mailing list.
Comment:                 Rediffed for Package Version 1.17.2 by
                         Fernando de Oliveira <famobr at yahoo dot com dot br>
Description:             Adds PRIME support to Xorg Server to make GPU offloading work.

diff -Naur xorg-server-1.17.2.orig/hw/xfree86/common/xf86Init.c xorg-server-1.17.2/hw/xfree86/common/xf86Init.c
--- xorg-server-1.17.2.orig/hw/xfree86/common/xf86Init.c	2015-06-05 12:19:40.000000000 -0300
+++ xorg-server-1.17.2/hw/xfree86/common/xf86Init.c	2015-06-17 11:35:07.227581436 -0300
@@ -340,6 +340,16 @@
     return ret;
 }

+extern void xf86AutoConfigOutputDevice(ScrnInfoPtr pScrn, ScrnInfoPtr master);
+static void
+xf86AutoConfigOutputDevices(void)
+{
+    int i;
+
+    for (i = 0; i < xf86NumGPUScreens; i++)
+        xf86AutoConfigOutputDevice(xf86GPUScreens[i], xf86Screens[0]);
+}
+
 static void
 InstallSignalHandlers(void)
 {
@@ -929,6 +939,8 @@
     for (i = 0; i < xf86NumGPUScreens; i++)
         AttachUnboundGPU(xf86Screens[0]->pScreen, xf86GPUScreens[i]->pScreen);

+    xf86AutoConfigOutputDevices();
+
     xf86VGAarbiterWrapFunctions();
     if (sigio_blocked)
         OsReleaseSIGIO();
diff -Naur xorg-server-1.17.2.orig/hw/xfree86/common/xf86platformBus.c xorg-server-1.17.2/hw/xfree86/common/xf86platformBus.c
--- xorg-server-1.17.2.orig/hw/xfree86/common/xf86platformBus.c	2015-06-16 12:21:07.000000000 -0300
+++ xorg-server-1.17.2/hw/xfree86/common/xf86platformBus.c	2015-06-17 11:35:07.227581436 -0300
@@ -469,6 +469,8 @@
     return foundScreen;
 }

+extern void xf86AutoConfigOutputDevice(ScrnInfoPtr pScrn, ScrnInfoPtr master);
+
 int
 xf86platformAddDevice(int index)
 {
@@ -537,6 +539,7 @@
    }
    /* attach unbound to 0 protocol screen */
    AttachUnboundGPU(xf86Screens[0]->pScreen, xf86GPUScreens[i]->pScreen);
+   xf86AutoConfigOutputDevice(xf86GPUScreens[i], xf86Screens[0]);

    RRResourcesChanged(xf86Screens[0]->pScreen);
    RRTellChanged(xf86Screens[0]->pScreen);
diff -Naur xorg-server-1.17.2.orig/hw/xfree86/modes/xf86Crtc.c xorg-server-1.17.2/hw/xfree86/modes/xf86Crtc.c
--- xorg-server-1.17.2.orig/hw/xfree86/modes/xf86Crtc.c	2015-06-16 10:55:48.000000000 -0300
+++ xorg-server-1.17.2/hw/xfree86/modes/xf86Crtc.c	2015-06-17 11:35:07.230581367 -0300
@@ -3387,3 +3387,35 @@
             crtc->x = crtc->y = 0;
         }
 }
+
+
+void xf86AutoConfigOutputDevice(ScrnInfoPtr pScrn, ScrnInfoPtr master)
+{
+    RRProviderPtr master_provider;
+    xf86CrtcConfigPtr config = XF86_CRTC_CONFIG_PTR(master);
+    xf86CrtcConfigPtr slave_config = XF86_CRTC_CONFIG_PTR(pScrn);
+    Bool unbound = FALSE;
+
+    if (!config || !slave_config)
+        return;
+
+    master_provider = config->randr_provider;
+
+    if ((master->capabilities & RR_Capability_SinkOffload) &&
+        pScrn->capabilities & RR_Capability_SourceOffload) {
+            /* source offload */
+
+        DetachUnboundGPU(pScrn->pScreen);
+        unbound = TRUE;
+        AttachOffloadGPU(master->pScreen, pScrn->pScreen);
+        slave_config->randr_provider->offload_sink = master_provider;
+    }
+    if ((master->capabilities & RR_Capability_SourceOutput) &&
+               pScrn->capabilities & RR_Capability_SinkOutput) {
+        /* sink offload */
+        if (!unbound)
+            DetachUnboundGPU(pScrn->pScreen);
+        AttachOutputGPU(master->pScreen, pScrn->pScreen);
+        slave_config->randr_provider->output_source = master_provider;
+    }
+}
'''
        self.apply_patch(self.directory, patch)
