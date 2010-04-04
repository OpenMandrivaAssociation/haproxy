%define name    haproxy
%define version 1.4.3
%define release %mkrel 1

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	TCP/HTTP reverse proxy for high availability environments
License:	GPLv2
Group:		System/Servers
URL:		http://haproxy.1wt.eu/
Source0:	http://haproxy.1wt.eu/download/1.4/src/%{name}-%{version}.tar.gz
BuildRoot:	%{_tmppath}/%{name}-%{version}-%{release}-root
BuildRequires:	libpcre-devel

%description
HA-Proxy is a TCP/HTTP reverse proxy which is particularly suited for high
availability environments. Indeed, it can:
- route HTTP requests depending on statically assigned cookies
- spread the load among several servers while assuring server persistence
  through the use of HTTP cookies
- switch to backup servers in the event a main one fails
- accept connections to special ports dedicated to service monitoring
- stop accepting connections without breaking existing ones
- add/modify/delete HTTP headers both ways
- block requests matching a particular pattern

It needs very little resource. Its event-driven architecture allows it to easily
handle thousands of simultaneous connections on hundreds of instances without
risking the system's stability.

%prep
%setup -q

%build
#%{__make} USE_PCRE=1 "COPTS.pcre=-DUSE_PCRE $(pcre-config --cflags)" DEBUG="" TARGET=linux26
%serverbuild
%make TARGET=linux26 CFLAGS="%{optflags}"  

%install
rm -rf %{buildroot}
 
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}

cp %{name} %{buildroot}%{_sbindir}/
cp examples/%{name}.cfg %{buildroot}%{_sysconfdir}/%{name}/
cp examples/%{name}.init %{buildroot}%{_initrddir}/%{name}
 
%clean
rm -rf $RPM_BUILD_ROOT
 
%files
%defattr(-,root,root)
%doc CHANGELOG TODO examples doc/haproxy-en.txt doc/haproxy-fr.txt doc/architecture.txt examples/url-switching.cfg
%attr(0755,root,root) %{_sbindir}/%{name}
%dir %{_sysconfdir}/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.cfg
%attr(0755,root,root) %config %{_initrddir}/%{name}

