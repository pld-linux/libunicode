
%define snap 20020919

Summary:	A unicode manipulation library
Summary(ko):	ю╞╢одз╣Е ╤Сюл╨Й╥╞╦╝
Summary(pl):	Biblioteka do obrСbki unicode
Summary(ru):	Библиотека Unicode
Summary(uk):	Б╕бл╕отека Unicode
Name:		libunicode
Version:	0.7
Release:	1.cvs.%{snap}
License:	LGPL
Group:		Libraries
Source0:	http://libunicode.sourceforge.net/src/%{name}-%{snap}.tar.bz2
#Source0:	http://libunicode.sourceforge.net/src/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/libunicode/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library to handle unicode strings.

%description -l pl
Biblioteka obsЁuguj╠ca ci╠gi znakСw unicode.

%description -l ru
Библиотека для работы со строками символов в unicode.

%description -l uk
Б╕бл╕отека для роботи з ланцюжками символ╕в в unicode.

%package devel
Summary:	A unicode manipulation library - development package
Summary(pl):	Pakiet dla programistСw libunicode
Summary(ru):	Библиотека Unicode
Summary(uk):	Б╕бл╕отека Unicode
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The libunicode-devel package includes header files for the libunicode
package.

%description devel -l pl
Pliki nagЁСwkowe potrzebne do programowania z u©yciem libunicode.

%description devel -l ru
Пакет libunicode-devel содержит библиотеки и файлы заголовков для
пакета libunicode.

%description devel -l uk
Пакет libunicode-devel м╕стить б╕бл╕отеки та файли заголовк╕в для
пакета libunicode.

%package static
Summary:	Static libunicode libraries
Summary(pl):	Biblioteki statyczne libunicode
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static libunicode libraries.

%description static -l pl
Biblioteki statyczne libunicode.

%prep
%setup -q -n %{name}

%build
rm -f missing
./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_bindir}/*
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
