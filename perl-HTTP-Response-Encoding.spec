%define modname	HTTP-Response-Encoding
%define modver	0.06

Summary:	Adds encoding() to HTTP::Response
Name:		perl-%{modname}
Version:	%{modver}
Release:	19
License:	GPLv2+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/HTTP-Response-Encoding
Source0:	https://cpan.metacpan.org/authors/id/D/DA/DANKOGAI/HTTP-Response-Encoding-%{modver}.tar.gz
BuildArch:	noarch
BuildRequires:	make
BuildRequires:	perl(Encode)
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Pod::Coverage)
BuildRequires:	perl-devel

%description
Adds encoding() to HTTP::Response.

%prep
%setup -qn %{modname}-%{modver}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes README
%{perl_vendorlib}/*
%{_mandir}/man3/*

