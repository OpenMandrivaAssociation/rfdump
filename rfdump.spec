Summary:	An RFID tags detector
Name:		rfdump
Version:	1.6
Release:	1
Group:		Education
License:	GPLv2+
URL:		https://www.rfdump.org
Source0:	https://www.rfdump.org/dl/%{name}-%{version}.tar.bz2
Patch0:		%{name}-1.6-optflags.patch
Patch1:		%{name}-1.6-format-security.patch
# (archlinux)
Patch2:		%{name}-1.6-drop-libglade.patch
BuildRequires:	pkgconfig(expat)
BuildRequires:	pkgconfig(gtk+-3.0)
#BuildRequires:	pkgconfig(libglade-2.0)

%description
RFDump is a tool to detect RFID-Tags and show their meta information:
Tag ID, Tag Type, manufacturer etc. The user data memory of a tag can
be displayed and modified using either a Hex or an ASCII editor. Tag
contents can be stored and loaded using a specific XML fomrat. This
effectively allows to copy data from one tag to another. In addition,
the integrated cookie feature demonstrates how easy it is for a
company to abuse RFID technology to spy on their customers.  RFDump
works with the ACG Multi-Tag Reader or similar card reader hardware.

%prep
%autosetup -p1

%files 
%doc AUTHORS NEWS README TODO
%license COPYING
%{_bindir}/%{name}
%{_datadir}/applications/%{name}.desktop
%{_datadir}/%{name}/
%{_datadir}/pixmaps/%{name}.png

#----------------------------------------------------------------------

%build
export CFLAGS="%{optflags} -fcommon"
autoreconf -fiv
%configure
%make_build 

%install
%make_install

