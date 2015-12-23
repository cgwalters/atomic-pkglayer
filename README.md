https://trello.com/c/2TxKtM9x/442-install-test-kernel-for-atomic-debugging-gss-7-2

This script supports installing an arbitrary set of RPMs
as a layer onto an Atomic Host system.  The RPMs must not need
dependencies outside of the Atomic Host.

First, start and enter a shell in the tools container:
```
atomic run rhel7/rhel-tools
```

Inside the tools container:

```
yum -y install pygobject3-base
cd /root
git clone https://github.com/cgwalters/atomic-pkglayer/
cd atomic-pkglayer
curl -O http://example.com/kernel-debug.rpm
./atomic-pkglayer ./kernel-deug.rpm
exit
```

You're now back in a shell on the host:

```
atomic host status
```

Notice that we have a custom tree commit with a `local` version,
which combines the base tree with our custom packages.

To go to the new deployment:

```
systemctl reboot
```

To revert back:

```
atomic host rollback
systemctl reboot
```

To free up the space occupied by our custom tree (be sure you have
performed the rollback to the production tree first):

```
ostree refs --delete temp-local
ostree admin undeploy 1
```

