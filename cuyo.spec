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



%changelog
* Sun Dec 05 2010 Oden Eriksson <oeriksson@mandriva.com> 2.1.1-4mdv2011.0
+ Revision: 610181
- rebuild

* Fri Apr 30 2010 Funda Wang <fwang@mandriva.org> 2.1.1-3mdv2010.1
+ Revision: 541190
- simplify BRs

* Fri Apr 30 2010 Funda Wang <fwang@mandriva.org> 2.1.1-2mdv2010.1
+ Revision: 541189
- fix build with gcc44

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Wed Apr 01 2009 Antoine Ginies <aginies@mandriva.com> 2.1.1-1mdv2009.1
+ Revision: 363367
- release 2.1.1

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

  + Pixel <pixel@mandriva.com>
    - rpm filetriggers deprecates update_menus/update_scrollkeeper/update_mime_database/update_icon_cache/update_desktop_database/post_install_gconf_schemas

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Tue Dec 18 2007 Thierry Vignaud <tv@mandriva.org> 2.0-1mdv2008.1
+ Revision: 132936
- auto-convert XDG menu entry
- kill re-definition of %%buildroot on Pixel's request

  + Antoine Ginies <aginies@mandriva.com>
    - add SDL_image in buildrequires tag
    - add SDL mixer and image buildrequire
    - add sdl-devel buildrequire
    - release 2.0-alpha1
    - Import cuyo



* Fri Jan 14 2005 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.8.5-1mdk
- 1.8.5

* Sun Jul 11 2004 Michael Scherer <misc@mandrake.org> 1.8.3-2mdk 
- rebuild for new gcc

* Tue Oct 14 2003 Per Øyvind Karlsen <peroyvind@linux-mandrake.com> 1.8.3-1mdk
- 1.8.3
- moved stuff to %%{_gamesbindir} and %%{_gamesdatadir}
- compile with $RPM_OPT_FLAGs
- added menu item
- added icons
- cleanups
- buildrequires

* Mon Aug 18 2003 Antoine Ginies <aginies@bi.mandrakesoft.com> 1.7.0-1mdk
- new release

* Tue Feb 11 2003 Antoine Ginies <aginies@mandrakesoft.com> 1.6.1-2mdk
- add description and correct Group

* Tue Feb 11 2003 Antoine Ginies <aginies@bi.mandrakesoft.com> 1.6.1-1mdk
- first release for mandrakesoft.
