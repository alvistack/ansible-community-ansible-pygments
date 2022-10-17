# Copyright 2022 Wong Hoi Sing Edison <hswong3i@pantarei-design.com>
#
# Licensed under the Apache License, Version 2.0 (the "License");
# you may not use this file except in compliance with the License.
# You may obtain a copy of the License at
#
#     http://www.apache.org/licenses/LICENSE-2.0
#
# Unless required by applicable law or agreed to in writing, software
# distributed under the License is distributed on an "AS IS" BASIS,
# WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
# See the License for the specific language governing permissions and
# limitations under the License.

%global debug_package %{nil}

Name: python-ansible-pygments
Epoch: 100
Version: 0.1.0
Release: 1%{?dist}
BuildArch: noarch
Summary: Pygments lexer and style Ansible snippets
License: BSD-2-Clause
URL: https://github.com/ansible-community/ansible-pygments/tags
Source0: %{name}_%{version}.orig.tar.gz
BuildRequires: fdupes
BuildRequires: python-rpm-macros
BuildRequires: python3-devel
BuildRequires: python3-setuptools

%description
This project provides a Pygments lexer that is able to handle Ansible
output. It may be used anywhere Pygments is integrated. The lexer is
registered globally under the name ansible-output.

%prep
%autosetup -T -c -n %{name}_%{version}-%{release}
tar -zx -f %{S:0} --strip-components=1 -C .

%build
%py3_build

%install
%py3_install
find %{buildroot}%{python3_sitelib} -type f -name '*.pyc' -exec rm -rf {} \;
fdupes -qnrps %{buildroot}%{python3_sitelib}

%check

%if 0%{?suse_version} > 1500
%package -n python%{python3_version_nodots}-ansible-pygments
Summary: Pygments lexer and style Ansible snippets
Requires: python3
Requires: python3-Pygments >= 2.4.0
Provides: python3-ansible-pygments = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-pygments) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-pygments = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-pygments) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-pygments = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-pygments) = %{epoch}:%{version}-%{release}

%description -n python%{python3_version_nodots}-ansible-pygments
This project provides a Pygments lexer that is able to handle Ansible
output. It may be used anywhere Pygments is integrated. The lexer is
registered globally under the name ansible-output.

%files -n python%{python3_version_nodots}-ansible-pygments
%license LICENSE.md
%{python3_sitelib}/*
%endif

%if 0%{?sle_version} > 150000
%package -n python3-ansible-pygments
Summary: Pygments lexer and style Ansible snippets
Requires: python3
Requires: python3-Pygments >= 2.4.0
Provides: python3-ansible-pygments = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-pygments) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-pygments = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-pygments) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-pygments = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-pygments) = %{epoch}:%{version}-%{release}

%description -n python3-ansible-pygments
This project provides a Pygments lexer that is able to handle Ansible
output. It may be used anywhere Pygments is integrated. The lexer is
registered globally under the name ansible-output.

%files -n python3-ansible-pygments
%license LICENSE.md
%{python3_sitelib}/*
%endif

%if !(0%{?suse_version} > 1500) && !(0%{?sle_version} > 150000)
%package -n python3-ansible-pygments
Summary: Pygments lexer and style Ansible snippets
Requires: python3
Requires: python3-pygments >= 2.4.0
Provides: python3-ansible-pygments = %{epoch}:%{version}-%{release}
Provides: python3dist(ansible-pygments) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}-ansible-pygments = %{epoch}:%{version}-%{release}
Provides: python%{python3_version}dist(ansible-pygments) = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}-ansible-pygments = %{epoch}:%{version}-%{release}
Provides: python%{python3_version_nodots}dist(ansible-pygments) = %{epoch}:%{version}-%{release}

%description -n python3-ansible-pygments
This project provides a Pygments lexer that is able to handle Ansible
output. It may be used anywhere Pygments is integrated. The lexer is
registered globally under the name ansible-output.

%files -n python3-ansible-pygments
%license LICENSE.md
%{python3_sitelib}/*
%endif

%changelog
