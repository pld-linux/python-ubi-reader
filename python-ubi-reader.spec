# Conditional build:
%bcond_without	python2 # CPython 2.x module
%bcond_without	python3 # CPython 3.x module

%define		module		ubireader
%define		egg_name	ubi_reader
%define		pypi_name	ubi-reader
Summary:	Python scripts for reading information about and extracting data from UBI and UBIFS images
Name:		python-%{pypi_name}
Version:	0.7.2
Release:	1
License:	GPL v3+
Group:		Libraries/Python
Source0:	https://pypi.debian.net/ubi-reader/ubi_reader-%{version}.tar.gz
URL:		https://github.com/jrspruitt/ubi_reader
%if %{with python2}
BuildRequires:	python-modules >= 1:2.5
BuildRequires:	python-setuptools
%endif
%if %{with python3}
BuildRequires:	python3-modules >= 1:3.2
BuildRequires:	python3-setuptools
%endif
BuildRequires:	rpm-pythonprov
BuildRequires:	rpmbuild(macros) >= 1.714
Requires:	python-modules >= 1:2.5
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
UBI Reader is a Python module and collection of scripts capable of
extracting the contents of UBI and UBIFS images, along with analyzing
these images to determine the parameter settings to recreate them
using the mtd-utils tools.

%package -n python3-%{pypi_name}
Summary:	Python scripts for reading information about and extracting data from UBI and UBIFS images
Group:		Libraries/Python
Requires:	python3-modules >= 1:3.2

%description -n python3-%{pypi_name}
UBI Reader is a Python module and collection of scripts capable of
extracting the contents of UBI and UBIFS images, along with analyzing
these images to determine the parameter settings to recreate them
using the mtd-utils tools.

%prep
%setup -q -n %{egg_name}-%{version}

%build
%if %{with python2}
%py_build
%endif

%if %{with python3}
%py3_build
%endif

%install
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%py_install
%py_postclean
%endif

%if %{with python3}
%py3_install
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%if %{with python2}
%files
%defattr(644,root,root,755)
%doc README.md
%{py_sitescriptdir}/%{module}
%{py_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif

%if %{with python3}
%files -n python3-%{pypi_name}
%defattr(644,root,root,755)
%doc README.md
%attr(755,root,root) %{_bindir}/ubireader_display_blocks
%attr(755,root,root) %{_bindir}/ubireader_display_info
%attr(755,root,root) %{_bindir}/ubireader_extract_files
%attr(755,root,root) %{_bindir}/ubireader_extract_images
%attr(755,root,root) %{_bindir}/ubireader_list_files
%attr(755,root,root) %{_bindir}/ubireader_utils_info
%{py3_sitescriptdir}/%{module}
%{py3_sitescriptdir}/%{egg_name}-%{version}-py*.egg-info
%endif
