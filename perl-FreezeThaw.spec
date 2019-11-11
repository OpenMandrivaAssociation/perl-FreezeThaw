%define upstream_name 	 FreezeThaw
%define upstream_version 0.5001

Name:		perl-%{upstream_name}
Version:	%perl_convert_version %{upstream_version}
Release:	6
Summary:	Converting Perl structures to strings and back
License:	GPL+ or Artistic
Group:		Development/Perl
Url:		http://search.cpan.org/dist/%{upstream_name}
Source0:	http://www.cpan.org/modules/by-module/Freeze/%{upstream_name}-%{upstream_version}.tar.gz

BuildRequires:	perl-devel
BuildArch: 	noarch

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
perl Makefile.PL INSTALLDIRS=vendor
%make_build

%install
%make_install

%files 
%doc README MANIFEST Changes
%{perl_vendorlib}/*.pm
%{_mandir}/*/*


%changelog
* Mon May 31 2010 Guillaume Rousse <guillomovitch@mandriva.org> 0.500.100-2mdv2010.1
+ Revision: 546785
- fix file perms (#59584)
- better description and summary

* Tue Apr 06 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.500.100-1mdv2010.1
+ Revision: 532147
- update to 0.5001

* Mon Mar 08 2010 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.500.0-1mdv2010.1
+ Revision: 515661
- update to 0.50

* Wed Jul 29 2009 JÃ©rÃ´me Quelin <jquelin@mandriva.org> 0.450.0-1mdv2010.0
+ Revision: 403184
- rebuild using %%perl_convert_version

* Mon Feb 16 2009 Guillaume Rousse <guillomovitch@mandriva.org> 0.45-1mdv2009.1
+ Revision: 341079
- new version
- new version

* Wed Jul 23 2008 Thierry Vignaud <tv@mandriva.org> 0.43-7mdv2009.0
+ Revision: 241228
- rebuild
- kill re-definition of %%buildroot on Pixel's request

  + Olivier Blin <oblin@mandriva.com>
    - restore BuildRoot

* Mon Aug 20 2007 Thierry Vignaud <tv@mandriva.org> 0.43-5mdv2008.0
+ Revision: 67615
- use %%mkrel
- simplify buildrequires


* Thu Feb 03 2005 Lenny Cartier <lenny@mandrakesoft.com> 0.43-5mdk
- rebuild

* Sat Oct 11 2003 Tibor Pittich <Tibor.Pittich@phuture.sk> 0.43-4mdk
- rebuild for new perl
- add GPL into License tag
- remove $RPM_OPT_FLAGS
- mascroszification of make
- add make test
- don't use PREFIX

* Wed May 28 2003 Thierry Vignaud <tvignaud@mandrakesoft.com> 0.43-3mdk
- rebuild for new auto{prov,req}

* Wed Jan 29 2003 Lenny Cartier <lenny@mandrakesoft.com> 0.43-2mdk
- rebuild

* Fri Jan 17 2003 François Pons <fpons@mandrakesoft.com> 0.43-1mdk
- 0.43.

* Thu Jul 25 2002 Lenny Cartier <lenny@mandrakesoft.com> 0.41-2mdk
- rebuild with new perl

* Wed Aug 29 2001 Lenny Cartier <lenny@mandrakesoft.com> 0.41-1mdk
- added by Christian Zoffoli <czoffoli@linux-mandrake.com> :
	- First Mandrake Release

