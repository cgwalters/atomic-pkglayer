Summary: A tool to install debug packages on Atomic Host
Name: atomic-pkglayer
Version: 2015.3
Release: 2%{?dist}
#VCS: https://github.com/cgwalters/atomic-pkglayer
# This tarball is generated via `git archive`.
# It doesn't follow the Github guidelines because they only work for
# github; the infrastructure above is generic for any git repository.
Source0: %{name}-%{version}.tar.xz
License: LGPLv2+
BuildRequires: git
URL: https://github.com/cgwalters/atomic-pkglayer
# We always run autogen.sh
BuildRequires: autoconf automake libtool
# For docs

Requires: pygobject3-base
Requires: rpm-ostree

%description
%{summary}

%prep
%autosetup -Sgit -n %{name}-%{version}

%build
env NOCONFIGURE=1 ./autogen.sh
%configure --disable-silent-rules
make %{?_smp_mflags}

%install
make install DESTDIR=%{buildroot} INSTALL="install -p -c"

%files
%doc COPYING README.md
%{_bindir}/atomic-pkglayer


