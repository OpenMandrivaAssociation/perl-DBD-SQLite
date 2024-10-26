%define upstream_name DBD-SQLite

Name:		perl-%{upstream_name}
Version:	1.76
Release:	1

Summary:	Self Contained RDBMS in a DBI Driver
License:	GPL
Group:		Development/Perl
URL:		https://metacpan.org/pod/DBD::SQLite
Source0:	https://cpan.metacpan.org/authors/id/I/IS/ISHIGAKI/DBD-SQLite-%{version}.tar.gz
BuildRequires:	perl-devel
BuildRequires:	perl(DBI)
BuildRequires:	perl(ExtUtils::MakeMaker)
BuildRequires:	perl(File::Spec)
BuildRequires:	perl(Test::Builder)
BuildRequires:	perl(Test::More)
BuildRequires:	perl(Tie::Hash)
BuildRequires:	sqlite3-devel >= 3.6.0

# Get rid of perl_convert_version remains
Obsoletes:	%{name} = 1.700.0-1

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
%autosetup -p1 -n %{upstream_name}-%{version}
perl Makefile.PL INSTALLDIRS=vendor

%build
%make_build

%check
make test

%install
%make_install

# useless content
rm -f %{buildroot}%{perl_vendorarch}/auto/share/dist/DBD-SQLite/sqlite3.c
rm -f %{buildroot}%{perl_vendorarch}/auto/share/dist/DBD-SQLite/sqlite3.h
rm -f %{buildroot}%{perl_vendorarch}/auto/share/dist/DBD-SQLite/sqlite3ext.h

%files
%doc README* Changes
%{perl_vendorarch}/DBD
%{perl_vendorarch}/auto/DBD
%{_mandir}/*/*
