%define keepstatic 1
Name:       libtheora
Summary:    Theora Video Compression Codec
Version:    1.2.0
Release:    1
License:    BSD
URL:        https://github.com/sailfishos/libtheora
Source0:    %{name}-%{version}.tar.bz2
Requires(post):  /sbin/ldconfig
Requires(postun):  /sbin/ldconfig
BuildRequires:  pkgconfig(ogg)
BuildRequires:  pkgconfig(vorbis)
BuildRequires:  pkgconfig(libpng)

BuildRoot:  %{_tmppath}/%{name}-%{version}-build

%description
Description: %{summary}

%package devel
Summary:    Development tools for Theora applications
Requires:   %{name} = %{version}-%{release}

%description devel
Description: %{summary}

%package devel-static
Summary:    Development tools for Theora applications

%description devel-static
Description: %{summary}

%prep
%setup -q -n %{name}-%{version}/theora

%build
./autogen.sh
%configure --enable-static \
    --disable-shared \
    --disable-examples

%make_build

%install
%make_install
rm -rf %{buildroot}/usr/share/doc/libtheora

%post -p /sbin/ldconfig

%postun -p /sbin/ldconfig

%files
%license COPYING
#%{_libdir}/libtheora.so.*
#%{_libdir}/libtheoradec.so.*
#%{_libdir}/libtheoraenc.so.*

%files devel-static
%{_libdir}/*.a

%files devel
%{_includedir}/theora
#%{_libdir}/*.so
%{_libdir}/pkgconfig/theora.pc
%{_libdir}/pkgconfig/theoraenc.pc
%{_libdir}/pkgconfig/theoradec.pc
