Name:           opencore-amr
Version:        0.1.3
Release:        1%{?dist}
Summary:        OpenCORE Adaptive Multi Rate (AMR) speech codec

License:        Apache License, Version 2.0
URL:            https://sourceforge.net/projects/opencore-amr/
Source0:        http://downloads.sourceforge.net/project/opencore-amr/opencore-amr/opencore-amr-%{version}.tar.gz

%description
This library contains an implementation of the 3GPP TS 26.073 specification for
the Adaptive Multi Rate (AMR) speech codec and an implementation for the 3GPP
TS 26.173 specification for the Adaptive Multi-Rate - Wideband (AMR-WB) speech
decoder. The implementation is derived from the OpenCORE framework, part of the
Google Android project.


%package        devel
Summary:        Development files for %{name}
Requires:       %{name}%{?_isa} = %{version}-%{release}
Requires:       pkgconfig

%description    devel
The %{name}-devel package contains libraries and header files for
developing applications that use %{name}.


%prep
%setup -q


%build
%configure --disable-static --disable-silent-rules
make %{?_smp_mflags}


%install
rm -rf %{buildroot}
%make_install
find %{buildroot} -name '*.la' -exec rm -f {} ';'


%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig


%files
%license LICENSE
%doc AUTHORS ChangeLog README
%{_libdir}/*.so.*

%files devel
%{_includedir}/*
%{_libdir}/*.so
%{_libdir}/pkgconfig/*.pc


%changelog
* Sun May 15 2016 Jajauma's Packages <jajauma@yandex.ru> - 0.1.3-1
- Public release
