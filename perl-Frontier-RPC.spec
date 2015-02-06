%define module	Frontier-RPC

Name:		perl-%{module}
Version:	0.07b4
Release:	5
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://search.cpan.org/CPAN/authors/id/K/KM/KMACLEOD/%{module}-%{version}.tar.bz2

BuildRequires:	perl-devel
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(LWP::UserAgent)
BuildRequires:	perl(HTTP::Daemon)
BuildArch:	noarch

%description
Frontier::RPC implements UserLand Software's XML RPC (Remote Procedure Calls
using Extensible Markup Language).  Frontier::RPC includes both a client module
for making requests to a server and several server modules for implementing
servers using CGI, Apache, and standalone with HTTP::Daemon.

%prep
%setup -q -n %{module}-%{version}

%build
perl Makefile.PL INSTALLDIRS=vendor
make

%check
make test

%install
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/MIME/changes.pod

%files
%doc ChangeLog COPYING README
%{perl_vendorlib}/Frontier
%{perl_vendorlib}/Apache
%{_mandir}/*/*

%changelog
* Fri May 15 2009 Jérôme Quelin <jquelin@mandriva.org> 0.07b4-2mdv2010.0
+ Revision: 375949
- rebuild

* Sat Mar 14 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.07b4-1mdv2009.1
+ Revision: 354995
- fix build dependencies

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

  + Thierry Vignaud <tv@mandriva.org>
    - kill re-definition of %%buildroot on Pixel's request

  + Buchan Milne <bgmilne@mandriva.org>
    - Import perl-Frontier-RPC



* Mon Mar 20 2006 Buchan Milne <bgmilne@mandriva.org> 0.07b4-1mdk
- First Mandriva package
