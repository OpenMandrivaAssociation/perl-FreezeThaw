%define upstream_name 	 FreezeThaw
%define upstream_version 0.5001

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1

Summary:	%{upstream_name} perl module
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Freeze/%{upstream_name}-%{upstream_version}.tar.gz

Buildarch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
%{upstream_name} convert Perl structures to strings and back. 

%prep
%setup -q -n %{upstream_name}-%{upstream_version}

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
