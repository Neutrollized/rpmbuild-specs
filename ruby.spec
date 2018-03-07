%define rubyver	2.5

Name:           ruby
Version:        2.5.0
Release:        1%{?dist}
Summary:        Ruby - A Programmer's Best Friend

License:        GPLv2
URL:            https://www.ruby-lang.org
Source0:        https://cache.ruby-lang.org/pub/ruby/%{rubyver}/%{name}-%{version}.tar.gz

BuildRequires:	readline-devel openssl-devel gdbm-devel libyaml-devel ncurses-devel glibc-devel tcl-devel
Requires:	libyaml openssl
BuildArch:	x86_64

%description
Package the latest (at time of writing) versio of Ruby that is not available from Red Hat repo


%prep
%setup -q -n %{name}-%{version}


%build
export CFLAGS="$RPM_OPT_FLAGS -Wall -fno-strict-aliasing"
export LDFLAGS="-Wl,-rpath,/usr/local/lib64/"

%configure \
  --enable-shared \
  --disable-rpath \
  --includedir=%{_includedir}/ruby \

make %{?_smp_mflags}


%install
%make_install

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(-,root,root,-)
%{_includedir}
%{_datadir}
/usr/bin/erb
/usr/bin/gem
/usr/bin/irb
/usr/bin/rake
/usr/bin/rdoc
/usr/bin/ri
/usr/bin/ruby
/usr/lib64/ruby/
/usr/lib64/libruby.so
/usr/lib64/libruby.so.%{rubyver}
/usr/lib64/libruby.so.%{version}
/usr/lib64/pkgconfig/ruby-%{rubyver}.pc

%doc



%changelog
* Wed Mar 7 2018 Glen Yu <glen.yu@gmail.com> - 2.5.0-1
- packaging latest version of Ruby from source for RHEL7
