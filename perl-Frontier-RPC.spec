%define module	Frontier-RPC
%define name	perl-%{module}
%define version 0.07b4
%define release %mkrel 2

Name:		%{name}
Version:	%{version}
Release:	%{release}
Summary:	%{module} module for perl
License:	GPL or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{module}/
Source:		http://search.cpan.org/CPAN/authors/id/K/KM/KMACLEOD/%{module}-%{version}.tar.bz2
BuildRequires:	perl(XML::Parser)
BuildRequires:	perl(LWP::UserAgent)
BuildArch:	noarch
BuildRoot:	%{_tmppath}/%{name}-%{version}

%description
Frontier::RPC implements UserLand Software's XML RPC (Remote Procedure Calls
using Extensible Markup Language).  Frontier::RPC includes both a client module
for making requests to a server and several server modules for implementing
servers using CGI, Apache, and standalone with HTTP::Daemon.

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%{__make}

%check
%{__make} test

%clean 
rm -rf %{buildroot}

%install
rm -rf %{buildroot}
%makeinstall_std
rm -f %{buildroot}%{perl_vendorlib}/MIME/changes.pod

%files
%defattr(-,root,root)
%doc ChangeLog COPYING README
%{perl_vendorlib}/Frontier
%{perl_vendorlib}/Apache
%{_mandir}/*/*
