Summary:	Japanese SKK input method for IBus
Summary(pl.UTF-8):	Metoda wprowadzania znaków japońskich SKK dla platformy IBus
Name:		ibus-skk
Version:	1.3.7
Release:	1
License:	GPL v2+
Group:		Libraries
Source0:	http://cloud.github.com/downloads/ueno/ibus-skk/%{name}-%{version}.tar.gz
# Source0-md5:	d8ed00a6cdeba7cc5c613f970dff599d
URL:		http://github.com/ueno/ibus-skk
BuildRequires:	gettext-devel
BuildRequires:	intltool >= 0.35.0
BuildRequires:	python-devel >= 1:2.5
Requires:	ibus
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
%doc AUTHORS ChangeLog NEWS README THANKS TODO
%attr(755,root,root) %{_bindir}/ibus-skk-convert-jisyo
%attr(755,root,root) %{_libexecdir}/ibus-engine-skk
%attr(755,root,root) %{_libexecdir}/ibus-setup-skk
%{_datadir}/ibus-skk
%{_datadir}/ibus/component/skk.xml
