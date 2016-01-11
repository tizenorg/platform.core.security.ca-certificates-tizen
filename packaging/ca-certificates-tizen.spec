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
BuildRequires: pkgconfig(libtzplatform-config)
BuildRequires: ca-certificates-devel
Requires: ca-certificates

%define tizen_dir       %TZ_SYS_SHARE/ca-certificates/tizen
%define wac_dir         %TZ_SYS_SHARE/ca-certificates/wac
%define fingerprint_dir %TZ_SYS_SHARE/ca-certificates/fingerprint

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
%make_install
mkdir -p %buildroot%tizen_dir
mkdir -p %buildroot%wac_dir
mkdir -p %buildroot%fingerprint_dir
mkdir -p %buildroot%TZ_SYS_CA_CERTS

for cert in `ls "%buildroot%tizen_dir"`
do
    subject_hash=`openssl x509 -in "%buildroot%tizen_dir/$cert" -noout -subject_hash`

    idx=0
    while true
    do
        if [ -f "%TZ_SYS_CA_CERTS/$subject_hash.$idx" ]; then
            idx=`expr $idx + 1`
        else
            break
        fi
    done

    ln -sf "%tizen_dir/$cert" "%buildroot%TZ_SYS_CA_CERTS/$subject_hash.$idx"
done

%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%license LICENSE
%{tizen_dir}/*
%{wac_dir}/*
%{fingerprint_dir}/*
%TZ_SYS_CA_CERTS/*

%changelog
