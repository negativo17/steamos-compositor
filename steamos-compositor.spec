Name:           steamos-compositor
Version:        1.35
Release:        1%{?dist}
Summary:        SteamOS Compositor
License:        BSD
URL:            http://store.steampowered.com/steamos/

Source0:        http://repo.steamstatic.com/steamos/pool/main/s/%{name}/%{name}_%{version}.tar.xz

Patch0:         %{name}-1.35-steamos-session.patch
Patch1:         %{name}-1.34-glintptr.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  gcc
BuildRequires:  pkgconfig(gl)
BuildRequires:  pkgconfig(libudev)
BuildRequires:  pkgconfig(SDL_image)
BuildRequires:  pkgconfig(x11)
BuildRequires:  pkgconfig(xcomposite)
BuildRequires:  pkgconfig(xdamage)
BuildRequires:  pkgconfig(xext)
BuildRequires:  pkgconfig(xrender)
BuildRequires:  pkgconfig(xxf86vm)

Requires:       steam
Requires:       steamos-modeswitch-inhibitor
Requires:       steamos-base-files

%description
Provides graphics compositor services for the full-screen environment of SteamOS
and required files for starting a desktop session with the Steam client
configured in SteamOS mode.

%prep
%autosetup -p1

%build
autoreconf -vif
%configure
%make_install

%install
%make_install

install -p -m755 -D .%{_bindir}/steamos-session %{buildroot}%{_bindir}/steamos-session

install -p -m644 -D .%{_datadir}/icons/steam/arrow.png %{buildroot}%{_datadir}/icons/steam/arrow.png

desktop-file-install --set-icon=steam --dir=%{buildroot}%{_datadir}/xsessions/ \
    .%{_datadir}/xsessions/steamos.desktop \

rm -fr %{buildroot}%{_docdir}/%{name}

%check
desktop-file-validate %{buildroot}%{_datadir}/xsessions/steamos.desktop

%files
%doc debian/copyright debian/changelog
%{_bindir}/loadargb_cursor
%{_bindir}/steamcompmgr
%{_bindir}/steamos-session
%{_bindir}/udev_is_boot_vga
%{_datadir}/icons/steam/
%{_datadir}/xsessions/steamos.desktop

%changelog
* Sun Jan 27 2019 Simone Caronni <negativo17@gmail.com> - 1.35-1
- Update to version 1.35.
- Rework package completely.

* Sat Apr 15 2017 Simone Caronni <negativo17@gmail.com> - 1.34-1
- Update to 1.34.

* Fri Apr 01 2016 Simone Caronni <negativo17@gmail.com> - 1.33-1
- Update to 1.33.

* Sat Oct 31 2015 Simone Caronni <negativo17@gmail.com> - 1.31-1
- Update to version 1.31.

* Fri Jul 31 2015 Simone Caronni <negativo17@gmail.com> - 1.29-1
- Update to 1.29

* Thu May 21 2015 Simone Caronni <negativo17@gmail.com> - 1.24-2
- Remove Encoding and icon suffix in steamos.desktop session file.

* Fri Apr 24 2015 Simone Caronni <negativo17@gmail.com> - 1.24-1
- Update to 1.24.
- Add patch for GLintptr change:
  https://bugs.freedesktop.org/show_bug.cgi?id=83631

* Wed Oct 01 2014 Simone Caronni <negativo17@gmail.com> - 1.23-1
- Update to 1.23.

* Tue Aug 05 2014 Simone Caronni <negativo17@gmail.com> - 1.21-1
- Update to 1.21.

* Tue Jul 29 2014 Simone Caronni <negativo17@gmail.com> - 1.20-1
- Update to 1.20.

* Sun Jun  8 2014 Simone Caronni <negativo17@gmail.com> - 1.19-1
- First build.
