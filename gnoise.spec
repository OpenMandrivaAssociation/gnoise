%define name gnoise
%define version 0.1.15
%define release %mkrel 12

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


%changelog
* Fri Dec 10 2010 Oden Eriksson <oeriksson@mandriva.com> 0.1.15-12mdv2011.0
+ Revision: 619013
- the mass rebuild of 2010.0 packages

* Fri Sep 04 2009 Thierry Vignaud <tv@mandriva.org> 0.1.15-11mdv2010.0
+ Revision: 429224
- rebuild

* Thu Jul 24 2008 Thierry Vignaud <tv@mandriva.org> 0.1.15-10mdv2009.0
+ Revision: 246346
- rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

* Fri Dec 21 2007 Olivier Blin <oblin@mandriva.com> 0.1.15-8mdv2008.1
+ Revision: 136447
- restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

* Fri Aug 31 2007 Funda Wang <fwang@mandriva.org> 0.1.15-8mdv2008.0
+ Revision: 76719
- Use desktop patch to fix Type
- Add gtk category
- drop old menu
- correct desktop file

  + Thierry Vignaud <tv@mandriva.org>
    - kill desktop-file-validate's error: string list key "Categories" in group "Desktop Entry" does not have a semicolon (";") as trailing character


* Tue Jan 09 2007 Crispin Boylan <crisb@mandriva.org> 0.1.15-7mdv2007.0
+ Revision: 106211
- Really disable gnome
- Import gnoise

* Sat Aug 19 2006 Lenny Cartier <lenny@mandriva.com> 0.1.15-6mdv2007.0
- xdg

* Fri Nov 05 2004 Christiaan Welvaart <cjw@daneel.dyndns.org> 0.1.15-5mdk
- add BuildRequires: libgtk+-devel
- use current autotools

* Fri Feb 20 2004 Lenny Cartier <lenny@mandrakesoft.com> 0.1.15-4mdk
- 0.1.15

