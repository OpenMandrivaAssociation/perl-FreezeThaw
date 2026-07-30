%define upstream_name 	 FreezeThaw
%define upstream_version 0.5001
Name:		perl-%{upstream_name}
Version:	0.5001
Release:	1
Summary:	Converting Perl structures to strings and back
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		https://metacpan.org/dist/FreezeThaw
Source0:	https://cpan.metacpan.org/authors/id/I/IL/ILYAZ/modules/FreezeThaw-0.5001.tar.gz

BuildRequires:	make
BuildRequires:	perl-devel
BuildArch: 	noarch

%description
Converts data to/from stringified form, appropriate for saving-to/reading-from
permanent storage.

Deals with objects, circular lists, repeated appearence of the same refence.
Does not deal with overloaded stringify operator yet.

%prep
%setup -q -n %{upstream_name}-%{version}
find . -type f | xargs chmod 644
find . -type d | xargs chmod 755

%build
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files 
%doc README MANIFEST Changes
%{perl_vendorlib}/*.pm
%{_mandir}/*/*


