%define module   HTTP-Response-Encoding
%define version    0.05
%define release    %mkrel 1

Name:       perl-%{module}
Version:    %{version}
Release:    %{release}
License:    GPL or Artistic
Group:      Development/Perl
Summary:    Adds encoding() to HTTP::Response
Url:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/HTTP/%{module}-%{version}.tar.gz
BuildRequires: perl-devel
BuildRequires: perl(Encode)
BuildRequires: perl(HTTP::Response)
BuildRequires: perl(Test::More)
BuildArch: noarch
BuildRoot:  %{_tmppath}/%{name}-%{version}

%description
no description found

%prep
%setup -q -n %{module}-%{version} 

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
rm -rf %buildroot
%makeinstall_std

%clean
rm -rf %buildroot

%files
%defattr(-,root,root)
%doc Changes README
%{_mandir}/man3/*
%perl_vendorlib/*


