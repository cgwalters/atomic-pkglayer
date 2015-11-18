include Makefile.inc

bin_programs = atomichost-debuglayer

all:

install: $(bin_programs)
	mkdir -p $(DESTDIR)$(bindir)
	for prog in $(bin_programs); do \
		install -m 0755 $$prog $(DESTDIR)$(bindir)/$$prog; \
	done
