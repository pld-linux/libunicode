
%define snap 20020919

Summary:	A unicode manipulation library
Summary(ko.UTF-8):	유니코드 라이브러리
Summary(pl.UTF-8):	Biblioteka do obróbki unicode
Summary(ru.UTF-8):	Библиотека Unicode
Summary(uk.UTF-8):	Бібліотека Unicode
Name:		libunicode
Version:	0.7
Release:	1.cvs.%{snap}.1
License:	LGPL
Group:		Libraries
Source0:	http://libunicode.sourceforge.net/src/%{name}-%{snap}.tar.bz2
# Source0-md5:	300c7294ec31a10747d5f1e0b94cf6f4
#Source0:	http://libunicode.sourceforge.net/src/%{name}-%{version}.tar.gz
URL:		http://sourceforge.net/projects/libunicode/
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library to handle unicode strings.

%description -l pl.UTF-8
Biblioteka obsługująca ciągi znaków unicode.

%description -l ru.UTF-8
Библиотека для работы со строками символов в unicode.

%description -l uk.UTF-8
Бібліотека для роботи з ланцюжками символів в unicode.

%package devel
Summary:	A unicode manipulation library - development package
Summary(pl.UTF-8):	Pakiet dla programistów libunicode
Summary(ru.UTF-8):	Библиотека Unicode
Summary(uk.UTF-8):	Бібліотека Unicode
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
The libunicode-devel package includes header files for the libunicode
package.

%description devel -l pl.UTF-8
Pliki nagłówkowe potrzebne do programowania z użyciem libunicode.

%description devel -l ru.UTF-8
Пакет libunicode-devel содержит библиотеки и файлы заголовков для
пакета libunicode.

%description devel -l uk.UTF-8
Пакет libunicode-devel містить бібліотеки та файли заголовків для
пакета libunicode.

%package static
Summary:	Static libunicode libraries
Summary(pl.UTF-8):	Biblioteki statyczne libunicode
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static libunicode libraries.

%description static -l pl.UTF-8
Biblioteki statyczne libunicode.

%prep
%setup -q -n %{name}

%build
./autogen.sh
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS ChangeLog
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%attr(755,root,root) %{_bindir}/unicode-config
%attr(755,root,root) %{_libdir}/lib*.so
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*.h

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
