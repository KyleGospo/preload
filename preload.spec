Name:           preload
Version:        {{{ git_dir_version }}}
Release:        1%{?dist}
Summary:        Improves application startup time by preloading commonly used applications into memory
License:        GPLv2
URL:            https://github.com/KyleGospo/preload

Source:         {{{ git_dir_pack }}}

Requires:       systemd
Requires:       logrotate

BuildRequires:  git
BuildRequires:  meson
BuildRequires:  cmake
BuildRequires:  gcc
BuildRequires:  glib2-devel
BuildRequires:  systemd-rpm-macros
BuildRequires:  help2man

%description
preload is an adaptive readahead daemon. It monitors applications that users run, and by analyzing this data, predicts what applications users might run, and fetches those binaries and their dependencies into memory for faster startup times.

# Disable debug packages
%define debug_package %{nil}

%prep
{{{ git_dir_setup_macro }}}

%build
meson build -Dprefix=%{_prefix} --bindir=%{_sbindir}
ninja -C build

%install
DESTDIR=%{buildroot} meson install -C build

install -d %{buildroot}%{_unitdir}
cat > %{buildroot}%{_unitdir}/preload.service << EOF
[Unit]
Description=Adaptive readahead daemon
After=kdm.service

[Service]
Type=forking
ExecStart=/usr/sbin/preload --verbose 1
Restart=always
RestartSec=1
Nice=19
IOSchedulingClass=3

[Install]
WantedBy=multi-user.target
EOF

install -d %{buildroot}%{_sysconfdir}/logrotate.d
cat > %{buildroot}%{_sysconfdir}/logrotate.d/preload << EOF
/var/log/preload.log {
    missingok
    notifempty
    size=64k
    compress
    postrotate
        /bin/kill -HUP `/sbin/pidof preload 2>/dev/null` 2> /dev/null || true
    endscript
}
EOF

install -d %{buildroot}%{_sysconfdir}/sysconfig
cat > %{buildroot}%{_sysconfdir}/sysconfig/preload << EOF
# Miminum memory that the system should have for preload to be launched.
# In megabytes.
MIN_MEMORY="256"

# Command-line arguments to pass to the daemon.  Read preload(8) man page
# for available options.
PRELOAD_OPTS="--verbose 1"

# Option to call ionice with.  Leave empty to skip ionice.
IONICE_OPTS="-c3"
EOF

mkdir -p %{buildroot}%{_localstatedir}/lib/preload/

%post
%systemd_post preload

%preun
%systemd_preun preload

%postun
%systemd_postun_with_restart preload

%files
%license LICENSE
%doc README.md
%config(noreplace) %{_sysconfdir}/preload.conf
%config(noreplace) %{_sysconfdir}/sysconfig/preload
%config(noreplace) %{_sysconfdir}/logrotate.d/preload
%{_datadir}/man/man8/preload.8.gz
%{_sbindir}/preload
%{_unitdir}/preload.service
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_localstatedir}/log/preload.log
%attr(0644,root,root) %ghost %config(missingok,noreplace) %{_localstatedir}/lib/preload/preload.state
%attr(0755,root,root) %dir %{_localstatedir}/lib/preload

%changelog
{{{ git_dir_changelog }}}