%define upstream_name    HTTP-Response-Encoding
%define upstream_version 0.06

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	7

Summary:	Adds encoding() to HTTP::Response
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/HTTP/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl(Encode)
BuildRequires:	perl(HTML::Parser)
BuildRequires:	perl(HTTP::Response)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Test::Pod)
BuildRequires:	perl(Pod::Coverage)
BuildRequires:	perl-devel
BuildArch:	noarch

%description
Adds encoding() to HTTP::Response.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

%build
%__perl Makefile.PL INSTALLDIRS=vendor
%make

%install
%makeinstall_std

%files
%doc Changes README
%{_mandir}/man3/*
%{perl_vendorlib}/*


%changelog
* Mon Apr 25 2011 Funda Wang <fwang@mandriva.org> 0.60.0-2mdv2011.0
+ Revision: 658907
- add br
- rebuild for updated spec-helper

* Sat Aug 01 2009 Jérôme Quelin <jquelin@mandriva.org> 0.60.0-1mdv2010.0
+ Revision: 405860
- update to 0.06
- using %%perl_convert_version
- fixed license field

* Tue Oct 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2009.1
+ Revision: 297818
- import perl-HTTP-Response-Encoding


* Tue Oct 28 2008 Guillaume Rousse <guillomovitch@mandriva.org> 0.05-1mdv2009.1
- initial mdv release, generated with cpan2dist
