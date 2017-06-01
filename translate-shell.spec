Name:           translate-shell
Version:        0.9.6.4
Release:        1%{?dist}
Summary:        A command-line online translator

License:        Public Domain
URL:            https://github.com/soimort/translate-shell
Source0:        %{url}/archive/v%{version}.tar.gz

# BuildRequires:
Requires:       gawk
Requires:       curl
Requires:       rlwrap
Requires:       fribidi

BuildArch:      noarch

%description
Translate Shell (formerly Google Translate CLI) is a command-line
translator powered by Google Translate (default), Bing Translator,
Yandex.Translate and Apertium.

%prep
%autosetup
touch configure
chmod +x configure


%build
%configure
%make_build


%install
rm -rf $RPM_BUILD_ROOT
make PREFIX=%{buildroot}%{_prefix} install
sed -i 's|/usr/bin/env bash|/usr/bin/bash|' %{buildroot}%{_bindir}/trans


%files
%license LICENSE
%doc CONTRIBUTING.md README.md WAIVER
%{_bindir}/trans
%{_mandir}/man1/trans.1*



%changelog
* Thu Jun 01 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.4-1
- Update to 0.9.6.4

* Wed May 31 2017 Vasiliy N. Glazov <vascom2@gmail.com> 0.9.6.3-1
- Initial packaging
