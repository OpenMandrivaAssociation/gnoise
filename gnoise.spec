%define name gnoise
%define version 0.1.15
%define release %mkrel 7


Version: 	%{version}
Summary: 	GTK-based wave file editor
Name: 		%{name}
Release: 	%{release}
License: 	GPL
Group: 		Sound
Source: 	%{name}-%{version}.tar.bz2
URL: 		http://sourceforge.net/projects/gnoise/
BuildRoot: 	%{_tmppath}/%{name}-buildroot
BuildRequires:	libgtk+-devel
BuildRequires:	automake1.8

%description
GNoise is a GTK-based wave file editor for Linux capable of handling large 
files. A peaks display cache provides a fast, double-buffered display.

%prep

%setup -q 

%build
export FORCE_AUTOCONF_2_5=1
aclocal-1.8
automake-1.8 -a -c
autoconf

%configure --disable-gnome

make

%install
rm -rf $RPM_BUILD_ROOT

%makeinstall

(cd $RPM_BUILD_ROOT
mkdir -p ./usr/lib/menu
cat > ./usr/lib/menu/%{name} <<EOF
?package(%{name}):\
command="/usr/bin/gnoise"\
title="Gnoise"\
longtitle="Wave file editor"\
needs="x11"\
icon="sound_section.png"\
section="Multimedia/Sound" xdg="true"
EOF
)

mkdir -p %{buildroot}%{_datadir}/applications
cat > %{buildroot}%{_datadir}/applications/mandriva-%{name}.desktop << EOF
[Desktop Entry]
Name=%{name}
Comment=%{Summary}
Exec=%{name}
Icon=%{name}
Terminal=false
Type=Application
Categories=X-MandrivaLinux-Internet-WebBrowsers
EOF

rm -rf %{buildroot}%_datadir/gnome/apps/Multimedia/gnoise.desktop

%post
%update_menus
 
%postun
%clean_menus 

%clean
rm -rf $RPM_BUILD_ROOT

%files
%defattr (-,root,root)
%doc README COPYING INSTALL TODO ChangeLog
%{_bindir}/*
%{_menudir}/*
%_datadir/pixmaps/gnoise.png
%_datadir/applications/*


