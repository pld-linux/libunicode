Summary:	A unicode manipulation library
Name:		libunicode
Version:	0.4
Release:	3
License:	LGPL
Group:		Libraries
Group(pl):	Biblioteki
Source0:	http://www.pango.org/download/%{name}-%{version}.tar.gz
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
A library to handle unicode strings

%package devel
Summary:	A unicode manipulation library
Group:		Development/Libraries
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
The libunicode-devel package includes the static libraries and header
files for the libunicode package.

Install libunicode-devel if you want to develop programs which will
use libunicode.

%package static
Summary:	Static %{name} libraries
Summary(pl):	Biblioteki statyczne %{name}
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name}-devel = %{version}

%description static
Static %{name} libraries.

%description -l pl static
Biblioteki statyczne %{name}.

%prep
%setup -q

%build
CFLAGS="$RPM_OPT_FLAGS"; export CFLAGS
%configure 
%{__make} 

%install
rm -rf $RPM_BUILD_ROOT
#install -d $RPM_BUILD_ROOT%{_prefix}

%{__make} install DESTDIR=$RPM_BUILD_ROOT

%clean
rm -rf $RPM_BUILD_ROOT

%post -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc README AUTHORS COPYING ChangeLog TODO
%{_libdir}/libunicode.so.*.*.*

%files devel
%defattr(644,root,root,755)
%{_libdir}/libunicode.so
%{_includedir}/*
%attr(755,root,root) %{_bindir}/unicode-config

%files static
%defattr(644,root,root,755)
%{_libdir}/libunicode.a
