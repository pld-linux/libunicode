Summary:	A unicode manipulation library
Name:		libunicode
Version:	0.4
Release:	7
License:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source0:	http://www.pango.org/download/%{name}-%{version}.tar.gz
Patch0:		%{name}-unicodeConf.sh.patch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_prefix		/usr/X11R6

%description
A library to handle unicode strings.

%package devel
Summary:	A unicode manipulation library
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The libunicode-devel package includes the static libraries and header
files for the libunicode package.

Install libunicode-devel if you want to develop programs which will
use libunicode.

%package static
Summary:	Static libunicode libraries
Summary(pl):	Biblioteki statyczne libunicode
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static libunicode libraries.

%description -l pl static
Biblioteki statyczne libunicode.

%prep
%setup -q
%patch0 -p1

%build
libtoolize --copy --force
aclocal
automake -a -c
autoconf
%configure 
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install DESTDIR=$RPM_BUILD_ROOT

strip --strip-unneeded $RPM_BUILD_ROOT%{_libdir}/lib*.so.*.*

gzip -9nf README AUTHORS ChangeLog TODO

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_libdir}/lib*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc *.gz
%attr(755,root,root) %{_bindir}/unicode-config
%attr(755,root,root) %{_libdir}/lib*.so
%attr(755,root,root) %{_libdir}/lib*.la
%attr(755,root,root) %{_libdir}/*.sh
%{_includedir}/*

%files static
%defattr(644,root,root,755)
%{_libdir}/lib*.a
