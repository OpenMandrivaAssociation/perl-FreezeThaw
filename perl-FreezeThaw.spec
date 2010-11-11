%define upstream_name 	 FreezeThaw
%define upstream_version 0.5001

Name:       perl-%{upstream_name}
Version:    %perl_convert_version %{upstream_version}
Release:    %mkrel 1
Summary:	Converting Perl structures to strings and back
License: 	GPL+ or Artistic
Group:		Development/Perl
Url:        http://search.cpan.org/dist/%{upstream_name}
Source0:    http://www.cpan.org/modules/by-module/Freeze/%{upstream_name}-%{upstream_version}.tar.gz

Buildarch: 	noarch
BuildRoot: 	%{_tmppath}/%{name}-%{version}-%{release}

%description
Converts data to/from stringified form, appropriate for saving-to/reading-from
permanent storage.

Deals with objects, circular lists, repeated appearence of the same refence.
Does not deal with overloaded stringify operator yet.

%prep
%setup -q -n %{upstream_name}-%{upstream_version}
find . -type f | xargs chmod 644
find . -type d | xargs chmod 755

%build
%{__perl} Makefile.PL INSTALLDIRS=vendor
%make

%install
rm -rf %{buildroot}
%makeinstall_std

%check
make test

%clean 
rm -rf %{buildroot}

%files 
%defattr(-,root,root)
%doc README MANIFEST Changes
%{perl_vendorlib}/*.pm
%{_mandir}/*/*
