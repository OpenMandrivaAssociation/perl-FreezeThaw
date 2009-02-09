%define module 	FreezeThaw
%define version 0.44
%define release %mkrel 1

Summary:	%{module} perl module
Name: 		perl-%{module}
Version: 	%{version}
Release: 	%{release}
License: 	GPL or Artistic
Group:		Development/Perl
URL:        http://search.cpan.org/dist/%{module}
Source:     http://www.cpan.org/modules/by-module/Freeze/%{module}-%{version}.tar.gz
Buildarch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}

%description
%{module} convert Perl structures to strings and back. 

%prep
%setup -q -n %{module}-%{version}

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make
make test

%install
rm -rf %{buildroot}
%makeinstall_std

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README MANIFEST Changes
%{perl_vendorlib}/*.pm
%{_mandir}/*/*
