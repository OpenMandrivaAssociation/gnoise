Summary:	GTK-based wave file editor
Version:	0.1.15
Name:		gnoise
Release:	14
License:	GPLv2+
Group:		Sound
Url:		http://sourceforge.net/projects/gnoise/
Source0:	%{name}-%{version}.tar.bz2
Patch0:		gnoise-0.1.15-fix-desktop.patch
BuildRequires:	pkgconfig(gtk+)
BuildRequires:	desktop-file-utils

%description
GNoise is a GTK-based wave file editor for Linux capable of handling large
files. A peaks display cache provides a fast, double-buffered display.

%files
%doc README COPYING TODO ChangeLog
%{_bindir}/*
%{_datadir}/pixmaps/gnoise.png
%{_datadir}/applications/*

#----------------------------------------------------------------------------

%prep
%setup -q
%patch0 -p0
find . -name "Makefile*" -o -name "*.m4" |xargs sed -i -e 's,configure.in,configure.ac,g'
find . -name "configure*" -o -name "missing" |xargs sed -i -e 's,configure.in,configure.ac,g'

%build
export FORCE_AUTOCONF_2_5=1
aclocal
automake -a -c
autoconf

%configure2_5x --disable-gnome
make

%install
%makeinstall_std

desktop-file-install --vendor='' --delete-original \
	--dir=%{buildroot}%{_datadir}/applications \
	%{buildroot}%{_datadir}/gnome/apps/Multimedia/gnoise.desktop

