%define name gnoise
%define version 0.1.15
%define release %mkrel 8

Version: 	%{version}
Summary: 	GTK-based wave file editor
Name: 		%{name}
Release: 	%{release}
License: 	GPL
Group: 		Sound
Source: 	%{name}-%{version}.tar.bz2
Patch0:		gnoise-0.1.15-fix-desktop.patch
URL: 		http://sourceforge.net/projects/gnoise/
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	libgtk+-devel
BuildRequires:	automake
BuildRequires:	desktop-file-utils

%description
GNoise is a GTK-based wave file editor for Linux capable of handling large 
files. A peaks display cache provides a fast, double-buffered display.

%prep

%setup -q
%patch0 -p0

%build
export FORCE_AUTOCONF_2_5=1
aclocal
automake -a -c
autoconf

%configure --disable-gnome

make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

desktop-file-install --vendor='' --delete-original \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%_datadir/gnome/apps/Multimedia/gnoise.desktop

%if %mdkversion < 200900
%post
%update_menus
%endif
 
%if %mdkversion < 200900
%postun
%clean_menus 
%endif

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README COPYING INSTALL TODO ChangeLog
%{_bindir}/*
%_datadir/pixmaps/gnoise.png
%_datadir/applications/*
