Layering RPM packages on top of an (rpm-)ostree tree
----------------------------------------------------

This is a proof-of-concept for RPM package layering on top of an
OSTree base tree.  It is only a demonstrator; do not use in
production.

To use:

    # ./atomic-pkglayer add strace

Now, let's try:

    # ostree admin status

What's up with that <unknown origin type>?  Well, OSTree is telling us
it no longer knows how to upgrade the system.  If you look at the
origin file underneath `/ostree/deploy/.../*.origin` for the new
deployment, you'll see that we have listed the additional packages,
and the refspec is now `base_refspec`.

And indeed if we try it:

    # atomic upgrade
    error: No origin/refspec in current deployment origin; cannot upgrade via ostree 

Anyways, let's reboot, and notice that strace is available.

    # systemctl reboot
    # rpm -q strace 

A very important thing to note; we do have a single unified RPM
database, still in /usr/share/rpm.

Integrating this into rpm-ostree
--------------------------------

There are a number of reasons I wrote this proof-of-concept as an
addon layer.

 * The whole subject deserves a lot of thought and careful coding,
   and ultimately will require changes in RPM to make this work more
   widely.
 * There's a strong drive right now to backport rpm-ostree to EL7,
   and that limits the dependency/feature growth.
 * For rpm-ostree, we intend to use the new C libraries of hawkey/librepo
   for package management - this will allow much tighter integeration
   than using yum allows.
 * yum is GPL, rpm-ostree is LGPL (for several reasons, but an important one
   is to allow ASL2.0 code to link to it) 


