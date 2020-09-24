#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-common-extensions
Version  : 0.2.1
Release  : 11
URL      : https://files.pythonhosted.org/packages/74/20/25764798e296518b7f5ea3053b6ac22fbc4da7fcac730da54c389c0e3e7e/colcon-common-extensions-0.2.1.tar.gz
Source0  : https://files.pythonhosted.org/packages/74/20/25764798e296518b7f5ea3053b6ac22fbc4da7fcac730da54c389c0e3e7e/colcon-common-extensions-0.2.1.tar.gz
Summary  : Meta package aggregating colcon-core and common extensions.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-common-extensions-python = %{version}-%{release}
Requires: colcon-common-extensions-python3 = %{version}-%{release}
Requires: colcon-bash
Requires: colcon-cmake
Requires: colcon-core
Requires: colcon-defaults
Requires: colcon-devtools
Requires: colcon-library-path
Requires: colcon-metadata
Requires: colcon-output
Requires: colcon-package-information
Requires: colcon-package-selection
Requires: colcon-parallel-executor
Requires: colcon-powershell
Requires: colcon-python-setup-py
Requires: colcon-recursive-crawl
Requires: colcon-ros
Requires: colcon-test-result
Requires: colcon-zsh
BuildRequires : buildreq-distutils3
BuildRequires : colcon-bash
BuildRequires : colcon-cmake
BuildRequires : colcon-core
BuildRequires : colcon-defaults
BuildRequires : colcon-devtools
BuildRequires : colcon-library-path
BuildRequires : colcon-metadata
BuildRequires : colcon-output
BuildRequires : colcon-package-information
BuildRequires : colcon-package-selection
BuildRequires : colcon-parallel-executor
BuildRequires : colcon-powershell
BuildRequires : colcon-python-setup-py
BuildRequires : colcon-recursive-crawl
BuildRequires : colcon-ros
BuildRequires : colcon-test-result
BuildRequires : colcon-zsh

%description
colcon-common-extensions
========================
A meta package aggregating `colcon-core <https://github.com/colcon/colcon-core>`_ as well as a set of common extensions.

%package python
Summary: python components for the colcon-common-extensions package.
Group: Default
Requires: colcon-common-extensions-python3 = %{version}-%{release}

%description python
python components for the colcon-common-extensions package.


%package python3
Summary: python3 components for the colcon-common-extensions package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-common-extensions package.


%prep
%setup -q -n colcon-common-extensions-0.2.1

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1571405169
# -Werror is for werrorists
export GCC_IGNORE_WERROR=1
export CFLAGS="$CFLAGS -fno-lto "
export FCFLAGS="$CFLAGS -fno-lto "
export FFLAGS="$CFLAGS -fno-lto "
export CXXFLAGS="$CXXFLAGS -fno-lto "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
