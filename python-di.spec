%if 0%{?rhel} && 0%{?rhel} <= 5
%{!?python_sitelib: %global python_sitelib %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib())")}
%{!?python_sitearch: %global python_sitearch %(%{__python} -c "from distutils.sysconfig import get_python_lib; print(get_python_lib(1))")}
%endif

Name:           python-di
Version:        0.3
Release:        1%{?dist}
Summary:        Python library for dependency injection support

License:        GPLv2+
URL:            http://fedorapeople.org/cgit/msivak/public_git/python-di.git/

# get the current source file using the following two commands
# git clone git://fedorapeople.org/home/fedora/msivak/public_git/python-di.git
# cd python-di; python setup.py sdist
# it will be in the dist directory
Source0:        http://pypi.python.org/packages/source/d/di/di-%{version}.tar.gz

BuildRequires:  python-setuptools-devel
BuildRequires:  python-nose
BuildRequires:  python2-devel     
BuildArch:      noarch

%description
This python package provides a "di" module. The module contains a couple of
decorators which try to implement the Dependency Injection (IoC) pattern
without requiring the user to change local variables in his methods.

It is intended to be used in unit testing environments.

%prep
%setup -q -n di-%{version}

# remove upstream egg-info
rm -rf *.egg-info

%build
%{__python} setup.py build

%install
%{__python} setup.py install --skip-build --root $RPM_BUILD_ROOT
rm -rf ${buildroot}%{python_sitelib}/setuptools/tests

%check
%{__python} setup.py nosetests

%files
%{python_sitelib}/di
%{python_sitelib}/di-*.egg-info

%doc README COPYING

%changelog
* Fri Mar 22 2013 Martin Sivak <msivak@euryale.brq.redhat.com> - 0.3-1
- Rename the register method to _inject_

* Thu Feb 14 2013 Fedora Release Engineering <rel-eng@lists.fedoraproject.org> - 0.2-2
- Rebuilt for https://fedoraproject.org/wiki/Fedora_19_Mass_Rebuild

* Thu Dec  6 2012 Martin Sivak <msivak@euryale.brq.redhat.com> - 0.2-1
- DiRegistry support for accessing attributes of the decorated object

* Fri Nov 23 2012 Martin Sivak <msivak@euryale.brq.redhat.com> - 0.1-1
- Inital release

