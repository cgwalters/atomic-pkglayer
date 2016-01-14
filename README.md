https://trello.com/c/2TxKtM9x/442-install-test-kernel-for-atomic-debugging-gss-7-2

This script supports installing an arbitrary set of RPMs
as a layer onto an Atomic Host system.  The RPMs must not need
dependencies outside of the Atomic Host.

#### On the Atomic Host system

Start and enter a shell in the tools container

```
atomic run rhel7/rhel-tools
```

#### Inside the tools container

##### Install `atomic-pkglayer`

```
cd /root
git clone https://github.com/cgwalters/atomic-pkglayer/
cd atomic-pkglayer
git checkout v2015.4
```

##### Download RPMs
* manually
```
curl -O http://example.com/kernel-debug.rpm
```
* using yumdownloader
```
yumdownloader --resolve ruby
```
##### Install the RPMs into the Atomic Host system and exit the container
* Single RPM
```
/root/atomic-pkglayer/atomic-pkglayer /path/to/specific.rpm
exit
```
* Multiple RPMs
```
/root/atomic-pkglayer/atomic-pkglayer /path/to/rpms/*rpm
exit
```
#### Back on the Atomic Host system

* Inspect the system state:

```
atomic host status
```

Notice that we have a custom tree commit with a `local` version,
which combines the base tree with our custom packages.

To go to the new deployment:

```
systemctl reboot
 ```

* To undo the changes, use `atomic host rollback`, and reboot again.

```
atomic host rollback
systemctl reboot
```

To free up the space occupied by our custom tree (be sure you have
performed the rollback to the production tree first):

```
ostree admin undeploy 1
```
