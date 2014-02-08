%define	module	DBD-SQLite
%define	modver	1.37

%define debug_package %{nil}

Name:		perl-%{module}
Version:	%{perl_convert_version %{modver}}
Release:	4

Summary:	Self Contained RDBMS in a DBI Driver
License:	GPL
Group:		Development/Perl
URL:		http://search.cpan.org/dist/%{module}/
Source0:	ftp://ftp.perl.org/pub/CPAN/modules/by-module/DBD/%{module}-%{modver}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(DBI) >= 1.616.0-5
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec) >= 0.820.0
BuildRequires:	perl(Test::Builder) >= 0.860.0
BuildRequires:	perl(Test::More) >= 0.470.0
BuildRequires:	perl(Tie::Hash)
BuildRequires:	pkgconfig(sqlite3)

%description
SQLite is a small fast embedded SQL database engine.

DBD::SQLite embeds that database engine into a DBD driver, so
if you want a relational database for your project, but don't
want to install a large RDBMS system like MySQL or PostgreSQL,
then DBD::SQLite may be just what you need.

It supports quite a lot of features, such as transactions (atomic
commit and rollback), indexes, DBA-free operation, a large subset
of SQL92 supported, and more.

%prep
%setup -q -n %{module}-%{modver}

%build
perl Makefile.PL INSTALLDIRS=vendor
%make

%check
make test

%install
%makeinstall_std

# useless content
rm %{buildroot}%{perl_vendorarch}/auto/share/dist/DBD-SQLite/sqlite3.c
rm %{buildroot}%{perl_vendorarch}/auto/share/dist/DBD-SQLite/sqlite3.h

%files
%doc README* Changes
%{perl_vendorarch}/DBD
%{perl_vendorarch}/auto/DBD
%{_mandir}/*/*

%changelog
* Wed Dec 19 2012 Per Øyvind Karlsen <peroyvind@mandriva.org> 1.370.0-2
- rebuild for new perl

* Thu Jan 26 2012 Oden Eriksson <oeriksson@mandriva.com> 1.360.0-0.3
+ Revision: 769166
- disable the tests for now
- fix build
- bump release
- another try at it...
- fix build
- use a pre-release of 1.36
- rebuilt for perl-5.14.2
- bump release
- fix deps (after looking at mageia)
- 1.35
- fix deps so that it pulls the latest DBI release
- force it
- rebuild

  + Per Øyvind Karlsen <peroyvind@mandriva.org>
    - svn commit -m mass rebuild of perl extension against perl 5.14.2

* Tue May 31 2011 Guillaume Rousse <guillomovitch@mandriva.org> 1.330.0-1
+ Revision: 682116
- update to new version 1.33

* Wed May 04 2011 Oden Eriksson <oeriksson@mandriva.com> 1.310.0-2
+ Revision: 667066
- mass rebuild

* Sat Oct 16 2010 Guillaume Rousse <guillomovitch@mandriva.org> 1.310.0-1mdv2011.0
+ Revision: 586098
- new version

* Sun Aug 01 2010 Funda Wang <fwang@mandriva.org> 1.290.0-4mdv2011.0
+ Revision: 564402
- rebuild for perl 5.12.1

* Tue Jul 20 2010 Sandro Cazzaniga <kharec@mandriva.org> 1.290.0-3mdv2011.0
+ Revision: 555461
- rebuild

  + Jérôme Quelin <jquelin@mandriva.org>
    - rebuild for 5.12

* Sat Jan 09 2010 Jérôme Quelin <jquelin@mandriva.org> 1.290.0-1mdv2010.1
+ Revision: 487931
- update to 1.29

* Tue Nov 24 2009 Jérôme Quelin <jquelin@mandriva.org> 1.270.0-1mdv2010.1
+ Revision: 469437
- update to 1.27

* Fri Jul 17 2009 Jérôme Quelin <jquelin@mandriva.org> 1.250.0-1mdv2010.0
+ Revision: 396886
- rebuild for new auto provides extraction
- using %%perl_convert_version

* Thu Apr 30 2009 Jérôme Quelin <jquelin@mandriva.org> 1.25-1mdv2010.0
+ Revision: 369171
- forgot to add new source
- update to 1.25

* Sat Mar 07 2009 Antoine Ginies <aginies@mandriva.com> 1.14-6mdv2009.1
+ Revision: 351712
- rebuild

* Sun Aug 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-5mdv2009.0
+ Revision: 273082
- fix tests, using debian patch
- re-enable all tests

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild

* Sun Feb 17 2008 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-2mdv2008.1
+ Revision: 169871
- disable failing tests, as a module with a few issues is better than no module
  at all

  + Thierry Vignaud <tv@mandriva.org>
    - rebuild
    - kill re-definition of %%buildroot on Pixel's request

  + Pixel <pixel@mandriva.com>
    - rebuild for perl-5.10.0

  + Olivier Blin <blino@mandriva.org>
    - restore BuildRoot

* Fri Oct 12 2007 Guillaume Rousse <guillomovitch@mandriva.org> 1.14-1mdv2008.1
+ Revision: 97440
- update to new version 1.14


* Sun Dec 17 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-2mdv2007.0
+ Revision: 98263
- fix build dependencies

* Sat Dec 16 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.13-1mdv2007.1
+ Revision: 98198
- new version

* Tue Aug 08 2006 Olivier Thauvin <nanardon@mandriva.org> 1.12-2mdv2007.0
+ Revision: 53730
- rebuild
- Import perl-DBD-SQLite

* Fri Apr 14 2006 Guillaume Rousse <guillomovitch@mandriva.org> 1.12-1mdk
- New release 1.12
- better source URL
- better buildrequires syntax

* Tue Dec 20 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.11-1mdk
- new version
- fix directory ownership

* Tue Sep 27 2005 Guillaume Rousse <guillomovitch@mandriva.org> 1.09-2mdk 
- rebuild to link against external library
- spec cleanup
- %%mkrel

* Wed Jun 22 2005 Rafael Garcia-Suarez <rgarciasuarez@mandriva.com> 1.09-1mdk
- 1.09
- spec cleanups

* Mon Mar 14 2005 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.08-1mdk
- new veresion 1.08

* Mon Nov 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.07-2mdk 
- rebuild for new perl
- remove README.urpmi

* Fri Oct 15 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.07-1mdk
- 1.07.

* Wed Aug 11 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.03-1mdk
- 1.03.
- Remove patch 1.

* Thu Jul 29 2004 Rafael Garcia-Suarez <rgarciasuarez@mandrakesoft.com> 1.00-1mdk
- 1.00, incompatible format with previous versions.
- Remove MANIFEST, add README.update.urpmi.
- Patch to prevent interactivity in Makefile.PL

* Tue May 18 2004 Olivier Thauvin <thauvin@aerov.jussieu.fr> 0.31-2mdk
- Fix compile FLAGS

