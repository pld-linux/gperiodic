Summary:	Displays a periodic table of the elements
Summary(pl.UTF-8):	Wyświetla układ okresowy pierwiastków
Name:		gperiodic
Version:	2.0.9
Release:	1
License:	GPL
Group:		X11/Applications
Source0:	http://www.frantz.fi/software/%{name}-%{version}.tar.gz
# Source0-md5:	6ecd96c3cf6b204cfe5210d67f107bcb
URL:		http://www.frantz.fi/software/gperiodic.php
BuildRequires:	gtk+-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)


%description
Gperiodic displays a periodic table of the elements, allowing you to
browse through the elements, and view detailed information about each
element.

%description -l pl.UTF-8
Gperiodic wyświetla układ okresowy pierwiastków. Pozwala przeglądać
układ i wyświetla szczegółowe informacje o pierwiastkach.

%prep
%setup -q

%build
%{__make}

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_mandir}/man1,%{_bindir},%{_pixmapsdir},%{_desktopdir}}

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc README ChangeLog NEWS AUTHORS 
%attr(755,root,root) %{_bindir}/*
%{_desktopdir}/*.desktop
%{_pixmapsdir}/*.png
