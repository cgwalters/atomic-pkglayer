https://trello.com/c/2TxKtM9x/442-install-test-kernel-for-atomic-debugging-gss-7-2

This script supports installing an arbitrary set of RPMs
as a layer onto an Atomic Host system.  The RPMs must not need
dependencies outside of the Atomic Host.

```
cd /root
curl -O http://example.com/kernel-debug.rpm
atomic run docker-registry.usersys.redhat.com/cgwalters/rhel-tools atomichost-debuglayer /host/$(pwd)/kernel-debug.rpm
atomic host status
systemctl reboot
```
