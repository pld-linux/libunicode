
%define snap 20020919

Summary:	A unicode manipulation library
Summary(ko):	유니코드 라이브러리
Summary(pl):	Biblioteka do obr�bki unicode
Summary(ru):	隋쫄�鞫탸� Unicode
Summary(uk):	數쫄┩旽個 Unicode
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
Biblioteka obs퀅guj켧a ci켫i znak�w unicode.

%description -l ru
隋쫄�鞫탸� 켈� 怒쫏疼 遝 戇碌個苽 譚斛驅窘 � unicode.

%description -l uk
數쫄┩旽個 켈� 碌쫏燉 � 訣光있個苽 譚斛驅┹ � unicode.

%package devel
Summary:	A unicode manipulation library - development package
Summary(pl):	Pakiet dla programist�w libunicode
Summary(ru):	隋쫄�鞫탸� Unicode
Summary(uk):	數쫄┩旽個 Unicode
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
The libunicode-devel package includes header files for the libunicode
package.

%description devel -l pl
Pliki nag농wkowe potrzebne do programowania z u퓓ciem libunicode.

%description devel -l ru
彫愾� libunicode-devel 遝컵壟�� 쪼쫄�鞫탸� � 팁奸� 憫하卿率窘 켈�
僅愾讀 libunicode.

%description devel -l uk
彫愾� libunicode-devel 稽戇�潼 짝쫄┩旽漑 讀 팁奸� 憫하卿率┹ 켈�
僅愾讀 libunicode.

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
%{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
