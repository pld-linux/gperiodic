Summary:	Displays a periodic table of the elements
Summary(pl):	Wy¶wietla uk³ad okresowy pierwiastków
Name:		gperiodic
Version:	1.3.0
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	ftp://ftp.seul.org/pub/gperiodic/%{name}-%{version}.tar.gz
Patch0:		%{name}-ac_fix.patch
URL:		http://gperiodic.seul.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	readline-devel >= 4.2
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
%patch -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make} gperiodic_LDADD="-lreadline"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install DESTDIR=$RPM_BUILD_ROOT

install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
