%global debug_package %{nil}

Name:           exa
Version:        0.10.1
Release:        1
Summary:        exa is a replacement for ls written in Rust.
Group:          Applications/System
License:        GPLv2
URL:            https://github.com/ogham/exa
BuildRequires:  cmake, libgit2, openssl-devel
Source:         https://github.com/ogham/exa/archive/v%{version}.tar.gz

%{?el7:BuildRequires: cargo, rust}

%description
exa is a modern replacement for ls. It uses colours for information by default,
helping you distinguish between many types of files, such as whether you are
the owner, or in the owning group. It also has extra features not present in
the original ls, such as viewing the Git status for a directory, or recursing
into directories with a tree view. exa is written in Rust, so it's small,
fast, and portable.

%prep
%setup -q -n %{name}-%{version}

%build
cargo build --release

%install
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/bin
cp target/release/exa %{buildroot}/usr/bin/

%clean
rm -rf %{buildroot}

%files
%defattr(-,root,root,-)
/usr/bin/exa

%changelog
* Tue Apr 13 2021 Jamie Curnow <jc@jc21.com> - 0.10.1-1
- Updated to 0.10.1

* Tue Apr 6 2021 Jamie Curnow <jc@jc21.com> - 0.10.0-1
- Updated to 0.10.0

* Mon Jul 15 2019 Jamie Curnow <jc@jc21.com> - 0.9.0-1
- Updated to 0.9.0

* Mon Jul 9 2018 Jamie Curnow <jc@jc21.com> - 0.8.0-1
- Updated to 0.8.0

* Wed Jun 14 2017 Jamie Curnow <jc@jc21.com> - 0.6.0-1
- Updated to 0.6.0

* Tue Feb 2 2016 Jamie Curnow <jc@jc21.com> - 0.4.0-1
- Updated to 0.4.0

* Tue Sep 1 2015 Jamie Curnow <jc@jc21.com> - 0.3.0-1
- Updated to 0.3.0

* Tue Feb 24 2015 Jamie Curnow <jc@jc21.com> - 0.1.0-1
- Initial Spec File

