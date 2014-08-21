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
%define tizen_dir /usr/share/ca-certificates/tizen
%define wac_dir /usr/share/ca-certificates/wac

%description
Used for the installation of Tizen-specific CA certificates.

%prep
%setup -q
cp %{SOURCE1001} .

%build

%install
rm -fr %{buildroot}
mkdir -p %{buildroot}/%{tizen_dir}
mkdir -p %{buildroot}/%{wac_dir}
cp -arf certificates/tizen*.pem %{buildroot}/%{tizen_dir}/
cp -arf certificates/wac*.pem %{buildroot}/%{wac_dir}/

%files
%manifest %{name}.manifest
%license LICENSE
%defattr(-,root,root,-)
%{tizen_dir}/*
%{wac_dir}/*

%changelog
