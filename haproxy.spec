Name:		haproxy
Version:	1.4.22
Release:	2
Summary:	TCP/HTTP reverse proxy for high availability environments
License:	GPLv2+
Group:		System/Servers
URL:		http://haproxy.1wt.eu/
Source0:	http://haproxy.1wt.eu/download/1.4/src/%{name}-%{version}.tar.gz
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

It needs very little resource. Its event-driven architecture allows it
to easily handle thousands of simultaneous connections on hundreds of instances
without risking the system's stability.

%prep
%setup -q

%build
#%{__make} USE_PCRE=1 "COPTS.pcre=-DUSE_PCRE $(pcre-config --cflags)" DEBUG="" TARGET=linux26
%serverbuild
%make TARGET=linux26 CFLAGS="%{optflags}"  

%install
 
mkdir -p %{buildroot}%{_sbindir}
mkdir -p %{buildroot}%{_initrddir}
mkdir -p %{buildroot}%{_sysconfdir}/%{name}

cp %{name} %{buildroot}%{_sbindir}/
cp examples/%{name}.cfg %{buildroot}%{_sysconfdir}/%{name}/
cp examples/%{name}.init %{buildroot}%{_initrddir}/%{name}
 
%files
%doc CHANGELOG TODO examples doc/haproxy-en.txt doc/haproxy-fr.txt doc/architecture.txt examples/url-switching.cfg
%attr(0755,root,root) %{_sbindir}/%{name}
%dir %{_sysconfdir}/%{name}
%attr(0644,root,root) %config(noreplace) %{_sysconfdir}/%{name}/%{name}.cfg
%attr(0755,root,root) %config %{_initrddir}/%{name}



%changelog
* Wed Sep 19 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.4.22-1
+ Revision: 817114
- update to 1.4.22

* Mon May 21 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.4.21-1
+ Revision: 799751
- update to 1.4.21
- fix license

* Mon Mar 12 2012 Dmitry Mikhirev <dmikhirev@mandriva.org> 1.4.20-1
+ Revision: 784373
- new version 1.4.20

* Tue Feb 28 2012 Alexander Khrukin <akhrukin@mandriva.org> 1.4.19-1
+ Revision: 781267
- version update 1.4.19

* Wed May 11 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.4.15-1
+ Revision: 673626
- update to 1.4.15 (and take the maintainership of it)

* Wed Mar 16 2011 Stéphane Téletchéa <steletch@mandriva.org> 1.4.13-1
+ Revision: 645235
- update to new version 1.4.13

* Mon Feb 14 2011 Sandro Cazzaniga <kharec@mandriva.org> 1.4.11-1
+ Revision: 637801
- update to 1.4.11

* Tue Nov 30 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4.10-1mdv2011.0
+ Revision: 603973
- update to 1.4.10

* Sat Nov 27 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4.9-1mdv2011.0
+ Revision: 601804
- update to 1.4.9

* Fri Jul 23 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4.8-1mdv2011.0
+ Revision: 557114
- update to 1.4.8

* Wed Apr 14 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4.4-1mdv2010.1
+ Revision: 534796
- Don't define name, version, release on top of spec
- new version 1.4.4

* Sun Apr 04 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4.3-1mdv2010.1
+ Revision: 531224
- update to 1.4.3

* Sun Mar 21 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4.2-1mdv2010.1
+ Revision: 525988
- Update to new version 1.4.2

* Fri Mar 05 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4.1-1mdv2010.1
+ Revision: 514432
- fix source
- update to 1.4.1

* Tue Mar 02 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.4.0-1mdv2010.1
+ Revision: 513327
- Update to 1.4.0
- Fix License
- Clean spec

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 1.3.22-1mdv2010.1
+ Revision: 462704
- update to new version 1.3.22

* Sat Nov 07 2009 Frederik Himpe <fhimpe@mandriva.org> 1.3.21-1mdv2010.1
+ Revision: 462696
- update to new version 1.3.21

* Tue Jul 28 2009 Frederik Himpe <fhimpe@mandriva.org> 1.3.19-1mdv2010.0
+ Revision: 402533
- update to new version 1.3.19

* Sat Jun 27 2009 Frederik Himpe <fhimpe@mandriva.org> 1.3.18-1mdv2010.0
+ Revision: 389589
- Update to new version 1.3.18
- Use Mandriva server CFLAGS

* Thu Apr 16 2009 Anne Nicolas <ennael@mandriva.org> 1.3.17-2mdv2009.1
+ Revision: 367606
- fix initrddir macro for MES 5 compatibility

* Wed Apr 15 2009 Anne Nicolas <ennael@mandriva.org> 1.3.17-1mdv2009.1
+ Revision: 367278
- fix group
- import haproxy


