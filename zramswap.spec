Summary:	ZRAM swap
Name:		zramswap
Version:	201211
Release:	1
License:	GPL
Group:		Applications/System
Source0:	zramctrl
Source1:	zramswap.service
URL:		https://aur.archlinux.org/packages/zramswap/
BuildArch:	noarch
Requires(post,preun,postun):	systemd-units
Requires:	gawk
BuildRoot:	%{tmpdir}/%{name}-%{version}-root-%(id -u -n)

%description
zramctl script creates RAM based block device (named zram) which acts
as swap disk. Pages swapped to this disk are compressed and stored in
memory itself.

%prep

%build

%install
rm -rf $RPM_BUILD_ROOT
install -d $RPM_BUILD_ROOT{%{_sbindir},%{systemdunitdir}}

install %{SOURCE0} $RPM_BUILD_ROOT%{_sbindir}
install %{SOURCE1} $RPM_BUILD_ROOT%{systemdunitdir}

%clean
rm -rf $RPM_BUILD_ROOT

%post
%systemd_post zramswap.service

%preun
%systemd_preun zramswap.service

%postun
%systemd_postun

%files
%defattr(644,root,root,755)
%attr(755,root,root) %{_sbindir}/zramctrl
%{systemdunitdir}/zramswap.service

