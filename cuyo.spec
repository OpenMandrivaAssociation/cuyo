%define	name	cuyo
%define	version	2.0
%define	release	%mkrel 1
%define	Summary A tetris like game
%define prerelease alpha1

Summary:	%{Summary}
Name:		%{name}
Url:		http://www.karimmi.de/cuyo/
Version:	%{version}
Release:	%{release}
Source0:	%{name}-%{version}-%{prerelease}.tar.bz2
Source1:	%{name}-16x16.png
Source2:	%{name}-32x32.png
Source3:	%{name}-48x48.png
License:	GPL
Group:		Games/Arcade
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-buildroot
BuildRequires:	qt3-devel >= 3.1 bison flex SDL1.2-devel
BuildRequires:  SDL_image1.2-devel, SDL_mixer1.2-devel
%description
Cuyo is a Tetris like game, There is many different level,
with different rules. We can play it with two players.

%prep
%setup -q -n %{name}-%{version}-%{prerelease}

%build
export MOC=%{_prefix}/lib/qt3/bin/moc
export UIC=%{_prefix}/lib/qt3/bin/uic
%configure	--bindir=%{_gamesbindir} \
		--datadir=%{_gamesdatadir} \
		--with-qt-dir=%{_prefix}/lib/qt3
%make

%install
%{__rm} -rf $RPM_BUILD_ROOT
%makeinstall	bindir=$RPM_BUILD_ROOT%{_gamesbindir} \
		datadir=$RPM_BUILD_ROOT%{_gamesdatadir}

%{__install} -d $RPM_BUILD_ROOT%{_menudir}
%{__cat} <<EOF > $RPM_BUILD_ROOT%{_menudir}/%{name}
?package(%{name}):command="%{_gamesbindir}/%{name}" \
                icon=%{name}.png \
                needs="x11" \
                section="More Applications/Games/Arcade" \
                title="Cuyo"\
                longtitle="%{Summary}"
EOF

%{__install} %{SOURCE1} -D $RPM_BUILD_ROOT%{_miconsdir}/%{name}.png
%{__install} %{SOURCE2} -D $RPM_BUILD_ROOT%{_iconsdir}/%{name}.png
%{__install} %{SOURCE3} -D $RPM_BUILD_ROOT%{_liconsdir}/%{name}.png

%post
%update_menus

%postun
%clean_menus

%clean
%{__rm} -rf $RPM_BUILD_ROOT

%files
%defattr(755,root,root,755)
%{_gamesbindir}/%{name}
%defattr(644,root,root,755)
%dir %{_gamesdatadir}/%{name}
%{_gamesdatadir}/%{name}/*
%{_mandir}/man6/cu*.6*
%{_menudir}/%{name}
%{_miconsdir}/%{name}.png
%{_iconsdir}/%{name}.png
%{_liconsdir}/%{name}.png
