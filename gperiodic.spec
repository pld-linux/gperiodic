Summary: Displays a periodic table of the elements.
Name: gperiodic
Version: 1.2.6
Release: 1
Copyright: GPL
Group: Applications/Scientific
Source: ftp://ftp.seul.org/pub/gperiodic/gperiodic-1.2.6.tar.gz
URL: http://gperiodic.seul.org/
Buildroot: /var/tmp/gperiodic

%description
Gperiodic displays a periodic table of the elements, allowing you to
browse through the elements, and view detailed information about each
element.

%prep
%setup -n gperiodic
%build
./configure
make

%install
mkdir -p $RPM_BUILD_ROOT/usr/bin
mkdir -p $RPM_BUILD_ROOT/usr/man/man1
install -m 755 src/gperiodic $RPM_BUILD_ROOT/usr/bin/gperiodic
install -m 755 man/gperiodic.1 $RPM_BUILD_ROOT/usr/man/man1/gperiodic.1

%files
%defattr(-,root,root)
%doc README Changes
/usr/bin/gperiodic
/usr/man/man1/gperiodic.1

%clean
rm -rf $RPM_BUILD_ROOT
