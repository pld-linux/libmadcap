Summary:	MADCAP protocol client library
Summary(pl):	Biblioteka klienta protoko³u MADCAP
Name:		libmadcap
Version:	0.1
Release:	4
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/malloc/%{name}-%{version}.tar.gz
Source1:	http://deimos.campus.luth.se/malloc/documentation/%{name}_manual.pdf
Patch0:		%{name}-termcap.patch
URL:		http://deimos.campus.luth.se/malloc/
BuildRequires:	ncurses-devel
BuildRequires:	automake
BuildRequires:	autoconf
BuildRequires:	libtool
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is basic MADCAP (RFC2730) client implementation library.

%description -l pl
To jest prosta implementacja protoko³u MADCAP (RFC2730).

%package devel
Summary:	Development part of libmadcap
Summary(pl):	Czê¶æ dla programistów biblioteki libmadcap
Group:		Development/Libraries
Requires:	%{name} = %{version}

%description devel
Development part of libmadcap.

%description devel -l pl
Pliki potrzebne do programowania z wykorzystaniem libmadcap.

%package static
Summary:	Static version of libmadcap library
Summary(pl):	Wersja statyczna biblioteki libmadcap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}

%description static
Static version of libmadcap.

%description static -l pl
Wersja statyczna biblioteki libmadcap.

%prep
%setup  -q
%patch0 -p1

%build
rm -f missing
%{__libtoolize}
%{__aclocal}
%{__autoconf}
%{__automake}
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install %{SOURCE1} .

%clean
rm -rf $RPM_BUILD_ROOT

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%files
%defattr(644,root,root,755)
%doc AUTHORS*
%attr(755,root,root) %{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc libmadcap_manual.pdf
%{_includedir}/madcap
%attr(755,root,root) %{_libdir}/*.so
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
