Summary:	Sri Lankan input method for SCIM
Summary(pl.UTF-8):	Metoda wprowadzania znaków srilanckich dla platformy SCIM
Name:		scim-sayura
Version:	0.3.3
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://www.sayura.net/im/%{name}-%{version}.tar.gz
# Source0-md5:	d239f30aa0b702ba7c098a266c357dcf
Patch0:		%{name}-fix-constructor.patch
URL:		http://www.sayura.net/im/
BuildRequires:	libstdc++-devel
BuildRequires:	pkgconfig
BuildRequires:	scim-devel >= 1.0
Requires:	scim >= 1.0
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a Sinhala Trans input method for SCIM.

%description -l pl.UTF-8
Ten pakiet udostępnia metodę wprowadzania Sinhala Trans dla platformy
SCIM.

%prep
%setup -q
%patch -P0 -p1

%build
%configure \
	--disable-static

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.la

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/sayura.so
%{_datadir}/scim/icons/scim-sayura.png
