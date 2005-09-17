Summary:	Displays a periodic table of the elements
Summary(pl):	Wy¶wietla uk³ad okresowy pierwiastków
Name:		gperiodic
Version:	1.3.3
Release:	2
License:	GPL
Group:		X11/Applications
Source0:	http://gperiodic.seul.org/downloads/%{name}-%{version}.tar.gz
# Source0-md5:	8b6344276252635b18572bca17aa62f6
Patch0:		%{name}-ac_fix.patch
URL:		http://gperiodic.seul.org/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	gettext-devel
BuildRequires:	gtk+-devel
BuildRequires:	libtool
BuildRequires:	readline-devel >= 4.2
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Gperiodic displays a periodic table of the elements, allowing you to
browse through the elements, and view detailed information about each
element.

%description -l pl
Gperiodic wy¶wietla uk³ad okresowy pierwiastków. Pozwala przegl±daæ
uk³ad i wy¶wietla szczegó³owe informacje o pierwiastkach.

%prep
%setup -q
%patch -p1

%build
rm -f missing
%{__libtoolize}
%{__gettextize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure

%{__make} \
	gperiodic_LDADD="-lreadline"

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_mandir}/man1

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

install man/*.1 $RPM_BUILD_ROOT%{_mandir}/man1

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog
%attr(755,root,root) %{_bindir}/*
%{_mandir}/man1/*
