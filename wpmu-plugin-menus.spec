%define		plugin	menus
Summary:	WordPressMU plugin to Enable or disable WP Backend Menus
Name:		wpmu-plugin-%{plugin}
Version:	2.5.7
Release:	0.2
License:	GPL v2+
Group:		Applications/Publishing
Source0:	http://wpmudev.org/download/1477487882_ds_toggle_admin_menus.php
# Source0-md5:	54bd7c38e1848ae038a3341b4fa2c64c
URL:		http://wpmudev.org/project/Menus
BuildRequires:	rpmbuild(macros) >= 1.553
BuildRequires:	sed >= 4.0
BuildRequires:	unzip
Requires:	wpmu >= 2.7
Obsoletes:	wpmu-plugin-menu
BuildArch:	noarch
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		wp_root		%{_datadir}/wpmu
%define		wp_content	%{wp_root}/wp-content
%define		pluginsdir	%{wp_content}/mu-plugins
%define		_sysconfdir	/etc/webapps/wpmu

%description
Enable or disable WP Backend Menus via SiteAdmin->Options Menu.

If you need to hide the Themes or Import Menu, or don't want anyone
messing with their Permalinks menu, or are frightened by the Delete
Blog menu, this plugin will help.

%prep
%setup -qcT
%{__unzip} -qq %{SOURCE0}
%undos *.php

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{pluginsdir},%{_sysconfdir}}
cp -a Menus-%{version}.php $RPM_BUILD_ROOT%{pluginsdir}/%{plugin}.php

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{pluginsdir}/*.php
