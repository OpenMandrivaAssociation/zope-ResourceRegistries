%define product		ResourceRegistries
%define realVersion 1.3.4
%define release 1

%define version %(echo %{realVersion} | sed -e 's/-/./g')
%define zope_minver	2.7

%define zope_home	%{_prefix}/lib/zope
%define software_home	%{zope_home}/lib/python


Summary:	Registries for linked style sheet files and javascripts
Name:		zope-%{product}
Version:	%{version}
Release:	%mkrel %{release}
License:	GPL
Group:		System/Servers
Source:		http://plone.org/products/resourceregistries/releases/%{version}/ResourceRegistries-%{realVersion}.tar.bz2
URL:		http://plone.org/products/resourceregistries/
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildArch:	noarch
Requires:	zope >= %{zope_minver}
Requires:	zope-Archetypes


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




