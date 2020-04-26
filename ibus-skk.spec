Summary:	Japanese SKK input method for IBus
Summary(pl.UTF-8):	Metoda wprowadzania znaków japońskich SKK dla platformy IBus
Name:		ibus-skk
Version:	1.4.3
Release:	1
License:	GPL v2+
Group:		Libraries
#Source0Download: https://github.com/ueno/ibus-skk/releases
Source0:	https://github.com/ueno/ibus-skk/releases/download/%{name}-%{version}/%{name}-%{version}.tar.xz
# Source0-md5:	17b27a2044ff6b9577f7b7927d05876d
URL:		http://github.com/ueno/ibus-skk
BuildRequires:	gettext-tools
BuildRequires:	gtk+3-devel >= 3.0
BuildRequires:	ibus-devel >= 1.5.11
BuildRequires:	intltool >= 0.35.0
BuildRequires:	libskk-devel >= 1.0.2
BuildRequires:	tar >= 1:1.22
# not required for releases
#BuildRequires:	vala >= 2:0.10.0
BuildRequires:	xz
Requires:	ibus >= 1.5.11
Requires:	libskk >= 1.0.2
Requires:	skkdic
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
A Japanese Simple Kana Kanji Input Method Engine for IBus.

%description -l pl.UTF-8
Silnik metody wprowadzania znaków japońskich SKK (Simple Kana Kanji)
dla platformy IBus.

%prep
%setup -q

%build
%configure
%{__make}

%install
rm -rf $RPM_BUILD_ROOT

%{__make} install \
	DESTDIR=$RPM_BUILD_ROOT

%find_lang %{name}

%clean
rm -rf $RPM_BUILD_ROOT

%files -f %{name}.lang
%defattr(644,root,root,755)
%doc AUTHORS ChangeLog NEWS README THANKS
%attr(755,root,root) %{_libexecdir}/ibus-engine-skk
%attr(755,root,root) %{_libexecdir}/ibus-setup-skk
%{_datadir}/ibus-skk
%{_datadir}/ibus/component/skk.xml
%{_desktopdir}/ibus-setup-skk.desktop
