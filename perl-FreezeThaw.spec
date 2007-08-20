%define module 	FreezeThaw
%define version 0.43
%define release %mkrel 5

Summary:	%{module} perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group:		Development/Perl
Url:		http://www.cpan.org
Source0:	%{module}-%{version}.tar.bz2
BuildRequires:	perl-devel >= 5.8.6
Requires: 	perl >= 5.8.6
BuildRoot: 	%{_tmppath}/%{name}-%{version}-buildroot
Buildarch: 	noarch

%description
%{module} convert Perl structures to strings and back. 

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf $RPM_BUILD_ROOT
%makeinstall_std

%clean 
rm -rf $RPM_BUILD_ROOT

%files 
%defattr(-,root,root)
%doc README MANIFEST Changes
%{perl_vendorlib}/*.pm
%{_mandir}/*/*


