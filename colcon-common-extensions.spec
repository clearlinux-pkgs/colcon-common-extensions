#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : colcon-common-extensions
Version  : 0.2.0
Release  : 6
URL      : https://files.pythonhosted.org/packages/66/41/72f618236c6bac205abe253479100df09fddde237f3949f247e70b6e081c/colcon-common-extensions-0.2.0.tar.gz
Source0  : https://files.pythonhosted.org/packages/66/41/72f618236c6bac205abe253479100df09fddde237f3949f247e70b6e081c/colcon-common-extensions-0.2.0.tar.gz
Summary  : Meta package aggregating colcon-core and common extensions.
Group    : Development/Tools
License  : Apache-2.0
Requires: colcon-common-extensions-python3
Requires: colcon-common-extensions-python
Requires: colcon-bash
Requires: colcon-cmake
Requires: colcon-core
Requires: colcon-defaults
Requires: colcon-devtools
Requires: colcon-library-path
Requires: colcon-metadata
Requires: colcon-output
Requires: colcon-package-information
Requires: colcon-parallel-executor
Requires: colcon-powershell
Requires: colcon-python-setup-py
Requires: colcon-recursive-crawl
Requires: colcon-ros
Requires: colcon-test-result
Requires: colcon-zsh
BuildRequires : buildreq-distutils3

%description
========================

%package python
Summary: python components for the colcon-common-extensions package.
Group: Default
Requires: colcon-common-extensions-python3

%description python
python components for the colcon-common-extensions package.


%package python3
Summary: python3 components for the colcon-common-extensions package.
Group: Default
Requires: python3-core

%description python3
python3 components for the colcon-common-extensions package.


%prep
%setup -q -n colcon-common-extensions-0.2.0

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C
export SOURCE_DATE_EPOCH=1533001614
python3 setup.py build -b py3

%install
rm -rf %{buildroot}
python3 -tt setup.py build -b py3 install --root=%{buildroot}
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
