%global username steam

Name:           steamos-compositor
Version:        1.31
Release:        1%{?dist}
Summary:        SteamOS Compositor

License:        BSD
URL:            http://store.steampowered.com/steamos/
Source0:        http://repo.steampowered.com/steamos/pool/main/s/%{name}/%{name}_%{version}.tar.xz
Source1:        steam-as-account
Source2:        steam-as-icon
Patch0:         %{name}-preload.patch
Patch1:         %{name}-glintptr.patch

BuildRequires:  autoconf
BuildRequires:  automake
BuildRequires:  desktop-file-utils
BuildRequires:  libXxf86vm-devel
BuildRequires:  libX11-devel
BuildRequires:  libXext-devel
BuildRequires:  libXrender-devel
BuildRequires:  libXcomposite-devel
BuildRequires:  mesa-libGL-devel
BuildRequires:  SDL_image-devel
BuildRequires:  systemd-devel

%description
Provides graphics compositor services for the full-screen environment of
SteamOS.

%package -n steamos-session
Summary:        SteamOS desktop session
BuildArch:      noarch

Requires:       %{name} = %{version}-%{release}
Requires(pre):  shadow-utils
Requires(pre):  openssl
# Require all SteamOS bits here
Requires:       steam
Requires:       steamos-modeswitch-inhibitor
Requires:       steamos-backgrounds
Requires:       steamos-base-files

%description -n steamos-session
The steamos-session package contains required files for starting a desktop
session with the Steam client configured in SteamOS mode.

%prep
%setup -q
%patch0 -p1
%patch1 -p1
sed -i -e '/Encoding/d' -e 's/steamicon.png/steamicon/g' \
    .%{_datadir}/xsessions/steamos.desktop

%build
autoreconf -vif
%configure
make %{?_smp_mflags}

%install
%make_install
install -p -m644 -D .%{_datadir}/icons/steam/arrow.png \
    %{buildroot}%{_datadir}/icons/steam/arrow.png
install -p -m644 -D .%{_datadir}/xsessions/steamos.desktop \
    %{buildroot}%{_datadir}/xsessions/steamos.desktop
install -p -m755 -D .%{_bindir}/steamos-session \
    %{buildroot}%{_bindir}/steamos-session

install -p -m644 -D %{SOURCE1} %{buildroot}%{_sharedstatedir}/AccountsService/users/steam
install -p -m644 -D %{SOURCE2} %{buildroot}%{_sharedstatedir}/AccountsService/icons/steam

desktop-file-validate %{buildroot}%{_datadir}/xsessions/steamos.desktop

rm -fr %{buildroot}%{_docdir}/%{name}

%pre -n steamos-session
getent group %username >/dev/null || groupadd %username
getent passwd %username >/dev/null || useradd \
    -g %username -d /home/%username \
    -s /bin/bash -c "SteamOS" \
    -p $(openssl passwd -1 %username) \
    %username
exit 0

%files
%doc debian/copyright debian/changelog
%{_bindir}/loadargb_cursor
%{_bindir}/steamcompmgr
%{_bindir}/udev_is_boot_vga
%{_datadir}/icons/steam

%files -n steamos-session
%{_bindir}/steamos-session
%{_datadir}/xsessions/steamos.desktop
%{_sharedstatedir}/AccountsService/users/steam
%{_sharedstatedir}/AccountsService/icons/steam

%changelog
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
