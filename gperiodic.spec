Summary:	Displays a periodic table of the elements.
Name:		gperiodic
Version:	1.2.6
Release:	1
Copyright:	GPL
Group:		Applications/Scientific
Source:		ftp://ftp.seul.org/pub/gperiodic/%{name}-%{version}.tar.gz
URL:		http://gperiodic.seul.org/
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gperiodic displays a periodic table of the elements, allowing you to browse
through the elements, and view detailed information about each element.

%prep
%setup -q -n gperiodic

%build
aclocal
autoconf
echo "n" | gettextize --copy --force
LDFLAGS="-s"; export LDFLAGS
%configure

make

%install
rm -rf $RPM_BUILD_ROOT

make install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf $RPM_BUILD_ROOT%{_mandir}/man1/* \
	README Changes

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
