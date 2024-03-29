#
# This file is auto-generated. DO NOT EDIT
# Generated by: autospec.py
#
Name     : nocasedict
Version  : 1.0.2
Release  : 16
URL      : https://files.pythonhosted.org/packages/ad/80/40b0bfddbea87c6e7d400171b42ee1a82b954114d706a8871e0eb4225c60/nocasedict-1.0.2.tar.gz
Source0  : https://files.pythonhosted.org/packages/ad/80/40b0bfddbea87c6e7d400171b42ee1a82b954114d706a8871e0eb4225c60/nocasedict-1.0.2.tar.gz
Summary  : A case-insensitive ordered dictionary for Python
Group    : Development/Tools
License  : LGPL-2.1
Requires: nocasedict-license = %{version}-%{release}
Requires: nocasedict-python = %{version}-%{release}
Requires: nocasedict-python3 = %{version}-%{release}
Requires: six
BuildRequires : buildreq-distutils3
BuildRequires : six

%description
=============================================================

%package license
Summary: license components for the nocasedict package.
Group: Default

%description license
license components for the nocasedict package.


%package python
Summary: python components for the nocasedict package.
Group: Default
Requires: nocasedict-python3 = %{version}-%{release}

%description python
python components for the nocasedict package.


%package python3
Summary: python3 components for the nocasedict package.
Group: Default
Requires: python3-core
Provides: pypi(nocasedict)
Requires: pypi(six)

%description python3
python3 components for the nocasedict package.


%prep
%setup -q -n nocasedict-1.0.2
cd %{_builddir}/nocasedict-1.0.2

%build
export http_proxy=http://127.0.0.1:9/
export https_proxy=http://127.0.0.1:9/
export no_proxy=localhost,127.0.0.1,0.0.0.0
export LANG=C.UTF-8
export SOURCE_DATE_EPOCH=1609793265
export GCC_IGNORE_WERROR=1
export AR=gcc-ar
export RANLIB=gcc-ranlib
export NM=gcc-nm
export CFLAGS="$CFLAGS -O3 -ffat-lto-objects -flto=4 "
export FCFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export FFLAGS="$FFLAGS -O3 -ffat-lto-objects -flto=4 "
export CXXFLAGS="$CXXFLAGS -O3 -ffat-lto-objects -flto=4 "
export MAKEFLAGS=%{?_smp_mflags}
python3 setup.py build

%install
export MAKEFLAGS=%{?_smp_mflags}
rm -rf %{buildroot}
mkdir -p %{buildroot}/usr/share/package-licenses/nocasedict
cp %{_builddir}/nocasedict-1.0.2/LICENSE %{buildroot}/usr/share/package-licenses/nocasedict/d4b196a7e20ce07168dba4cb390677d32586ba88
python3 -tt setup.py build  install --root=%{buildroot}
echo ----[ mark ]----
cat %{buildroot}/usr/lib/python3*/site-packages/*/requires.txt || :
echo ----[ mark ]----

%files
%defattr(-,root,root,-)

%files license
%defattr(0644,root,root,0755)
/usr/share/package-licenses/nocasedict/d4b196a7e20ce07168dba4cb390677d32586ba88

%files python
%defattr(-,root,root,-)

%files python3
%defattr(-,root,root,-)
/usr/lib/python3*/*
