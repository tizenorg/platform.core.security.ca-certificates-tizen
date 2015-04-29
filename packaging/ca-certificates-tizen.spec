Name:          ca-certificates-tizen
Summary:       Tizen-specific CA certificate installation
Version:       0.1.1
Release:       0
Group:         Security/Certificate Management
URL:           http://www.tizen.org
License:       Apache-2.0
Source:        %{name}-%{version}.tar.gz
Source1001:    %{name}.manifest
BuildArch:     noarch
BuildRequires: cmake
BuildRequires: openssl

%define tizen_dir       /usr/share/ca-certificates/tizen
%define wac_dir         /usr/share/ca-certificates/wac
%define fingerprint_dir /usr/share/ca-certificates/fingerprint

%description
Used for the installation of Tizen-specific CA certificates.

%prep
%setup -q
cp %{SOURCE1001} .

%build
%cmake . -DTIZEN_DIR=%{tizen_dir} \
         -DWAC_DIR=%{wac_dir} \
         -DFINGERPRINT_DIR=%{fingerprint_dir}

%install
rm -fr %{buildroot}
%make_install
mkdir -p %{buildroot}%{tizen_dir}
mkdir -p %{buildroot}%{wac_dir}
mkdir -p %{buildroot}%{fingerprint_dir}

%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%license LICENSE
%{tizen_dir}/*
%{wac_dir}/*
%{fingerprint_dir}/*

%changelog
