Summary:	Displays a periodic table of the elements
Summary(pl):	Wy¶wietla uk³ad okresowy pierwiastków
Name:		gperiodic
Version:	1.2.6
Release:	1
License:	GPL
Group:		X11/Applications
Group(pl):	X11/Aplikacje
Source0:	ftp://ftp.seul.org/pub/gperiodic/%{name}-%{version}.tar.gz
URL:		http://gperiodic.seul.org/
BuildRequires:	gettext-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6
%define		_mandir		%{_prefix}/man

%description
Gperiodic displays a periodic table of the elements, allowing you to
browse through the elements, and view detailed information about each
element.

%description -l pl
Gperiodic wy¶wietla uk³ad okresowy pierwiastków. Pozwalaj±c przgl±daæ
uk³ad i wy¶wietla szczegó³owe informacje o pierwiastkach.


%prep
%setup -q -n gperiodic

%build
aclocal
autoconf
echo "n" | gettextize --copy --force
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

gzip -9nf README Changes

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README Changes
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
