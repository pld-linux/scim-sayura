Summary:	Sri Lankan input method for SCIM
Name:		scim-sayura
Version:	0.3.3
Release:	1
License:	GPL v2
Group:		Libraries
Source0:	http://www.sayura.net/im/%{name}-%{version}.tar.gz
# Source0-md5:	d239f30aa0b702ba7c098a266c357dcf
Patch0:		%{name}-fix-constructor.patch
URL:		http://www.sayura.net/im/
BuildRequires:	scim-devel
Requires:	scim
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
This package provides a Sinhala Trans input method for SCIM.

%prep
%setup -q
%patch0 -p1

%build
%configure

%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%{__rm} $RPM_BUILD_ROOT%{_libdir}/scim-1.0/*/*/*.{la,a}

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%doc README AUTHORS
%attr(755,root,root) %{_libdir}/scim-1.0/*/IMEngine/sayura.so
%{_datadir}/scim/icons/scim-sayura.png
