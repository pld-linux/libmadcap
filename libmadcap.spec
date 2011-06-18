Summary:	MADCAP protocol client library
Summary(pl.UTF-8):	Biblioteka klienta protokołu MADCAP
Name:		libmadcap
Version:	0.1
Release:	4
License:	GPL
Group:		Libraries
Source0:	http://dl.sourceforge.net/malloc/%{name}-%{version}.tar.gz
# Source0-md5:	b9314ccddbe73cf3e1a9147ccd357cb6
Source1:	%{name}_manual.pdf
# Source1-md5:	615dc6c4234276e1a63720dfa76138b3
Patch0:		%{name}-termcap.patch
URL:		http://malloc.sourceforge.net
BuildRequires:	autoconf
BuildRequires:	automake
BuildRequires:	libtool
BuildRequires:	ncurses-devel
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This is basic MADCAP (RFC2730) client implementation library.

%description -l pl.UTF-8
To jest prosta implementacja protokołu MADCAP (RFC2730).

%package devel
Summary:	Development part of libmadcap
Summary(pl.UTF-8):	Część dla programistów biblioteki libmadcap
Group:		Development/Libraries
Requires:	%{name} = %{version}-%{release}

%description devel
Development part of libmadcap.

%description devel -l pl.UTF-8
Pliki potrzebne do programowania z wykorzystaniem libmadcap.

%package static
Summary:	Static version of libmadcap library
Summary(pl.UTF-8):	Wersja statyczna biblioteki libmadcap
Group:		Development/Libraries
Requires:	%{name}-devel = %{version}-%{release}

%description static
Static version of libmadcap.

%description static -l pl.UTF-8
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
