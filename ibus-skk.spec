Summary:	Japanese SKK input method for ibus
Name:		ibus-skk
Version:	1.3.7
Release:	0.1
License:	GPL v2+
Group:		Libraries
Source0:	http://cloud.github.com/downloads/ueno/ibus-skk/%{name}-%{version}.tar.gz
# Source0-md5:	d8ed00a6cdeba7cc5c613f970dff599d
URL:		http://github.com/ueno/ibus-skk
BuildRequires:	pkgconfig
BuildRequires:	python-devel
Requires:	ibus
Requires:	skkdic
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%define		_libexecdir	%{_libdir}/ibus

%description
A Japanese Simple Kana Kanji Input Method Engine for ibus.

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
%doc AUTHORS README TODO
%attr(755,root,root) %{_bindir}/ibus-skk-convert-jisyo
%attr(755,root,root) %{_libexecdir}/ibus-*-skk
%{_datadir}/ibus-skk
%{_datadir}/ibus/component/skk.xml
