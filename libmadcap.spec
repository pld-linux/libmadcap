Summary:	MADCAP protocol client library	
Summary(pl):	Biblioteka klienta protoko³u MADCAP
Name:		libmadcap
Version:	0.1
Release:	3
Group:		Libraries
Group(fr):	Librairies
Group(pl):	Biblioteki
License:	GPL
Source0:	http://prdownloads.sourceforge.net/malloc/libmadcap-0.1.tar.gz
Source1:	http://deimos.campus.luth.se/malloc/documentation/libmadcap_manual.pdf
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
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Requires:	%{name} = %{version}

%description devel
Development part of libmadcap.

%description devel -l pl
Pliki potrzebne do programowania z wykorzystaniem libmadcap.

%package static
Summary:	Static version of libmadcap library
Summary(pl):	Wersja statyczna biblioteki libmadcap
Group:		Development/Libraries
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
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
libtoolize --copy --force
aclocal
autoconf
automake --add-missing
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR="$RPM_BUILD_ROOT"

install %{SOURCE1} .

gzip -9nf AUTHORS*

%post   -p /sbin/ldconfig
%postun -p /sbin/ldconfig

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS* 
%{_libdir}/*.so.*.*

%files devel
%defattr(644,root,root,755)
%doc libmadcap_manual.pdf
%{_includedir}/madcap
%{_libdir}/*.so
%{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a

%changelog
* %{date} PLD Team <pld-list@pld.org.pl>
All persons listed below can be reached at <cvs_login>@pld.org.pl

$Log: libmadcap.spec,v $
Revision 1.3  2001-10-07 19:35:01  blues
- release 3
- ac2.5 ready

Revision 1.2  2001/10/03 16:41:41  filon
- changed req for main subpkg in static subpkg to devel
- release 2

Revision 1.1  2001/06/25 17:41:28  jajcus
- initial spec
