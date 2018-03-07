Name:           qemu
Version:        2.11.1
Release:        1%{?dist}
Summary:        QEMU the FAST! processor emulator

License:        GPLv2+
URL:            https://www.qemu.org
Source0:        https://download.qemu.org/%{name}-%{version}.tar.xz

BuildRequires:  gtk2-devel
BuildArch:      x86_64

%description
Packaging the latest (at time of writing) version of qemu that is not available from Red Hat repository

%prep
%setup -q -n %{name}-%{version}

%build
./configure --target-list=%{buildarch}-softmmu
make

%install
%make_install

%clean

rm -rf $RPM_BUILD_ROOT


%files
%defattr(-,root,root,-)
/usr/local/bin/
/usr/local/libexec/
/usr/local/share/locale/
/usr/local/share/qemu/

%doc

%changelog
* Wed Feb 21 2018 Glen Yu <glen.yu@gmail.com> - 2.11.1-1
- packaging latest version of qemu from source for RHEL7
