%define Product ResourceRegistries
%define product resourceregistries
%define name    zope-%{Product}
%define version 1.4.1
%define bad_version %(echo %{version} | sed -e 's/\\./-/g')
%define release %mkrel 4

%define zope_minver	2.7
%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	Registries for linked style sheet files and javascripts
License:	GPL
Group:		System/Servers
URL:        http://plone.org/products/%{product}
Source:     http://plone.org/products/%{product}/releases/%{version}/%{product}-%{bad_version}.tgz
Requires:	zope >= %{zope_minver}
Requires:	zope-Archetypes
BuildArch:  noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}


%description
A registry for linked Stylesheet files and Javascripts.
This registry is mainly aimed at solving the following usecases:
- Enable product authors to register stylesheets with their product
  installers without having to resort to override either header.pt or
  ploneCustom.css creating potential conflicts with other products.
- Enable more componentialization of the stylesheets provided with Plone
  (and other products) without having to increase the number of http
  requests for a Plone page.
- Enable condition checking on stylesheets. Great for variable
  look-and-feel for groups/roles/folders/departments/content-types/etc
- Enable inline dynamic stylesheets. For those style rules that should
  vary for each request. Mainly used for things like header-bar-
  backgroundimages, department colors etc.
- Enable developers to activate/deactivate their styles in a simpler way


%prep
%setup -c -q

rm -rf `find -type d -name .svn`

%build
# Not much, eh? :-)


%install
%{__rm} -rf %{buildroot}
%{__mkdir_p} %{buildroot}/%{software_home}/Products
%{__cp} -a * %{buildroot}%{software_home}/Products/


%clean
%{__rm} -rf %{buildroot}

%post
if [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%postun
if [ -f "%{_prefix}/bin/zopectl" ] && [ "`%{_prefix}/bin/zopectl status`" != "daemon manager not running" ] ; then
	service zope restart
fi

%files
%defattr(-, root, root, 0755)
%{software_home}/Products/*




