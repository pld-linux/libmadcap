Summary:	MADCAP protocol client library	
Summary(pl):	Biblioteka klienta protokoЁu MADCAP
Name:		libmadcap
Version:	0.1
Release:	4
License:	GPL
Group:		Libraries
Group(de):	Libraries
Group(es):	Bibliotecas
Group(fr):	Librairies
Group(pl):	Biblioteki
Group(pt_BR):	Bibliotecas
Group(ru):	Библиотеки
Group(uk):	Б╕бл╕отеки
Source0:	ftp://ftp.sourceforge.net/pub/sourceforge/malloc/%{name}-%{version}.tar.gz
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
To jest prosta implementacja protokoЁu MADCAP (RFC2730).

%package devel
Summary:	Development part of libmadcap
Summary(pl):	CzЙ╤Ф dla programistСw biblioteki libmadcap
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
Requires:	%{name} = %{version}

%description devel
Development part of libmadcap.

%description devel -l pl
Pliki potrzebne do programowania z wykorzystaniem libmadcap.

%package static
Summary:	Static version of libmadcap library
Summary(pl):	Wersja statyczna biblioteki libmadcap
Group:		Development/Libraries
Group(de):	Entwicklung/Libraries
Group(es):	Desarrollo/Bibliotecas
Group(fr):	Development/Librairies
Group(pl):	Programowanie/Biblioteki
Group(pt_BR):	Desenvolvimento/Bibliotecas
Group(ru):	Разработка/Библиотеки
Group(uk):	Розробка/Б╕бл╕отеки
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
%attr(755,root,root) %{_libdir}/*.la

%files static
%defattr(644,root,root,755)
%{_libdir}/*.a
