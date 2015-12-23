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

You're now in a shell on the host:

```
atomic host status
systemctl reboot
```
