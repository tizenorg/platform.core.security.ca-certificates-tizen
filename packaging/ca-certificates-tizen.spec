Name:          ca-certificates-tizen
Summary:       Tizen-specific CA certificate installation
Version:       0.2.0
Release:       0
Group:         Security/Certificate Management
URL:           http://www.tizen.org
License:       Apache-2.0
Source:        %{name}-%{version}.tar.gz
Source1001:    %{name}.manifest
BuildRequires: cmake
BuildRequires: openssl

%define ro_data_dir     %{?TZ_SYS_RO_SHARE:%TZ_SYS_RO_SHARE}%{!?TZ_SYS_RO_SHARE:%_datadir}
%define tizen_dir       %{ro_data_dir}/ca-certificates/tizen
%define fingerprint_dir %{ro_data_dir}/ca-certificates/fingerprint

%description
Used for the installation of Tizen-specific CA certificates.

%prep
%setup -q
cp %{SOURCE1001} .

%build

# define build architecture
%ifarch %{ix86}
echo "release emulator mode"
%define ARCH i586
%define REL_MODE emul
%else
echo "release engineering mode"
%define ARCH arm
%define REL_MODE eng
%endif

%cmake . -DRELMODE=%{REL_MODE} \
         -DTIZEN_DIR=%{tizen_dir} \
         -DFINGERPRINT_DIR=%{fingerprint_dir} \
         -DPROFILE_TARGET=%{?profile}

make %{?_smp_mflags}

%install
rm -fr %{buildroot}
%make_install
mkdir -p %{buildroot}%{tizen_dir}
mkdir -p %{buildroot}%{fingerprint_dir}

%files
%defattr(-,root,root,-)
%manifest %{name}.manifest
%license LICENSE
%{tizen_dir}/*
%{fingerprint_dir}/*
