#$Revision: 1.3 $, $Date: 2004-04-17 10:27:29 $

%define         _name Lila

Summary:	KDE icons - %{_name}
Summary(pl):	Motyw ikon do KDE - %{_name}
Name:		kde-icons-%{_name}
Version:	0.5
Release:	1
License:	GPL
Group:		Themes
Source0:	http://www.kde-look.org/content/files/11492-lilasvg-%{version}.tar.bz2
# Source0-md5:	60ddc1d959192678d46c6e28c3a8f37f
Source1:	generate.py
URL:		http://www.kde-look.org/content/show.php?content=11492
# See also http://programmer-art.org/index.php?page=gentoo
Requires:	kdelibs
BuildRequires:	librsvg
BuildRequires:	/usr/bin/python
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)
BuildArch:	noarch

%description
%{_name} is a violet icon theme ported from GNOME to KDE.

%description -l pl
%{_name} to fioletowy motyw ikon sportowany z GNOME.

%prep

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT%{_iconsdir}

%{__tar} xjf %{SOURCE0} -C $RPM_BUILD_ROOT%{_iconsdir}/
cd  $RPM_BUILD_ROOT%{_iconsdir}
rm -f ./generate.py
install %{SOURCE1} ./
./generate.py

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr(644,root,root,755)
%{_iconsdir}/*
