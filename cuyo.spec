%define	name	cuyo
%define	version	2.1.1
%define	release	%mkrel 4
%define	Summary A tetris like game
%define prerelease alpha1

Summary:	%{Summary}
Name:		%{name}
Url:		http://www.karimmi.de/cuyo/
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}.tar.bz2
Source1:	%{name}-16x16.png
Source2:	%{name}-32x32.png
Source3:	%{name}-48x48.png
Patch0:		cuyo-2.1.1-gcc44.patch
License:	GPL
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	SDL-devel
BuildRequires:	SDL_image-devel
BuildRequires:	SDL_mixer-devel

%description
Cuyo is a Tetris like game, There is many different level,
with different rules. We can play it with two players.

%prep
%setup -q -n %{name}-%{version}
%patch0 -p0

%build
%configure2_5x	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir}
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall_std

mkdir -p $RPM_BUILD_ROOT%{_datadir}/applications/
cat << EOF > %buildroot%{_datadir}/applications/mandriva-%{name}.desktop
[Desktop Entry]
Type=Application
Exec=%{_gamesbindir}/%{name}                
Icon=%{name}                                
Categories=Game;ArcadeGame;                
Name=Cuyo                
Comment=%{Summary}
EOF

%{__install} %{SOURCE1} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
%{__install} %{SOURCE2} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
%{__install} %{SOURCE3} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%if %mdkversion < 200900
%post
%update_menus
%endif

%if %mdkversion < 200900
%postun
%clean_menus
%endif

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}
%defattr(644,root,root,755)
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_mandir}/man6/cu*.6*
%{_datadir}/applications/mandriva-%{name}.desktop
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
%{_datadir}/games/applications/%name.desktop
%{_datadir}/games/icons/hicolor/32x32/apps/%name.png
%{_datadir}/games/icons/hicolor/64x64/apps/%name.png

