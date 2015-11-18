FROM rhel7/rhel-tools

LABEL BZComponent="rhel-tools-docker"
LABEL Name="rhel7/atomichost-kerneldebug-install"
LABEL Version="7.1"
LABEL Release="0"
LABEL Architecture="x86_64"

RUN yum -y install glib2 pygobject3 && yum clean all
RUN cd /root && git clone --depth=1 http://gitlab.osas.lab.eng.rdu2.redhat.com/walters/atomichost-kerneldebug-install.git && cd atomichost-kerneldebug-install && ./configure --prefix=/usr && make && make install
LABEL RUN "/usr/bin/docker run --name \${NAME} --rm --privileged -v /:/host --pid=host \${IMAGE} atomichost-debuglayer"
