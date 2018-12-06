%bcond_without check
%global goipath     github.com/mdlayher/wifi
%global commit      17fb8383f38adbf6a7f12e6cbd1d461760aabf5c

Version:            0

%global common_description %{expand:
Package wifi provides access to IEEE 802.11 WiFi device actions and statistics.
}

%gometa

Name:    %{goname}
Release: 0.2%{?dist}
Summary: Provides access to IEEE 802.11 WiFi device actions and statistics
License: MIT
URL:     %{gourl}
Source:  %{gosource}

BuildRequires: golang(github.com/mdlayher/genetlink)
BuildRequires: golang(github.com/mdlayher/netlink)
BuildRequires: golang(github.com/mdlayher/netlink/nlenc)
BuildRequires: golang(golang.org/x/net/bpf)
BuildRequires: golang(golang.org/x/sys/unix)

%if %{with check}
BuildRequires: golang(github.com/google/go-cmp/cmp)
BuildRequires: golang(github.com/mdlayher/genetlink/genltest)
%endif

%description
%{common_description}

%package   devel
Summary:   %{summary}
BuildArch: noarch

%description devel
%{common_description}

This package contains the source code needed for building packages that import
the %{goipath} Go namespace.

%prep
%gosetup -q
rm -rf vendor

%install
%goinstall

%check
%if %{with check}
  %gochecks
%endif

%files devel -f devel.file-list
%license LICENSE.md
%doc README.md

%changelog
* Fri Jul 13 2018 Fedora Release Engineering <releng@fedoraproject.org> - 0-0.2.git17fb838
- Rebuilt for https://fedoraproject.org/wiki/Fedora_29_Mass_Rebuild

* Thu May 17 2018 Paul Gier <pgier@redhat.com> - 0-0.1.20180517git17fb838
- First package for Fedora
